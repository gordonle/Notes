C241 L05 | January 22, 2019

# Procedures

```ruby
main: ...
	; save $31
	; update top of stack, decrement $30		# ^ CALLER-SAVE
	; load addr of procedure
	; jump to procedure using jalr, overwriting $31
# proc returns here #
	; increment $30
	; restore $31
jr $31
procedure:
	; push registers that procedure will use onto stack
	; decrement $30			# ^ CALLER-SAVE
	; body of procedure
	; increment $30
	; restore registers off at stack
	jr $31
```

# Assembler

The ==input== will be assembly code, and the ==output== will be machine code. For every line of assembly code, we get one line of machine code. This translation has two phases:

1. Analysis: understand the meaning of source string
2. Synthesis: output the equivalent machine code

The **Assembly File** is a stream of characters. We group characters into meaningful ==tokens==, for example labels, hex #s, reg #s, .word, etc. We have tools for this. `asm.rkt` and `asm.cc`. Our assembler now gets a sequence of tokens.

Our job is to:

1. Group tokens into instructions.
2. Output corresponding machine code

Focus on finding correct sequences. Anything else is an error, and we send it to `std::err`.

## The Big Problem

```ruby
beq $0, $1, abc		# we dont know the value of this label yet
...
abc:
```

The standard solution would be to pass through the entire program, and find all the labels and their memory addresses. During this 1st pass, we should:

- group tokens into instructions (ie. `add` should be followed by 3 registers)
- record address of all labelled instructions
  - this is where we build our “**symbol table**”, a list of (label, address) pairs.

**Note**: a line of assembly may have multiple labels

```ruby
f:
g: mult $1, $2		# both labels here have the same memory address as the instruction
```

During the 2nd pass:

- translate each instruction into machine code
- lookup labels in our symbol table when needed

The assembler now outputs assembled MIPS to `std::out`. We can also output the symbol table to `std::err`. For example,

```ruby
									# MEMORY ADDRESS
main:		lis $2					# 0
			.word 13				# 4
			add $3, $0, $0			# 8
top:		add $3, $3, $2			# C
			lis $1					# 10
			.word -1				# 14
			add $2, $2, $1			# 18
			bne $2, $0, top			# 1C
			jr $31					# 20
			; comments
beyond:
```

Pass 1: Group tokens into instructions, and build a symbol table with a map. For the above code,

| Label  | Address | Symbol Table   |
| ------ | ------- | -------------- |
| main   | 0x0     | (main, 0x0)    |
| top    | 0xC     | (top, 0xC)     |
| beyond | 0x24    | (beyond, 0x24) |

Pass 2: Translate each instruction

| Instruction                                                  | Hex        |
| ------------------------------------------------------------ | ---------- |
| `lis $2`                                                     | 0x00001014 |
| `.word 13`                                                   | 0x0000000d |
| `bne $2, $0, top` <br />we have to look up top to be (0xC), then we calculate<br />$\frac{(\text{0xC - 0x20})}{4} = -5$<br />-5 has a binary magnitude of 0000 0000 0000 0101<br />flipped bits and add 1: 1111 1111 1111 1011<br />in hex: f f f b | 0x1440fffb |

In a 32-bit instruction, we have (in order)

| 6 bits                                                   | 5 bits     | 5 bits     | 16 bits     |
| -------------------------------------------------------- | ---------- | ---------- | ----------- |
| opcode                                                   | register s | register t | offset i    |
| `bne` = 000101<br />(this really represents 0001010...0) | $2 = 00010 | $0 = 00000 | -5 = 0xfffb |

To put 000101 into the first 6 bits we need to append 26 zeros by **left-shifting** by 26 bits.

```cpp
Racket: (arithmetic-shift 5 -26)
C++: 5 << 26

// Move $2, 21 bits to the left
2 << 21
=> 00010...0 (21 trailing 0s)

// Move $0, 16 bits to the left
0 << 16
=> 00000...0 (16 trailing 0s)

// Move -5 = 0xfffffffb, we only want the last 16 bits (fffb)
//  so use bitwise AND with 0x0000ffff
// bitwise AND = singular '&'
Racket: (bitwise-and -5 #xffff)
C++: (-5 & 0xffff)

// Put it all together bitwise OR all pieces
(5 << 26) | (2 << 21) | (0 << 16) | (-5 & 0xffff)

// Binary Output:
// So assembled instruction has numerical value: 339804155(base 10).
cout << 339804155;
// NO! We want to print out the 32 bits, but we are printing the 9 bytes of ASCII codes

// ie:
char c = 65;
int x = 65;
cout << x << c;
=> prints out "65A";
```

To send “raw” bytes to `std::out`, we print as chars. `00010100 01000000 fffb`What ASCII character represents each byte?

```c++
int instr = 339804155;
/*
-----------------
| x |   |   |   |  int
-----------------
  |---------->|
            -----
            | x | char
            -----
*/
char c = instr >> 24;
cout << c;
c = instr >> 16;
cout << c;
c = instr >> 8;
cout << c;
c = instr;
cout << c;
```

