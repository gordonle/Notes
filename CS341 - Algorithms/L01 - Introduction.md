CS341 L01 | September 04, 2019

# Introduction

==Outline== How to find the best algorithms for various problems

1. How to Design Algorithms
   - General paradigms: greedy, divide-and-conquer, dynamic programming, reductions
   - Basic repertoire of algorithms: sorting, searching, string algs, graph algorithms, linear programming
2. Analysis of Algorithms
   - How good is the algorithm?
     - Time, space, approximation factor, randomization
   - Big O notation: <u>worst</u>/avg cases
   - Model of computation
3. Lower Bounds
   - Model of computation
   - Basic lower bounds
   - **NP-completeness**: seemingly no really fast algorithm
   - **Undecidability**: no algorithm at all

## Case Study: Convex Hall

Given $n$ points in the plane, find their convex hull (the smallest convex set containing them all). 

- Think of it like wrapping an elastic band around all the points. 
- Equivalently, we can find lines $l$ through 2 (or more) points and all other points lie on one side of $l$ 

- **Basic Algorithm**: Try all ${n}\choose{2}$ pairs of points, find line $l$; test all other points and see which side the points are
  - Takes $O(n^3)$
- **Better Algorithms**:
  - B: <u>Jarvis’ March</u>: 
    - From line $l$, find the “next” line. Rotate $l$ through point $s$ to find the next line $l’$ through $s$ an $t$ (find $t$), to find the maximum angle $\alpha$ . Finding the max is then $O(n)$
    - Takes $O(n^2)$, but more accurately $O(n * h)$, where $h$ is the size of the convex hull
  - C: <u>Reduction</u>: 
    - Sort all the points by their x-coordinate, then by y $O(n\log n$)
    - Then find the upper and lower convex halls $O(n)$
    - So overall runtime is $O(n\log n) + O(n) = O(n\log n)$
  - D: <u>Divide and Conquer</u>: 
    - Divide points in half by a vertical line (x-coords)
    - Recurse on each side
    - Combine each the convex hulls into one $O(n)​$
    - $T(n) = 2T(\frac n2) + O(n) = O(n\log n)$

Can we do better than $O(n\log n)$ though? In some sense, no - if we could, then we could sort faster than $O(n\log n)$.

## Final Question

Which is better: $O(n\log n)$ or $O(n*h)$, where $h$ is the size of the convex hull? 

- In worst case, it is clear that $O(n\log n)$ is better. But what if we are given a set of points where the convex hull only had a small number of points (small $h$) and the inside had many (large $n$)? 
- Is there a way to get the best of both worlds? Yes, credits to Prof. Timothy Chan who gave us $O(n\log h)$ 