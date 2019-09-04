CS241 L15 | March 7^th^, 2019

# Context Sensitive Analysis

What properties of valid C programs cannot be enforced by CFGs? 

- using **undeclared** variables/procedures
- **duplicate** declarations
- scope
- when calling **functions**, do the arguments match parameter types? Is the return type valid?
- what are valid **operations**? checking types of operands

These all correspond with ==semantic analysis==, which will be done in Assignment 8.

```text
              scanner                                                 semantic
WLP4     lexical analysis                 parsing                     analysis
Source --------------------> Tokens -------------------> Parse Tree ------------> Augmented
code     regular languages           syntactic analysis                 (A8)      Parse Tree
               (A6)                         (A7)                                      |
                                                                              code    |
                                                                           generation |
                                                                            (A9/A10)  |
                                                                                      |
                                                     MIPS          (A3/A4)           MIPS
                                                  Machine Code  <----------------  Assembly
                                                                                    Program
```

Informally, let’s look at an example.

> **Ex:** Suppose this is your parse tree class:
>
> ```c++
> class Tree {
>     public:                       // For example,
>     string rule;                  // "expr -> expr PLUS term"
>     vector<string> tokens;        // "expr", "expr", "PLUS", "term"
>     vector<Tree> children;
> };
> 
> // Tree traversal example: Print Tree
> void doSomething(const Tree &t) {
>     // can have action here, or in the for loop or after
>     for (const auto &i : t.children) {
>         doSomething(i);
>     }
> }
> ```

## Declaration Errors

This includes multiple and missing declarations. To implement this, we use a ==symbol table==, and we need to traverse the parse tree to collect all declarations. For each node that corresponds to the rule `dcl -> TYPE ID`:

- extract ID’s name and type (`int`, `int *`)
- if the name already exists in the table, we `ERROR` due to multiple declarations
- then check for `factor -> ID` and `lvalue -> id`
  - if ID’s name is not in the symbol table, `ERROR` due to undeclared variables

## Implementation - Symbol Table

We’ll need some type of global variable : `map<string, string> symbolTable`, that corresponds to `name -> type`. This doesn’t work, since we haven’t taken into consideration the *scope*. It also doesn’t handle ID’s for *procedures*. This means we will need non-global symbol tables. 

> **Ex: **Looking at potential errors.
>
> ```c++
> int f() {
>     int x = 0;
>     return 1;
> }
> int wain(int a, int b) {
>     int x = 0;
>     return 1;
> }
> // This is certainly valid. Be careful with the following case
> int f() {
>     int x = 0;
>     return 1;
> }
> int wain(int a, int b) {
>     return x; // not okay, not in scope
> }
> // Lastly
> int f() { ... }
>     f() { ... } // not okay
> ```
>
> We must permit duplicate declarations in different procedures, yet forbid duplicate declarations in the same procedure. This applies to both variables and procedure names.
>
> ** CHECK TO SEE IF WLP4 ALLOWS OVERLOADING **
>
> ==Solution==: Separate symbol table for each procedure.

We modify our global variable to collect all the procedure names. Then we’ll have our map that maps each procedure to it’s own symbol table : `map<string, map<string, string>>`, corresponding to `procedureName -> symbolTable`.

When we are traversing our parse tree, if the node corresponds to:

1. `proc -> INT ID LAREN` or `main -> INT WAIN`
   - when we encounter a new procedure, we need to check to make sure that
     - its name doesn’t already exist in the symbol table. If it does, `ERROR`
     - if not, create a new entry
   - we store the name of our procedure each time we encounter one
     - this will indicate which procedure/scope we are currently in
     - we update this every time we hit a new `proc ->` or `main ->`
2. `dcl -> TYPE ID`:
   - same as before

For variables, we only need to store the `type` and the `name`. By the time we’ve arrived here, our compiler will have dealt with overflow and such, so we don’t need to hold the value. What about the type info for procedures? 

The ==signature== of a procedure is the return type, as well as the types of arguments it takes. All procedures in WLP4 return `int`, so our signature is only the parameter types. Where should we store this? In the *top level*, since all procedures are in the global scope. So, we have `map< string, pair<vector<string>, map<string, string>>>` that corresponds to `procName -> pair<signature, symbolTable>` . To compute the signature, we traverse our parse tree! If the node rule is:

1. `paramlist -> dcl`
2. `paramlist -> dcl COMMA paramlist`
3. `(if params -> , then signature is empty)`

We need to do all of this in 1 pass, through the grammar! Let’s get into types.

## Types

Why do programming languages have types? We need the type to interpret the bits. Error checking involves making sure that things are being used properly.

A good type system prevents us from reinterpreting the bits as something else. 

```c++
int *a = nullptr;
a = 7; // ERROR
```

In WLP4, we only have two types:

1. `int`
2. `int *`

To check type correctness, we need to determine the type associated with each variable/expression, and ensure that all operators are applied to operands of the correct type. 

