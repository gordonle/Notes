CS341 L09 | October 2, 2019

# Dynamic Programming II

Let’s open with a problem. Count the number of changes/differences between 2 strings. 
$$
\begin{align}
	\text{You: } &\text{ r e c u r a n c e }
	\\ \text{Google:  } &\text { r e c u r r e n c e}
\end{align}
$$
A change is defined as one of:

- adding a letter
- deleting a letter
- changing a letter (this cost can depend on the letters involved)

This is called ==edit distance==.

> **Problem**: Given 2 strings, $x_1,...,x_m$ and $y_1,...,y_n$, compute their edit distance. 

Subproblem for  $x_1,...,x_i$ and $y_1,...,y_j$, where $M(i,j)=min(\text{# (or cost) of changes})$. At any point, we have a few options:

- match $x_i, y_j$
- match $x_i/y_j$ to a blank
- pay replacement cost if different
- delete $x_i/y_j$
- add a letter

So, $M(i,j) = min$ of

- $M(i-1, j-1)$ if $x_i == y_j$
- if $x_1\ne y_j$
  - $r(x_i, y_j) + M(i-1, j-1)$
  - $d + M(i-1, j)$
  - $a + M(i, j-1)$

where $r(x_i, y_j) = $ replacement cost, $d =$ cost for deletion, $a=$ cost for addition

We can see that this can be viewed as a $n\times m$ matrix, where you need the item above, left, and diagonally left/up to fill in your index. So then the runtime here takes $O(n\times m)$. 

> **Ex**: Weighted Interval Scheduling (aka. Happiest Schedule)
>
> Given set $I$ of intervals,
>
> ```
>         ----------
>             2
>               -----------
> ------------       3 ---------
>      5                   4
> ```
>
> each interval $i$ has weight $w(i)$. So find the set $S\subseteq I$ of disjoint intervals to get $max \sum_{i\in S}w(i)$.
>
> More generally, we have a set $I$ (not necessarily intervals) and we have conflict between some pairs in $I$. Could think of it like a graph, where overlapping intervals(conflicting items) are joined by edges, and we need to select all the nodes with the highest weight such that none are adjacent.  

A general approach to finding $OPT(I)$, could be this:

Consider one item $i\in I$. We either choose $i$ or we don’t. Then, $OPT(I) = max\{OPT(I-\{i\}), w(i)+OPT(I’)\}$ , where $I’=$ items that do not conflict with $i$. The problem is that this recursive solution is exponential! It may end up solving for all possible subsets of $I$, which come out to $2^n, n = |I|$. $T(n) = 2T(n-1) + O(1)$.

When $I$ is a set of intervals, we can use DP! First we’ll order $I$ by right endpoint (start time). Notice that for some $i$, intervals $I’$ that are disjoint from $i$ form a set $1..j$ for some $j$. Let $M(i)=$ max weight of subset of $1..i$. So $M(i)=max\{M(i-1), w(i) + M(p(i))\}$, where $p(i) = $ largest index $j$ such that interval $j$ is disjoint from $i$. 

```
M(0) = [0]
S(0) = []
for i = 1..n:
	compute p(i) - naive approach is O(n), could use BS O(logn)
	if M[i-1] >= w(i) + M[p(i)]:
		M[i] = M[i-1]
		S[i] = S[i-1]
	else:
		M[i] = w(i) + M[p(i)]
		S[i] = {i}U S(p(i))
return M[n], S[n]
```

Some improvements we can make:

- We don’t need to explicitly store the set $S$ of intervals used. 
- Just compute M, and use a recursive routine (we’ll call this $S-OPT(I)$)

```
s-OPT(i):
	if i = 0:
		return null
	else if M[i-1] > w(i) + M[p(i)]:
		return S-OPT(i-1)
	else:
		return {i} U S-OPT(p(i))
```

Theres a more efficient way to compute $p$ in $O(n)$. 

```
sort array by left endpoint
j = n
for k = n...1:
	while l_k overlaps j do:
		j = j-1
	p(l_k) = j
```





So then the final runtime would be $O(n\log n)$. 