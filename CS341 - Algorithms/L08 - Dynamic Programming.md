CS341 L08 | September 30, 2019

# Dynamic Programming

The concept here is to divide our main problem into smaller, sub-problems. By doing so, we can save our result each time we solve a sub-problem, so that if we ever need to solve it again we don’t need to redo our calculations. 

A simple example of this is with Fibonacci! We only need to keep track of how far we’ve gone, as well as the previous two Fibonacci items. Doing this recursively would result in an exponential number of iterations on our stack, and would be terribly bad. Doing this iteratively though, avoid re-computing $f(i)$ for $i < n$. 

> **Ex**: Text Segmentation
>
> Given a long string of letters $A[1..n]$ where $A[i] \in \{a,b,...,z\}$, can we split $A$ into words? For this, we’ll assume that we have a dictionary/test to see if a string is a word ($Word[i,j]$ will return $T/F$ if it’s a word or not. Assume $O(1)$ operation). 
>

Suppose we’re given $A=THEMEMPTY$. If we used greedy here, we could try to pull of the shortest word (THE) or the longest word (THEME), but then that would return the wrong answer.

What if we knew $Split[k]$, which is $T$ only if $A[1..k]$ is split-able. If $k=0..n-1$, can we find $Split[n]$? 

```
for all k = 0...n-1
	if Split[k] and Word[k+1, n], set Split[n] as true!
```

Our claim is that $Split[n] \iff$ at least one $k$ gives us true for the above algorithm. Here’s the full pseudocode:

```
Split[] <- n-sized array
Split[0] <- True
for k = 1..n:
	S[k] <- False
	for j = k-1...0:
		if Split[j] AND Word[j+1, k]:
			Split[k] <- True
			break
return Split[n]
```

This runs in $\Theta(n^2)$. Is there a way to tell what words we get from the split? Try adding into the pseudocode a way to do this. (Hint: Try using an array to keep track of where we split)

Let’s try another example,

> **Ex**: Longest Increasing Subsequence
>
> Given a sequence of numbers $A[1..n]$, where $A[i] \in \N$, find the longest increasing subsequence. Pretty simple $O(n^2)$ solution, can you find the $O(n\log n)$ solution? 

Lastly,

> **Ex**: Maximum Common Subsequence
>
> Given two strings $x_1,..,x_n$ and $y_1,...,y_m$, find the longest common substring (can skip letters but not change order).
>

Try $M(i,j)$ =  length of the longest common substring $s$ of $x_1,...,x_i$ and $y_1,...,j_j$. There are $n\cdot m$ subproblems here. To build our subproblems, we could:

1. Match $x_i$ and $y_j$, in which case we can use $M[i-1, j-1]$. 
2. Skip $x_i$
3. Skip $y_j$

<u>Claim</u>: We cannot match $x_i$ with previous $y_k$ and we cannot match $y_j$ with a previous $x_{\ell}$.

$M(i,j) = max\{1+M(i-1, j-1) \text{ if }x_i = y_j, M(i-1, j) \text{ to skip }x_i, M(i, j-1) \text{to skip }y_j \}$

Starting points:

$M(i, 0) = 0, \forall i = 0..n$, and $M(0, j) = 0 \forall j=0...m$ .

---

Typically in DP, we find that the run-time = (# of subproblems) * (max time to solve one subproblem).

