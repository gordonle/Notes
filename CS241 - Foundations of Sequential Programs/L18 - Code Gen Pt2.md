CS241 L18 | March 19^th^, 2019

Recall, when we see `println(expr);`, this prints `expr` followed by <u>newline</u> to the screen. This takes input in `$1`. We had to do this in A2P6 and A2P7a.

# Runtime Environment

This is a set of procedures supplied by the compiler (or OS) to assist in execution of programs. 

> For example, MSVCRT.dll, libe.so are available in different compilers/OS’s

We need to make `print` part of your runtime environment - we will link it in:

```bash
wlp4gen < source.wlp4i > source.asm
cs241.linkasm < source.asm > source.merl
linker source.merl print.merl > source.mips
```

Then we can run our executable with

```bash
mips.twoints source.mips # or mips.array
```

> **Notes**: If `$1` is holding something else, we better save it and restore it once we’re done. So, calling print clobbers `$31`. So we need to save it too.  

Thus, `code(println(expr);) = code(expr)`. We aren’t evaluating the `expr`, we are generating Assembly that will evaluate `expr` at runtime.  `$3 <- expr` 

```mips
add $1, $3, $0
sw $31, -4($30)
sub $30, $30, $4
lis $5
.word print
jalr $5
add $30, $30, $4
lw $31, -4($30)
```

## Assignment Statements

`statement->expr1, BECOMES expr2 SEMI`; remember that `expr1` is an `lvalue`. For now, ==assume expr1 is an ID==.

```perl
code(statement) = code(expr2) # $3 <- expr2
# then we need to lookup ID's offset in our symbol table, say offset k
sw ___ k($29)
```

## `if` and `while`

We need boolean tests. The suggested convention for storing the value 1 is to store it in register `$11`. Also, let’s store “print” in register `$10`. 

```perl
	.import print
	lis $4
	.word 4
	lis $10
	.word print
	lis $11
	.word 1
	sub $29, $30, $4 # updating stack frame pointer
# then here we allocate space on our stack for all our variables
# my code
	add $30, $29, $4
	jr $31
```

### Boolean Tests

For our boolean tests, we have that for template `test->expr1 _ expr2`,

For `<`,

```perl
code(test) =
	code(expr1)
	add $5, $3, $0
	code(expr2)
	slt $3, $5, $3
```

For `>`, we swap `expr2` and `expr1` above.

For `!=`, we have

```perl
code(test) =
	code(expr1)
	add $5, $3, $0
	code(expr2)
	slt $6, $3, $5
	slt $7, $5, $3
	add $3, $6, $7
```

For `==`, we treat it as `!(!=)`, so we add `sub $3, $11, $3` to previous.

For `>=, <=` we can do it ourselves.

### IF

`statement->IF test statements1 ELSE statements2`

```perl
code(statement) = code(test)
	beq $3, $0, else
	code(statments1)
	beq $0, $0, endif
else:
	code(statements2)
endif:
```

Equivalently,

```perl
code(statement) = code(test)
	bne $3, $0, true # beq $3, $11, true
	code(statements2)
	beq $0, $0, endif
true: 
	code(statements1)
endif:
```

#### Problems

What if we have multiple if statements? The label names will then overlap, and so we will need to generate unique label names. We’ll just add a numerical value to them to order them. We will keep a counter X for if-statements, and we’ll use `elseX`, `endifX`, `trueX` for label names.

### WHILE

`statement -> WHILE ( test ) { statements }`

```perl
code(statement) = 
loopY:
	code(test)
	beq $3, $0, doneY
	code(statements)
	beq $0, $0, loopY
doneY:
```

and again, we use a counter $Y$ to keep track of the number of while loops to create unique labels. 

## Pointers

We need to now support a number of new things:

1. `NULL`
2. `*` dereferencing
3. `&` address of
4. comparisons
5. arithmetic
6. allocation / deallocation
7. etc

#### NULL

`factor -> NULL`

What should we make `NULL`? We could use `0`, but then we want to be able to catch when we are trying to dereference a null pointer, so we’ll have to add a lot more in since 0 is a valid memory address. 

Instead, we use any address not divisible by 4, say `1`, since addresses are all non-negative and multiples of 4. 

```perl
code(factor) : add $3, $0, $11
```

#### DEREF

`factor1 -> STAR factor2`, with a valid address

```perl
code(factor) : code(factor2) # the memory address of this is stored in $3
	lw $3, $0,($3)
	
```

#### COMPARISONS

same as int

use sltu instead of slt

check if int or int * rune type-of

Better is to add type field to each node of tree

#### Pointer Arithmetic







