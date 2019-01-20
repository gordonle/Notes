thank you https://github.com/alexieyizhe for the notes :heart: 

# MIPS Architecture Model

Every CPU has its own machine language. The process that the code you write in a programming language like `C` or `C++`undergoes in order for the CPU to be able to understand it is as follows:

1. **High Level Language Code**: code that we write.

   ==**Compiler**==

2. **Assembly Language Program**

   ==**Assembler**==

3. **Machine Language Program**: 1s and 0s that the CPU can understand.

   ==**Loader**==: places it into CPU and Memory

4. **CPU & Memory**: executes the program.

Computer programs operate on data, but *are* data themselves. We can't differentiate between whether a memory location contains *machine instructions* or *data,* since everything is just binary (sequences of 1s and 0s that map to certain instructions or data).

[![image-20190110100455891](https://github.com/alexieyizhe/uni-notes/raw/master/2B/CS%20241/Notes/assets/image-20190110100455891-7132695.png)](https://github.com/alexieyizhe/uni-notes/blob/master/2B/CS%20241/Notes/assets/image-20190110100455891-7132695.png)

We will work with **MIPS**, an architecture that consists of the following:

- **Central Processing Unit (CPU):** the "brains" of the model, consisting of:

  - **Control Unit:** decodes the machine instructions and dispatches orders to other parts of computer to carry out instructions

  - **Arithmetic/Logic Unit:** does math things

  - **Memory:** many kinds:

    - CPU cache: registers, L1, L2, L3 `tiny` ==very fast==
    - RAM: the main memory `moderate` ==fast==
    - Disk: HD, SSD `large` ==slower==
    - Network

  - **Registers**: a small amount of very fast memory

    - 32 general purpose registers with a size of 32 bits each (one word) in the 32-bit MIPS model we're using

    - CPU can only operate on data that is stored in registers

    - Denoted with `$n` where `n` is the $n$^th^ register.

      - `$0` is always 0s
      - `$31` is also special
      - others might be special

    - Each register operation will specify registers it operates on, and it takes 5 bits to represent a register number (5 digits in binary to represent a register number)

    - An **op code** determines which operation we are executing

  - **Memory Address Register (MAR)** stores a single desired word's memory address in RAM so that the Control Unit can reference it when fetching data from the RAM

  - **Memory Data Register (MDR)** stores the data fetched from the RAM at the address specified in the MAR, and the Control Unit moves it to the memory register specified with `load`

  - **Program Counter (PC)**: holds the address of the next instruction to execute

    - By convention, we guarantee that a specific address (*ex. address 0*) contains code so that an initial value can be provided to the PC

    - Computer runs a **Fetch-Execute Cycle**: loads instruction at address of PC into IR and execute it, repeat

      ```
      PC <- 0
      loop
      	IR <- MEM[PC]
      	PC <- PC + 4
      	decode and execute instr in IR
      end loop
      ```

      This means that the PC will hold the address of the next instruction when the current instruction is being executed since it's incremented first before the instruction in IR is decoded and executed.

    - The ==Loader== (see above) puts the program into RAM and sets the PC to the address of the 1^st^ instruction in the program.

      When the program terminates, the PC is set back to the next instruction of the ==Loader== and it is responsible for loading another program. Register 32 (`$31`) holds the address of the next instruction of the ==Loader==, so we set the PC to the contents of `$31`.

      ⚠️ **Make sure that you are careful when you manipulate $31 or recurse; make sure to always save the previous value of PC somewhere!**

- **Random Access Memory (RAM)**: A large amount of memory separate from the CPU

  - Data travels between RAM and CPU on the **bus**: it must reach the CPU to be used

    - Interact with RAM with two instructions:

      `load`: transfer a word from a memory address in RAM specified by MAR to toe MDR and then to a specified register in the CPU

      `store`: stores a word in the MDR into a location in memory specified by MAR (reverse of `load`)

  - Each cell of memory has an address

  - Each n^th^ 4-byte block with addresses ${4n, 4n+1, ..., 4n+3}$ is a word, so words have addresses 0, 4, 8, etc

  - RAM access is much slower than registers