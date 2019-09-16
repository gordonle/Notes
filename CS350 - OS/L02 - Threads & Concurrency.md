CS350 L02 | September 10, 2019

# Threads and Concurrency

A ==thread== is a sequence of instructions. A normal ==sequential program== consists of a single thread of execution. Threads provide a way for programmers to express ==concurrency== in a program. In threaded concurrent programs, there are multiple threads of execution, all occurring at the same time. Threads are great because:

- **Resource Utilization**: blocked/waiting threads give up resources (ie. CPU) to others
- **Parallelism**: multiple threads can go simultaneously, improving performance
- **Responsiveness**: dedicated threads to UI, others to loading/long tasks
- **Priority**: can be prioritized to get more or less CPU time
- **Modularization**: can organize the execution of tasks and responsibilities

> Threads can get ***blocked***, meaning they can’t run. This means that the CPU would just remain idle. But with concurrency, we can let it execute a different thread until our first thread gets unblocked.

All threads **share** access to the program’s global variables and heap, but each thread’s stack frames are **private** to that thread; each thread has it’s own stack. Local variables are thus private to each thread as well.

## Thread Functions

To create a new thread, we use `thread_fork`, to terminate a thread we use `thread_exit` and to voluntarily yield CPU time, `thread_yield`. A “join” function is common within threads, but it is not offered by OS/161. ==pthreads== is a sophisticated API library for POSIX threads, it’s well supported and popular. 

==OpenMP== is another library, it’s cross platform and it’s great to use for multi-processing and thread API. ==GPGPU Programming== is general purpose GPU programming APIs that create/run threads on the GPU instead of the CPU.

> **<u>TASK</u>**: Write a thread_forkbomb that adds threads faster than they die.

## MIPS Registers

| num   | name  | Usage                |
| ----- | ----- | -------------------- |
| 0     | z0    | Always zero          |
| 1     | at    | assembler reserved   |
| 2     | v0    | return val/syscall # |
| 3     | v1    | return value         |
| 4-7   | a0-a3 | subroutine args      |
| 8-15  | t0-t7 | temps (caller-save)  |
| 16-23 | s0-s7 | saved (callee-save)  |
| 24-25 | t8-t9 | temps (caller-save)  |
| 26-27 | k0-k1 | kernel temps         |
| 28    | gp    | global pointer       |
| 29    | sp    | stack pointer        |
| 30    | s8/fp | frame pointer        |
| 31    | ra    | return addr (for jr) |

We learned in the past how using MIPS registers work when we’re calling multiple functions, etc. What happens when we have multiple threads?

Only the active thread can be using the CPU’s MIPS registers. Each thread will save their register values on their stack while they are inactive, and then we’ll load them back into the registers once it becomes active. Each thread has its own stack!

The OS will manage the stack sizes for you, so that the thread stacks don’t run into each other. 

With GDB, you can dereference a thread to see all the information inside. Using breakpoints and backtracing, this is how we should be debugging our code.