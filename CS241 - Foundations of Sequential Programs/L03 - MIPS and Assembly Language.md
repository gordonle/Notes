Lecture 3 | January 15, 2019

# MIPS Instruction Formats

> **Ex.1** Add the value in register 5 to the value in register 7 and store the result in register 3, then return.

```ruby
add $3, $5, $7
jr $31
```

| `add d, s, t`    | 0000 00ss ssst | tttt | dddd d000 0010 000  |
| ---------------- | -------------- | ---- | ------------------- |
| Binary           | 000 0000 1010  | 0111 | 0001 1000 0010 0000 |
| Hexadecimal (0x) | 0 0 A          | 7    | 1 8 2 0             |

| `jr s`           | 0000 00ss sss0 | 0000... 1000 |
| ---------------- | -------------- | ------------ |
| Binary           | 0000 0011 1110 | 0000....     |
| Hexadecimal (0x) | 0 3 E          | 0 0 0 0 8    |

> **Ex.2** Add 42 to 52, store sum in $3 and return

```ruby
lis $d
```

What this does is “Load immediate and skip”. It treats the next word as an **immediate value** and loads it into `$d`. Then, it skips to the following instruction `pc += 4`. Immediate values are probably not instructions.

```ruby
0: lis $5
4: .word 42 # go and write 42 in 2s-compliment and store it in $5
8: lis $7
C: .word 52
10: add $3, $5, $7
14: jr $31
```

## Assembly Language

Here, we can replace `1`s and `0`s with English-like instructions. There’s less chance of error, and the translation to binary can be automated with the **assembler**. 

> **Ex.3** Compute the absolute value of $1, store in \$1 and return.

Let’s take a look at the “Branch on Equal” command:

```ruby
beq $s, $t, i # branch if two registers have equal contents (same bits in same order)
```

Then we’ll increment the program counter by a given # of words. Remember, we can branch backwards! We can also “Branch on Not Equal”, and “Set Less Than” `slt`:

```ruby
0: slt $2, $1, $0 	# checks if $1 < 0. If true, store 1 in $2. Otherwise store 0.
4: beq $2, $0, 1	# this checks if it's positive, and if it is pc jumps 4*1
8: sub $1, $0, $1 	# if negative, it will compute 0 - $1 and store it back in $1
C: jr $31
```

Note that we jump our program counter by $4*1$ since it’s already on then next command.

> **Ex.4** Looping: sum the integers 1...13 and store it in $3, then return

Initially, this is how we would approach it.

```ruby
0: lis $2
4: .word 13
8: add $3, $0, $0
C: add $3, $3, $2 # loop starts here
10: lis $1	# we gotta load -1 in since we need to decrement 13
14: .word -1
18: add $2, $2, $1
1C: bne $2, $0, -5 
20: jr $31
```

This loop makes us load -1 in every loop! So refactored,

```ruby
0: lis $2
4: .word 13
8: add $3, $0, $0
C: lis $1
10: .word -1
14: add $3, $3, $2 # loop starts here
18: add $2, $2, $1
1C: bne $2, $0, -3 # loop ends here
20: jr $31
```

**Note:** Remember to update offsets if you (re)move code around! But this will become tedious with a larger code base.

### Labelled Instructions

The assembler provides us with **labelled instructions** so that we don’t have to manually update the offsets.

```ruby
foo: 14 add $3, $3, $2
	...
    ...
	 1C bne $2, $0, foo
	 20 jr $31
```

`foo` is the memory address of the next instruction. Here, it has `0x14`. The assembler will then compute 
$$
\begin{align} \frac {foo - PC} {4} &= \frac {14 - 20} {4} \\ &= -3 \end{align}
$$
Recall this is in base 16!

## RAM

“Load Word” loads a word from RAM into a register.

```ruby
lw $a, i($b) # loads word at MEM[$b + i] into $a 
```

“Store Word” stores word from register to RAM

```ruby
sw $a, i($b) # stores what's in $a into MEM[$b + i]
```

> **Ex.** \$1 is the address of an array, \$2 is the number of elements in the array. Place element at index 5 into \$3

In general,

```ruby
0: lis $5
4: .word 5
8: lis $4
C: .word 4
10: mult $5, $4 # the results are stored in the hi:lo registers, since its got 64 bits
14: mflo $5
18: add $5, $5, $1
1C: lw $3, 0($5)
20: jr $31
```

Above, we multiplied 5 by 4 with the command `mult`. The product of two 32-bit integers is 64 bits, which is too big to fit in a single register. Thus we use the two special registers given to us, `hi:lo`. We will only be accessing the `lo` register in the scope of this course, since our numbers wont be that large.

**Note**: In division, `lo` stores the quotient, `hi` stores the remainder!

In this case, we could actually do this in one command!

```ruby
lw $3, 20($1)
jr $31
```

