CS350 L04 | September 17, 2019

# MCP

This is the first OS to be written entirely in a higher level language, and that supported multi-tasking/threaded. It had a journal file system, high-level job controls and provided source code to users, so that they could submit their own patches. 

# Thread stack after preemption

```
** stack grows DOWNWARDS **

----------------------
|        ..
|  other stack frames 
|        ..
|---------------------  -> timer interrupt!
|      trap frame
|---------------------
|  interrupt handler
|    stack frame(s)
|---------------------
|    thread_yield
|---------------------
|    thread_switch
|---------------------
|     switchframe
|
```

==Note==: Immediately after a timer interrupt, we’ll throw a `trap frame` onto the stack. 

# Synchronization

All threads in a concurrent program **share access** to the program’s global variables and the heap. The part of the program that is being shared is called the ==critical section==.

A ==race condition== is when the program result depends on the order of execution. Race conditions occur when multiple threads are reading and writing the same memory at the same time.

