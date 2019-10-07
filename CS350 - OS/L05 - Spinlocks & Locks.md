CS350 L05 | September 19, 2019

# CTSS

Created by IBM in 1961, it’s a ==compatible time sharing system== from MIT that is backwards compatible with IBM batch processing OS. It’s the first OS to demonstrate the feasibility of time-sharing, and one of the first with text formatting utilities and user messaging (ie ancestor of email). 

It also came with QED, a text editor (precursor to VIM).

# Spinlocks

## ARM Synchronization Instructions

To fix these race conditions, we need to have locking mechanisms around the critical section. We first try to `Acquire` the lock, and if it’s available then we’ll take it. Once we’re done with it, we’ll release the lock. If instead we cannot `Acquire` it, then we’ll wait until it’s available by consistently checking to see if it’s been released yet. 

With ARM based atomic test and set, `LDREX` = Load Exclusive, `STREX` = Store Exclusive. Similar to ARM, in MIPS, theres `ll`(load link) and `sc`(store conditional).

So, a ==spinlock== is a lock that “spins”, repeatedly testing lock availability in a loop until the lock is available. Threads actively use the CPU while they “wait” for the lock. In OS/161, spinlocks are already defined.

```
struct spinlock {
	volatile spinlock_data_t lk_lock;
	struct cpu *lk_holder;
};

void spinlock_init(struct spinlock *lk);
void spinlock_acquire(struct spinlock *lk);
void spinlock_release(struct spinlock *lk);
```

Spinlocks should only be used to protect the **smallest** of critical sections. Spinlocks disable interrupts! So while you are acquiring a lock, that specific CPU will not be able to perform a context switch due to preemption. This means we shouldn’t run it for long. Essentially, while you own a spinlock, you are the only thread that can run on that CPU. So you’re effectively the owner of that entire CPU. This, the owner of a spinlock is a CPU. 

# Locks

Like spinlocks, ==locks== are used to enfore mutual exclusion. Where spinlocks *spin*, locks ***block***. A thread that calls `spinlock.acquire` spins until the lock can be acquired. But when it calls `lock.acquire`, the thread sleeps until the lock can be aquire. For ASST1, we want to implement locks that BLOCK, not SPIN. 

## Thread Blocking

Sometimes a thread needs to wait for something, and when it blocks, it stops running. The scheduler then chooses a new thread to ru, then a context switch from the blocking thread to the new thread occurs. The blocking thread is queued in a ==wait queue== (not on the READY list). Eventually, this blocked thread is reenabled and woken up by aother thread. 

Locks are owned by a thread. 

