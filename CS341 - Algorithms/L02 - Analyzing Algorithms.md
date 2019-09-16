CS341 L01 | September 09, 2019

# Analyzing Algorithms

An ==algorithm== is a finite answer to an infinite question. The problems we are focusing on must specify its **infinite set of inputs**, as well as its corresponding **outputs**. From Alan Turing, an algorithm is a well-defined computational procedure to go from any input to its corresponding output. For our purposes, we’ll be giving it in pseudocode.

We will analyze algorithms by measuring the time & space taken as a function of the input size $n$. We’ll do this by an abstract <u>model of computing</u>. 

## Models Of Computing

We want to be able to specify the elementary steps needed to built our algorithms. Once this is done, we want to specify the measures of time, space (memory used) and input size per step. Our goal is to “reflect but simplify reality”. We’ll divide our models into *general purpose* and *special purpose* (ie. for proving lower bounds of sorting).

### General Purpose

These models assume that our machines can do everything real computers can.

#### I. Pseudocode

Let’s look at some of the characteristics of pseudocode.

- each line is 1 step - careful of:
  - initializing arrays should cost the length of the array
  - large numbers (ie. Fibonacci Sequence should be $O(n)$, but if you run it you’ll overflow very fast)
- count the cost in bits
  - a * b, size = # of bits of a = $\log a$, or more precisely $\lceil \log a\rceil + 1$ . So it’ll take $(O(\log a)(\log b))$ bit operations. Later in the course, we’ll be able to get $(O(\log a)(\log b))^{0.59}$ with divide and conquer algs

#### II. RAM - Random Access Machine

This is a more formal model. When using a tape to write down the memory, we must pay to walk along the tape until we reach the memory address we’re looking for. Here, “random access” means that we can access any memory location instantly (in $O(1)$). 

So how do we charge for size of word? Memory location.

- unit cost (assume each line is $O(1)$) - this is too greedy of an assumption
- bit cost  - this is too weak of an assumption

So a good compromise is to consider **word RAM**: the number of bits is a word is $\Theta(\log n)= $ constant $\cdot \log n$, where $n$ is the input size. This is slightly weird, as the model will change as the input grows, but it’s very natural. For example, consider an array [1..$n$]. Index $i\in[1..n]$ should fit in one word, so $\log n$ bits. 

Our model will use word RAM = pseudocode, but take care for powerful instructions like those mentioned above.

==Note==: Sorting $n$ integers can be achieved in $O(\log(\log n))$ with this model, but it’s outside the scope of this course.

#### III. Other General Purpose Models

**Circuit model**: models hardware circuits

**Turing Machine**: models human computation

### Special Purpose

Comparison Models - $\Omega(n\log n)$, Arithmetic models

## Running Time of Algorithms

$T_A(I)$ is the running time of algorithm $A$ on input $I$. So how fast can we sort the possible times for each input? When each input has only one runtime, we use the <u>worst-case</u> runtime: $T_A(n) = max\{T_A(I): \text{input $I$ of size $n$}\}$. 

Why do we always use the worst case?

1. We want a guarantee
2. Average case is hard to analyze and it depends on the input distribution

## Asymptotic Analysis of Algorithms

We want $T(n)$ to be *simple to express* and *machine independent* (one machine might be faster than another). By ignoring constant factors, this also implies that we are *ignoring lower order terms*.

==Big Oh Notation==: Let’s consider functions $f(n)$ and $g(n)$ from $\N$ to $\R^{\ge0}$.

- $f(n)$ is $O(g(n))$ if $\exists$ constants $c>0$ and $n_0$ such that $f(n) \le c\cdot g(n)$ if $n \ge n_0$.
  - $T(n) = 5n^2+3n+25 \in O(n^2)$
  - $10^{100}n\in O(n)$
  - $\log n \in O(n)$ but $n \notin O(\log n)$
  - $2^{n+1} \in O(2^n)$
  - $(n+1)! \notin O(n!)$

Trick Question: If alg $A$ has runtime $O(n^2)$ and alg $B$ has runtime $O(n\log n)$, which is better?

Answer: We don’t know! We need $\Theta$ for this. 

# Problems

1. Find the smallest Fibonacci number that overflows a 32 bit word

   ==Answer==: $n=47$. Think of the Fib number that’s greater than $2^{32}-1$. 

2. Show how to sort $n$ numbers in $O(n)$ on unit cost RAM using + , * , - , bit-shift (Hint: do all $n^2$ comparisons of pairs of numbers in 1 subtraction)

   Think about having your numbers in binary, and make one big number. 