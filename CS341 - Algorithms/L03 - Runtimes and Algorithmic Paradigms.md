CS341 L03 | September 11, 2019

Recall, we analyze algorithm run time using <u>asymptotic</u> worst case based on word RAM. We use Big Oh notation.

# Asymptotic Analysis of Algorithms

==Big Oh Notation==: Let’s consider functions $f(n)​$ and $g(n)​$ from $\N​$ to $\R^{\ge0}​$. Continuing from last time, 

Properties of $O(\cdot)​$

- **Max Rule**: $O(f(n) + g(n)) \in O(max(f(n), g(n)))$
- **Transitivity**: $f(n) \in O(g(n)) \and g(n)\in O(h(n)) \implies f(n) \in O(h(n))$ 

$f(n) \in \Omega(g(n))​$ if $\exists​$ constants $c>0, n_0​$ such that $f(n) \ge c\cdot g(n) \:\forall n \ge n_0​$. 

$f(n) \in \theta(g(n))$ if $f(n)\in O(g(n)) \and f(n)\in \Omega(g(n))$

$f(n) \in o(g(n))$ if for any constant $c>0$, $\exists n_0 : f(n) \le c \cdot g(n) \: \forall n \ge n_0$ . Equivalently, $\lim_{n\to\infin} \frac{f(n)}{g(n)} = 0$. 

$f(n)$ is $O(g(n))$ if $\exists$ constants $c>0$ and $n_0$ such that $f(n) \le c\cdot g(n)$ if $n \ge n_0$.

> Note, there are functions $f,g$ such that neither is big O of the other! Just use sinusoidal functions. 

## Typical Runtimes

| Run Time  | Algorithm                        |
| --------- | -------------------------------- |
| $\log n$  | binary search                    |
| $n$       | sum, max                         |
| $n\log n$ | sorting                          |
| $n^2$     | insertion sort                   |
| $n^3$     | multiplying $n\times n$ matrices |
| $2^n$     | try all subsets of $n$ items     |
| $n!$      | try all orderings of n items     |

## Non-typical Runtimes

- $\log(\log (n)) << \log (n) << \log ^2 (n) << \sqrt n << n << n\log n$, where $<<$ means “is little oh of”
- $n^a \in o(n^b) if a<b$
- $log^an \in o(n^b), b > 0$ 
- $n^a \in o(2^n), \forall a$ 

# Algorithmic Paradigms

We’re going to be focusing on 4 main paradigms:

1. Reductions
2. Divide & Conquer
3. Greedy
4. Dynamic Programming

## I. Reductions

The idea is to use the algorithms you have to solve new problems. Let’s look at some examples.

> **2-SUM**: The input is an array $A[1...n]$ of numbers and a target number $m$. Are there two numbers in the array that add up to $m$? So find $i, j : A[i] + A[j] = m$, where $i$ can equal $j$. Return SUCCESS if they exist.

<u>Algorithm 1</u>: Brute Force - $O(n^2)$

```
for i = 1..n
	for j = 1..n
		if A[i] + A[j] = m:
			return SUCCESS
return FAIL
```

<u>Algorithm 2</u>: Sort and Binary Search - $O(n\log n) + O(n\log n) \in O(n\log n)​$

```
sort A
for each i in A:
	do binary search for m-A[i]
```

<u>Algorithm 3</u>: Two pointers - $O(n\log n) + O(n) \in O(n\log n)$

```
sort A
i, j = 1, n
while i <= j:
	S = A[i] + A[j]
	if S > m:
		j = j-1
	else if S < m:
		i = i + 1
	else:
		return SUCCESS
return FAIL
```

For correctness, we must look for the invariant. If there’s a solution, $i^*, j^*, i^*\le j^*$, then $i^*\ge i, j^*\le j$. So verify the invariant.

> **3-SUM**: Similar to 2-SUM, except this time we want to find values $i, j, k : A[i] + A[j] + A[k] = m$. 

<u>Algorithm 1</u>: Brute Force - $O(n^3)$, try all possible 3 sums. 

<u>Algorithm 2</u>: Reduce 3-SUM to 2-SUM - $O(n^2)$

Since $A[i]+A[j] = m-A[k]$, we would run 2-SUM for every choice of $k=1..n$. This means that we have $n$ calls to 2-SUM, so $nO(n\log n) \in O(n^2\log n)$. But we only have this because we sort with every iteration of 2-SUM, so instead we can sort beforehand. This gives us a runtime of $O(n\log n) + O(n^2) \in O(n^2)$.

