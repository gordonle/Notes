

CS341 L04 | September 16, 2019

# Algorithmic Paradigms

## II. Divide and Conquer, Solving Recurrences

Some examples include `merge-sort` and `binary-search`. There are three main steps to this:

1. Divide: break the problem into subproblems
2. Recurse: to solve these subproblems
3. Conquer: combine these solutions

> Ex. Counting inversions. This can be used when comparing people’s preferences (music, movies, ...), you get people to *rank* a set and then you *compare* these rankings.

|          | best |      |      | worst |
| -------- | ---- | ---- | ---- | ----- |
| I like   | 1    | 2    | 3    | 4     |
| You like | 4    | 2    | 1    | 3     |

Looking at the second row (you like), we can see that:

- **In Order Pairs**: (1,3), (2,3)
- **Out-of-order Pairs**: (4,2), (2,1), (2,3), (4,1), (4,3). 5 pairs!

How do we get these numbers in order then?

<u>Algorithm 1</u>: Naive Approach. Try all pairs of indices, $i, j$, which will take $\Theta(n^2)$.

<u>Algorithm 2</u>: Divide & Conquer. Given a list of $a_1,...,a_n$, our goal is to count the # of inversions. To do so,

- divide the list in two $m = \lceil\frac n2\rceil$

  $A = a_1,...,a_m,\: B = a_m+1, ...,a_n$. We stop this process once each array has only one item

- recursively count the # of inversions in each of A and B ($r_A, r_B$)

- then the answer is $= r_a + r_b + r$, where $r = $ the number of pairs $a_i \in A, a_j \in B : a_i > a_j$. We can use $r=\Sigma_{a_j\in B} r_j$, where $r_j = $ of elements in $A$ larger than $a_j$.

We’ll use the internal logic of `merge-sort`. We’ll sort $A, B$, then we need to find the first element in sorted $A$ that is less than $a_j$. Then we’ll know that the number of elements after and including that index will be less than $a_j$, or equivalently, is $r_j$. 

```
sort-and-count: (will return the sorted list L, and the # of inversions)
	divide L into A, B (first half, second half)
	A = (A, r_a) <- sort-and-count(A), which returns the sorted list A and its # of inversions
	B = (B, r_b) <- sort-and-count(B)
	r = 0
	do merge A & B
		when an element is moved from B to output, r = r + # elements remaining in A
	return (merged list, r_a + r_b + r)
```

To analyze the runtime, $T(n) = T(\lfloor\frac n2\rfloor) + T(\lceil\frac n2\rceil) + O(n)$. As for merge sort, the solution is $O(n\log n)$. 

## Solving Recurrence Relations

There are 3 basic approaches to solving recurrence relations:

1. recursion tree method
2. guess a solution and prove it by induction
3. Master Theorem

### I. Recursion Tree

Let’s analyze how this would work with `merge-sort`. $T(n) \ 2T(\frac n2) + c\cdot n$, where $T(1) = 0$ (count # comparisons). In this method, we often make the assumption that $n$ is a power of 2 to avoid floors and ceilings. Most numbers aren’t powers of 2, so we need to explain why this still applies with such a strong assumption. This is due to the fact that <u> $T$ is non-decreasing.</u> $T(15)$ will always take less or equal time when compared to $T(16)$. If we have a list and we want to increase it to a power of 2, at worst we have to *double* the length of our list. 

We can draw the tree out, and for each level the number of elements in $T$ will be cut down to half. There will be $\log n$ levels, each of which sum to $c\cdot n$ operations. So thus the total runtime is then $c\cdot n\log n$. 

When $n$ is not a power of 2, $T(n) = T(\lfloor\frac n2\rfloor) + T(\lceil\frac n2\rceil) + c\cdot n$. Here, the solution is
$$
\begin{align}
	T(n) = n\lceil\log n\rceil - 2^{\lceil\log n\rceil} + 1
\end{align}
$$
But since we only care about $O(\cdot)$, we can use the fact that runtime increases as $n$ increases (ie to pad a list of size 10 to $16=2^4$). So then $T(n)\le T(n’) \text{ if }n’\ge n$, where $n’$ is the smallest power of 2 bigger than $n$ ($n’ \le 2n$). 

### II. Induction

Prove that $T(n) \le c\cdot n\log n \forall n\ge 2$ for $T(n) =T(\lfloor\frac n2\rfloor) + T(\lceil\frac n2\rceil) + n-1​$. We can be rigorous here about the floor/ceiling. 

<u>Base Case</u>: $n=1$, then $T(1) = 0, c\cdot n\log n $ is 0. 

<u>Induction</u>: Assume that it’s true $\forall k < n$. Let’s split this into cases:

1. $n$ is even, then $T(n) = 2T(\frac n2) + n-1$

2. $n$ is odd, then $T(n) = T(\frac{n-1}2) + T(\frac{n+1}/2) + n-1$

   By induction, $T(n) \le c\frac{n-1}2\log\frac{n-1}2 + c\frac{n+1}2\log\frac{n+1}2 + n-1 \le c\cdot n\log n$, check this out with *log rules*.  

> CAUTION: Here is an example of a bad induction. $T(n) = 2T(\frac n2) + n$
>
> <u>Claim</u>: $T(n)\in O(n)$. 
>
> We need to prove that $\exists c, n_0 : T(n) \le c\cdot n \: \forall n\ge n_0$. So we assume by induction, $T(n’)\le c\cdot n’ \: \forall n’ \le n$.
> $$
> \begin{align}
> 	T(n) &= 2T(\frac n2) + n \\
> 	&\le 2c\cdot\frac n2 + n \\
> 	&= (c+1)n \\
> 	&= \text{constant}\cdot n
> \end{align}
> $$
> This is cheating since $(c+1)$ is increasing, so it’s not a constant!

### III. Master Theorem

The theorem is $T(n) = aT(\frac nb) + c\cdot n^k$. For the parameter $T(\frac nb)$, both floor and ceilings are allowed. We assume that $T(1)$ is a constant. $a\ge 1, b>1, c>0, k\ge 1$.  So, $T(n)\in$

- $\Theta(n^k)$ if $a<b^k$, or $\log_ba < k$.
- $\Theta(n^k\log n)$ if $a = b^k$
- $\Theta(n^{\log_ba})$ if $a > b^k​$

For rigorous proofs, we use induction, but the idea is to use a recursion tree. 
$$
\begin{align}
	T(n) = n^{\log_ba}T(1)+ c\cdot n^k\sum_{i=0}^{\log_bn-1}(\frac a{b^k})^i
\end{align}
$$
If $a<b^k$, then the first term is smaller, and the $\sum$ is constant. So then we arrive at $\Theta(n^k)$. 

If $a=b^k$, then both terms have $n^k$, and $\sum = \sum_{i=0}^{\log_bn} 1^i$. Thus $T(n) \in \Theta(n^k\log n)$. 

If $a > b^k$, then 