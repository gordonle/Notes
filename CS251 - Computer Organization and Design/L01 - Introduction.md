# Lecture 1: Introduction to MIPS

> January 8th, 2019

---

## MIPS

MIPS stands for “Microprocessor without Interlocked Pipelined Stages”. It has an RISC architecture (Reduced Instruction Set). It has 3 formats when issuing commands. To hold our data, we keep them in containers known as **registers**.

### Registers

A register is a portion of memory that is quick to access and store memory. Each register has a defined width, and this width defines how many bits it can hold inside. The 0th register (`$0`)will always contain only 0s. This allows us to perform special functions, such as setting constants.

In MIPS, we have **32 registers** (`$0` to `$31`), each with a width of 32. This is a **design choice**, we could have any arbitrary number of registers. 

### Datapaths

We separate the memory on our system into different sections: the **instruction memory**, the **data memory** and the **register file**.

### 1. R-Format

The R-Format contains basic operations such as addition, subtraction, logical comparison operators, etc. 

For example, `add $3, $2, $1` adds the values stored in registers `$2` and `$1`, and stores the result in `$3`. This is done by calling the **Arithmetic Logic Unit** which then performs the operation.

Let’s compare some `C` code,

```c
f = (g + h) - (i + j);
```

with the same code written in `MIPS`,

```mips
add $r6, $r2, $r3
add $r7, $r4, $r5
sub $r1, $r6, $r7
// missing step here
```

In order to manipulate any values, they must first be loaded into a register. These are all R-Format Instructions, as you can see the formatting includes two source registers and one destination.

Each instruction takes up 4 bytes, and a **program counter** (PC) in the instruction memory keeps track of which instruction we currently are at.

### 2. I-Format

`$addi $1, $2, 100` is calling the *add immediate* function, that adds the immediate value of $100$ to contents of `$2`, and stores it in `$1`.

### 3.J-Format

`j 3`

Used for unconditional

When a jump is executed, PC set to four times immediate argument. The address that we are jumping to is called the *Jump Target Address* (JTA). The Jump offset/immediate is actually saying: “*jump to instruction number $X$*”. 

To obtain the address for this instruction, you must multiply the number by 4. The hardware will do this multiplication, so we don’t need to worry about it.

Let’s examine the following code:

```php
Address 0: j 3
Address 4: add $1, $2, $3
Address 8: sub $1, $3, $5
Address 12: addi $2, $12, 16
```

This code will hit line 1, then jump to address $3*4=12​$.

