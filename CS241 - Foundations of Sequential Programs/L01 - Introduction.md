# Lecture 1: Introduction

> January 8th, 2019

---

## Binary

The binary system consists of bits, defined as `0`s and `1`s, and it’s the only unit that a computer understands.

> This is hard for us to understand, so we’ve developed higher-level programming languages like `C` and `JavaScript` to allow us to more easily issue commands.

We group bits into sequences of 8, known as a **byte**. For $n$ bytes, there are $8n$ bits and so $2^{8n}$ different sequences. 

A **word** is the machine-specific grouping of bits: most computers nowadays use 32-bit or 64-bit words. In this course, we will be using a 32-bit computing machine. In the real world, 64-bit is commonplace. 

**<u>Fun Fact:</u>** 4 bits is known as a **nibble**!

> Q: Given a byte (or a word) in RAM, what does it mean?
>
> A: There could be many different meanings - so we need to know the context. 

### Numbers

Given a binary number,`11001001` refers to $128 + 64 + 8 + 1 = 201$  in decimal

Given a decimal number, 201, we subtract the highest power of 2 and continue until we reach 0.

​	$201 - 2^7 = 73$, $73 - 2^6 = 9$, $9-2^3 = 1$, $1 - 2^0 = 0$, so 201 = `11001001`.

What about negative numbers? We could make the first bit a “sign” bit, often called **sign-magnitude**.

| Bit  | Sign |
| ---- | ---- |
| `0`  | `+`  |
| `1`  | `-`  |

This is wasteful, since we have two representations for 0! (+0 and -0). It also introduces ambiguity when the reader does not know if we are using sign-magnitude or not. Instead, we use **2s-compliment**.

#### Two’s-compliment

1. Interpret the $n$-bit number as an unsigned integer
2. Read the leftmost bit,
   1. If it’s `0`, done
   2. Else, subtract $2^n$

For example, for $n=3$,

| 000  | 001  | 010  | 011  | 100       | 101       | 110      | 111      |
| ---- | ---- | ---- | ---- | --------- | --------- | -------- | -------- |
| 0    | 1    | 2    | 3    | $4-8 =-4$ | $5-8 =-3$ | $6-8=-2$ | $7-8=-1$ |

Note the cyclic nature of this.

##### Alternative Method

==+==: Numbers are “normal” binary magnitude

`-`: Take the magnitude of the binary number, flip the bits, then add 1.

To convert from a negative decimal number, you can do the same process but forwards (ie. flip bits, add 1), due to the cyclic nature of this.

> ex. $-73$
>
> | Magnitude   $\rightarrow$ | Flipped Bits   $\rightarrow$ | Add 1    |
> | ------------------------- | ---------------------------- | -------- |
> | 01001001                  | 10110110                     | 10110111 |
>
> ex. 11001001
>
> First bit is 1, so it’s negative!
>
> | Flipped Bits | Add 1    | Magnitude |
> | ------------ | -------- | --------- |
> | 00110110     | 00110111 | 55        |
>
> And so $11001001 = -55$

#### Hexadecimal Numbers

We represent 4 bits of binary with 1 digit in base 16. Since we only have 10 digits from 0-9, we represent the other 6 with $A, B, C, D, E, F$

>ex. Converting Hexadecimal to Decimal
>
>$00110111 \rightarrow 0011,0111 \rightarrow 3, 7 \rightarrow (16^1 * 3) + (16^0 * 7) = 55$ (decimal).

“0x” means that the number is in hexadecimal.

> Q: Given a byte 11001001, how can we tell if it’s unsigned, sign-magnitude, or 2s-compliment?
>
> A: We can’t. 

### Characters

ASCII ~ 7bits