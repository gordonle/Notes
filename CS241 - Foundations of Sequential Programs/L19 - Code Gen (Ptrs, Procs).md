CS240 L19 | March 21^st^, 2019

Recall, for pointers when we see `NULL` we want to use non-negative non-multiple of 4, say 1.

### Pointer Arithmetic

Meaning is based on types used. 

- `int` + `int` $\to$ `int`
- `int*` + `int`
- `int` + `int*`

In our grammar, we have the rule $expr_1\to expr_2 + term$. If $expr_2:int *\:, term:int$

```
code(expr1) =
	code(expr2)
	push($3)
	code(term)
	mult $3, $4
	mflo $3
	pop($5)
	add $3, $5, $3 // with subtraction, we subtract here
```

If $expr_2:int\:, term:int*$, then we have to multiply the first by 4 instead. Subtraction works similarly. Instead of adding at the end, we would subtract. 

#### Subtraction

$expr_1\to expr_2 - term$, $expr_2:int*\:, term:int*$ . The result is an `int`- the number of items between them.

```
code(expr1) =
	code(expr2)
	push($3)
	code(term)
	pop($5)
	sub $3, $5, $3
	div $3, $4
	mflo $3 \\ quotient is in lo, remainder is in hi
```

#### Assignment through Pointer Dereference

==LHS==: address at which to store the value

==RHS==: the value

$statement\to$ ID BECOMES $expr_2$ SEMI, or $statement\to$ STAR $expr1$ BECOMES $expr_2$ SEMI.

Our `lvalue`s are “ID” or “STAR $expr_1$”. We have to now calculate the value of $expr_1$ and use this as an address to store the value of $expr_2$.

```
code(statement) =
	code(expr2)
	push($3)
	code(expr1)
	pop($5)
	sw $5, 0($3) // this is dereferencing, saving expr2 in address of expr1
```

#### Address-of

There are two cases here. 

- ID: `&a`
- STAR $expr$: `&*a` (remember that the & and the * cancel out, but this is still valid code)

If $expr = \text{ID}$

```
code(factor) = 
	lis $3
	.word ___ //  lookup ID in symbol table to get offset value
	add $3, $29, $3
```

If $expr=\text{STAR }expr_2$

```
code(factor) =
	code(expr2)
```

### Memory Allocation

This is part of the runtime environment! We provide an allocation module: `alloc.merl`. We’ll have to link this in the same way we linked in `print.merl`, but we should link this *last*. In our prologue, we need to

- `import init`

  - Sets up allocator’s data structure
  - `init` **<u>must be called once</u>**, at the beginning of the assembly file, so call it in the prologue.
  - It takes a parameter in `$2`, which is the size of the array that I want

- `import new`

  - `$1` = number of words needed
  - returns point to memory in $3
  - returns 0 if allocation is not possible

  ```
  code(new int [expr]) =
  	code(expr)
  	add $1, $3, $0
  	call(new)
  	bne $3, $0, $1 // check: did we gt the memory address
  	add $3, $11, $0 // No, then send back NULL (1)
  ```

- `import delete`

  - `$1` = pointer to memory to deallocate

  ```
  code(delete) =
  	code(expr)
  	beq $3, $11, skipDelete // if NULL do nothing
  	add $1, $3, $0
  	call(delete)
  skipDelete:
  	// do nothing!
  ```

`new` and `delete` we’ll call as procedures.

## Calling Procedures

==The Big Picture==:

Say we have a bunch of functions, 

```c++
int f() {...}
int g() {...}
...
int wain( , int) {...}
```

- There’s stuff that we do in wain, a prologue (ie. save our two parameters on the stack). 
- then generate code main function (wain)
- then run epilogue (main program)

After this, we run it for each procedure, each has their own prologues and epilogues. 

**<u>Main Prologue/Epilogue</u>**

- save `$1`, `$2` onto stack
- import `print`, `init`, `new`, `delete`
- set `$4`, `$11`, ..
- call `init`
- reset stack at end
- `jr $31`

<u>**Procedure Specific**</u>

- don’t need the imports
- set `$29`
- save registers to protect them
- restore registers and reset stack at end
- `jr $31`

### Saving and Restoring Registers

We have a few conventions that we try to maintain. 

1. Procedures should save and restore all registers it will modify. But how do we know which ones?
   - If we aren’t sure which ones to save, save all of them except for `$3`
   - Our codegen uses `$1`-`$7`, `$11`, `$29`-`$31`
   - If your code gen uses others, that’s okay but remember to keep track and save them
   - Don’t forget to save and restore `$29`

Two approaches: suppose procedure `f` calls `g`

1. ==Caller-save==: `f` saves registers that contain critical data before calling `g`.
   - Then `g` doesn’t worry about `f`‘s registers
2. ==Callee-save==: `g` saves all registers it modifies
   - This way, `f` doesn’t worry about what `g` is going to do

Our approach is to perform **callee-save** for `$31`, and **caller-save** for everything else. Note that multiple different types of approaches can also work. 

**<u>Q:</u>** Who should save `$29`? Caller or callee?

Let’s suppose callee (`g`) saves `$29`:

```
g:  sub $29, $30, $4
	save g's registers
```

2 tasks in prologue: point `$29` to `g`’s frame, and save registers. But which one do we do first?



