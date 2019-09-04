CS241 L17 | March ^14^, 2019

# Code Generation

$$
\text{Parsing} \to_{\text{parse tree}}\text{Semantic Analysis}\to_{\text{Parse Tree, symbol table}}\text{Code Generation}\to_{\text{MIPS Assembly}}
$$

The source program is now guaranteed to be without compiler errors. There are $\infty$ many Assembly program equivalent to our WLP4 source code, so which one do we choose? We need to consider the following:

- correctness
- efficiency/optimized
  - in 241, we want the minimum number of lines of Assembly generated

Consider this **example**:

Input: `int wain (int a, int b) { return a }`. Convention: parameters of `wain` are held in `$1` and `$2`. The output will be in `$3`. 

```text
output:
	add $3, $1, $0
	jr $31
```

The problem arises when we want to change the source code. What if we want to return `b` instead of `a`?

Look at the parse tree. We need to determine where the variables/parameters are being stored. So we use our symbol table!

| Name | Type | Location |
| :--: | :--: | :------: |
|  a   | int  |    $1    |
|  b   | int  |    $2    |

Then, when traversing the parse tree for code generation, when an `ID` is encountered we look up the `ID` in the symbol table. If `a`, get back `$1`. If `b`, get back `$2`. 

How do we deal with **<u>local variables</u>**? We use registers or Memory. We only have a limited number of registers, so we typically want to store them in Memory. 

We need a stack frame pointer. This is stored in `$29`!

> **Ex:** `int wain(int a, int b) { int c = 0; return a; }`
>
> ```text
> lis $4
> .word 4
> sub $29, $30, $4
> sw $1, -4($30)
> sub $30, $30, $4
> sw $2, -4($30)
> sub $30, $30, $4
> sw $0, -4($30)
> sub $30, $30, $4
> lw $3, 0($29)
> add $30, $30, $4
> ...
> jr $31
> ```
>
> We have repeated code for pushing and popping onto the stack. This gets more complicated once we hit something like expressions (`a+b`). 

In general, for each grammar rule $A\to\gamma$, we want to $buildCode(A)$ from $code(\gamma)$. We also add the following convention: register `$3` for all output of all expressions. 

> **Ex:** `a+b`
> $$
> \begin{align}
> 	\$3 &\gets eval(a)
> 	\\ \$3 &\gets eval(b)
> 	\\ \$3 &\gets \$3 + \$3
> \end{align}
> $$
> We need a place to store pending computations - let’s try using registers. 
>
> ```text
> code(a)           ; $3 <- a
> add $5, $3, $0    ; $5 <- $3
> code(b)           ; $3 <- b
> add $3, $5, $3    ; $3 <- $3 + $5
> ```
>
> **Ex:** `a + (b + c)`. We need 3 registers.
>
> ```text
> code(a)
> add $5, $3, $0
> code(b)
> add $6, $3, $0
> code(c)
> add $3, $6, $3
> add $3, $5, $3
> ```
>
> What about `a + (b + (c + d))`? we will need 4 registers. Eventually we’ll run out of registers to use. So we should store these in memory instead.

A more general solution: use a stack! For `a + (b + (c + d))`,

```text
code(a)
push($3)
code(b)
push($3)
code(c)
push($3)
code(d)
pop($5)
add $3, $5, $3 ; c + d
pop($5)
add $3, $5, $3 ; b + (c + d)
pop($5)
add $3, $5, $3 ; a + (b + (c + d))
```

In even more general, for $expr_1 \to expr_2 + term$, 

```
code(expr1) =
	code(expr2)
	push($3)
	code(term)
	pop($5)
	add $3, $5, $3
```

## Singleton Rules

$S\to BOF \:procedure \:EOF$, $code(S) = code(procedure)$. 

$expr\to term$, $code(expr) = code(term)$. 





```c++
int wain(int a, int b) {
    int c = 0;
    return c;
}
```

