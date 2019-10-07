CS341 L10 | October 7, 2019

To recall, with **Dynamic Programming**, the key idea is to identify subproblems and an order of solving them such that each subproblem can be solved by combining previously solved ones. 

# Example Problems

> **Constructing an Optimum Binary Search Tree**
>
> Given items $1...n$ and probabilities $p_1,...,p_n$, construct a BST to minimize search cost $(\sum_i p_i\times\text{depth}_i)$

The subproblems are to find the optimum search tree for items $i...j$, where $1\le i\le j\le n$. So our $M[i,j]$ wil hold the minimum cost for the BST on items $i..j$.
$$
M[i,j] = \sum_{t=i}^jp_t+\text{min}_{k=i..j}\{M[i, k-1] + M[k+1, j]\}
$$
To compute $\sum_{t=i}^jp_t$, we can compute the running sum $P[i] = \sum_{j=1}^ip_j$, $P[0]=0$ then $\sum_{t=i}^jp_t = P[j] - P[i-1]$. 

```python
for i in 1..n:
    M[i,i] = p_i
    M[i,i-1] = 0
M[n+1, n] = 0
for d in 1..n-1: 		# d is j-i 
    for i = 1..n-d: 	# j is i + d
    	# solve for M[i, i+d]
        best = infinity
        for k = i..i+d:
            temp = M[i,k-1] + M[k+1, i+d]
            if temp < best:
                best = temp
        M[i,i+d] = best + P[i+d] - P[i-1]
```

Looking for the run-time here, we have $n^2$ subproblem, and each subproblem takes $n$ time. Thus we get $O(n^3)$.

We actually can’t do something like 

```
i = 1..n:
	j = i..n:
		M[i,j] = min{}
```

because we’ll be missing subproblems/asking for things we haven’t solved yet! 

> **0-1 Knapsack**
>
> We have items $1..n$, where item $i$ has a weight $w_i\in\N$ and value $v_i$. Our goal is to choose a subset $S\subseteq\{1,..,n\}$ such that $\sum_{i\in S}w_i \le W$ while maximizing $\sum_{i\in S}v_i$, where $W\in \N$ is the capacity of our knapsack.

A first idea is to choose if item $n$ is in $S$ or  not:

- if $n\notin S$, we want the optimum solution in $\{1,..,n-1\}$
- if $n\in S$, we want a subset of $\{1,..,n-1\}$ with $\sum w_i \le W-w_n$.

There are subproblems for each pair $i, w$ where $i=0...n, w=0...W$. We’ll store this in a table $M$ of size $n\times W$, where $M[i,w] = \text{max}\sum_{i\in S} v_i$ for $S$ such that our weight fits the capacity and that we maximize value.
$$
\begin{align}
M[i,w] = max\{&M[i-1, w], \\
&v_i + M[i-1, w-w_i] \}
\end{align}
$$

```
initialize M[0, w] = 0
for i = 1..n:
	for w = 0...W:
		if w_i > w:
			M[i,w] = M[i-1, w]
		else:
			M[i,w] = max(... as written above)
```

This will take $O(nW)$ time. Is this polynomial time? We defined polynomial time as being polynomial based on the input size. Our input is $w_1,...,w_n, v_1,...,v_n, W$. The size is $\log W = t$ which is the number of bits. In terms of the size, our runtime is $O(n\cdot 2^t)$. Thus the runtime is <u>exponential</u> with respect to the size of $W=t$. This is called a ==pseudo-polynomial time algorithm==. There is no known algorithm for this problem that is truly in polynomial time. 

Read this in the notes for further detail on finding the solution. 

# Memoization

