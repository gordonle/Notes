CS241 L04 | January 17, 2019

# Implementing Procedures in MIPS

1. Call and Return:
   - How do we transfer control in and out of a procedure?
   - What if your procedure calls another procedure?
   - How do we pass parameters?
2. Registers
   - What if a procedure we call overwrites a register we are using?

```ruby
RAM DIAGRAM
-----------------
| Your Program  |
|               |
-----------------
|     FREE      |
|      RAM      |
----------------- <- $30 points here
```

> In MIPS, register `$30` is initialized by loader to store memory address just passed the last word of memory given to your program. We can thus use `$30` a s a “bookmark” if we allocate from the bottom.

RAM used in LIFO (aka a stack). `$30` is a stack pointer that contains the address to the top of the stack.

```text
# main calls f, f calls g, g calls h
On the stack, this looks like:
-----------------
|  YOUR PROGRAM |
-----------------
|               | // EVERYTHING HERE AND BELOW IS FREE RAM
----------------- <- $30 ends up here
|       h       |
-----------------
|     g         |
-----------------
|   f           |
-----------------
|main           |
----------------- <- $30 starts here
```

**Strategy**: each procedure stores in RAM the initial value of registers that it will overwrite, which protects the data from the procedure it was called from. Then it will restore the original values on return.

## Call and Return

**Template**: 

```ruby
f:
sw $2, -4($30) 	# our procedure is going to use $2 and $3,
sw $3, -8($30) 	#  so we want to save their initial values
lis $2 			# since we already saved the value of $2
.word -8
add $30, $30, $2 # updates top of stack pointer
jr (body of your procedure)
lw $2, -4($30)	# restores values of saved registers
lw $3, -8($30)
```

Do we return `jr $31` ?

```ruby
# call
main:
	lis $5
    .word f
    # when f completes we want to jump back to here
    # instead of jr, we use "jalr" = jump and link register, saves current PC into $31
    jalr $5
        
f: ..... # since jalr overwrites $31, we need to save and restore the values in $31 
   ..... #  before we jump to f
   
```

To return, we need to set the PC to the line after `jr`/`jalr` from where the procedure was called. Using `jalr` sets the value of `$31` to the address of the next instruction, overwriting it, so we need to save `$31` on the stack then restore it when the call returns.

```ruby
main:
	lis $5
    .word f
    sw $31, -4($30)
    lis $31
    .word -4
    add $30, $30, $31
    jalr $5 # calls f, overwrites $31
    lis $31
    .word 4
    add $30, $30, $31
    lw $31, -4($30)
    jr $31 # return to loader
    .....
        
f:
	... # push the registers that f will use on the stack
    ... # decrement $30
    ... # body of f
    ... # increment $30
    ... # pop registers off the stack
    jr $31 # return to caller
```

## Parameters and Result Passing

In general, use registers and document what you’re saving where. If there are too many parameters, you can push hem onto the stack.

> **Ex**: Write a procedure to sum 1 to N
>
> ```ruby
> # Documentation:
> # sum1ToN: adds the numbers 1...N
> 
> # Registers:
> # $1 - working				; save
> # $2 - input (value of N)	; save (just to be safe if caller wants it)
> # $3 - output				; don't save
> 
> sum1toN:	sw $1, -4($30)	# Saving $1 and $2
> 			sw $2, -8($30)
> 	    	lis $1			# Updating stack pointer
> 			.word -8
> 			add $30, $30, $1
> 			add $3, $0, $0	# Body of sum1ToN
> 			lis $1
> 			.word -1
> topOfLoop:	add $3, $2, $3
> 			add $2, $2, $1
> 			bne $2, $0, topOfLoop
> 			lis $1			# Restore registers and update $30
> 			.word 8
> 			add $30, $30, $1
> 			lw $1, -4($30)	# Popping registers saved off stack
> 			lw $2, -8($30)
> 			jr $31			# Return call
> ```
>
> There is a **difference** between program and procedure. 

## Recursion

If we manage saving and restoring registers, etc. recursion just works.

## I/O

- Output: `sw to 0xffff000c`. 
  - This will print the least significant byte.
- Input: `lw from 0xffff0004`
  - next character from stdin will be the lease significant byte

> **Ex:** Print “CS\n”
>
> ```ruby
> lis $1
> .word 0xffff000c
> lis $2
> .word 67 # ascii for C
> sw $2, 0($1)
> lis $2
> .word 83 # ascii for S
> sw $2, 0($1)
> lis $2
> .word 10
> sw $2, 0($1) # ascii for \n
> jr $31
> ```
>
>