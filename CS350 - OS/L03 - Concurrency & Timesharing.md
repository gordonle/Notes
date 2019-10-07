CS350 L03 | September 12, 2019

Remember, a thread is just a sequence of instructions. Concurrency is giving the illusion of multiple threads running at the same time. `thread_yield` does not guarantee that your thread will stop. If there are no other threads of equal or greater priority, then your thread will not yield and it will continue to run. 

# Implementing Concurrent Threads

1. **Hardware support**: With $P$ processors, $C$ cores, an $M$ multithreading per core, we get $PCM$ threads that can execute <u>*simultaneously*</u>.
2. **Timesharing**: Multiple threads take turns on the same hardware; rapidly switching between threads so that all can make progress (<u>*not actually simultaneous*</u>, but rapid switches gives this illusion).
3. **Hardware + Timesharing**: $PCM$ threads running simultaneously with timesharing. 

## Timesharing

When timesharing, the <u>switch</u> from one thread to another is called a ==context switch==. During this, there are 3 steps:

1. decide which thread will run next (==scheduling==)
2. save register contents of current thread
3. load register contents of next thread

We have to balance the time taken between context switches, since if it’s too short, then the time taken to save and load the registers will take too much time and no code can run. Too long, then the timesharing isn’t really that efficient (not simultaneous). 

> Look at `kern/thread/thread.c` to see how thread switching (`thread_switch`) works.

What actually causes context switches? There are a few cases when that causes this. When the running thread...

- calls `thread_exit` and terminates
- preemption (timesharing)
- calls `thread_yield` and voluntarily gives up CPU time
- *blocks*, meaning it’s put to sleep until another particular thread is finished

The limit imposed on the amount of CPU time allotted per thread is called the ==scheduling quantum==. The quantum is an ***upper bound*** on how long a thread can run before it must yield the CPU. What if a running thread never yields, blocks, or terminates when the quantum runs out?

==Preemption== forces a running thread to stop running, accomplished using ==interrupts==. That’s an event that occurs during the execution of a program, caused by timers, disk controllers, network interfaces, etc. When an interrupt occurs, the hardware automatically will transfer control to a fixed location in memory. There we can find our ==interrupt handler==, placed there by our thread library. This handler creates a ==trap frame== that **<u>saves every register</u>** at the time of the interrupt. It then determines which decide caused the interrupt and performs device-specific processing. It then loads the thread context from the trap frame and resumes execution of the original thread.

While in interrupt handlers, we disable all other interrupts to avoid performance issues and other problems.

### Preemption

A preemptive scheduler uses the scheduling quantum to impose a time limit on running threads. There’s a clock that periodically causes interrupts. Once the clock goes off, the interrupt handler realizes it’s the clock that called it, and then scheduling quantum can be evaluated. If a thread’s quantum has expired, the clock will call `thread_switch` on behalf of the thread for it, starting the context switch. 

## Thread States

There are 3 states that a thread can be in:

- Ready: Threads that are ready to start executing on the CPU
- Running: Currently executing code on the CPU
- Blocked: Threads that are waiting for something to happen

The transitions between states is limited and restricted. When in the **ready** state, threads can be dispatched to the **running** state, nowhere else. If the thread is **running**, the thread can return to the **ready** state by preemption or by thread yielding. It can also go to the **blocked** state if the resource we want is available. Once in the **blocked** stage, the only way to execute is for the resource to become available, or `wake_all`/`wake_one` is called, then the thread will return to the **ready** stage. Once a thread is **running** and completes, it terminates. 

### `thread_yield`

The program calls `thread_yield`, which then calls `thread_switch` to kick off the context switch. `thread_switch` will then pick a new thread to execute, and calls `switchframe_switch` to perform the low-level context switch.



# EXEC 1 - OS

It’s a *batch processor* with *multiprogramming*. It automatically loads the next job upon completion of another.

