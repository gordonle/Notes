CS240 L06 | January 24^th^, 2019

# QuickSelect

```python
quick-select(A, k):
    p = choose-pivot(A)
    i = partition(A, p)
    if i = k:
        return A[i]
    elif i > k:
        return quick-select(A[0, 1, ..., i-1], k)
    elif i < k:
        return quick-select(A[i+1, i+2, ..., n-1], k-i-1)
```

Previously, we found that $T(n) \in \Theta(n^2)$. Why isn’t this $O$ or $\Omega$? We maintained equality throughout the proof.

## Average Case Analysis

Best and worst are easier, since we’re looking for the single input that will give us the best/worst case scenarios. When analyzing the average case, we take the average run-time over all instances of input of a size $n$.

There are thus $n!$ permutations of an array on $n$ numbers. The partition returns an index $i$ 

```text
                 i
-----------------------------------
|    <= A[i]    | |   >= A[i]     | # i partitions our array A
-----------------------------------
```

If we have uniform distribution, we will have that $i$ could equally likely be any array index from 0 to $n-1$. But then for any location of our pivot, how many permutations of the rest of the elements? $n-1$ elements remaining $\implies (n-1)!$ permutations. 

Note that for any set of distinct $n$ numbers, we will always have the same number of best case, worst case, and everything in between. The particular numbers don’t matter, it is their ***relative order*** that matters. So assuming that all $n!$ permutations are equally likely, the average run-time is the sum of costs for all permutations divided by $n!$.

We define $T(n)$ to be the average cost for selecting from an $n$ sized array, assuming we use `choose-pivot1(A)` that has runtime ___.

We fix one $0 \le i \le n-1$. There are $(n-1)!$ permutations for which the pivot-value $v$ is the $i$th smallest item (ie. the pivot index is $i$).
$$
\begin{align}
T(n) &= \frac{1}{n!} \sum_{I:size(I)=n}
\\ &= \frac{1}{n!} \sum_{i=0}^{n-1} \sum_{I\text{ has pivot-index }i}
\\ &\le \frac{1}{n!} \sum_{i=0}^{n-1} (n-1)! (c \cdot n+ max\{T(i), T(n-i-1)\})
\\ &\le \frac1n \sum_{i=0}^{n-1}(c \cdot n+ max\{T(i), T(n-i-1)\})
\\ &= c \cdot n + \frac1n \sum_{i=0}^{n-1}max\{T(i), T(n-i-1)\}
\end{align}
$$
We are basically doing $T(n, k)$ where there are three cases:

1. $i=k​$ : found the element
2. $i >k​$ : recurse left
3. $i<k$ : recurse right

We choose the worst of 1, 2, and 3 for the given $i$ to come up with an upper bound on the average run-time ( $\le$ ). So then in the end we have 
$$
T(n) \le c \cdot n + \frac1n \sum_{i=0}^{n-1}max\{T(i), T(n-i-1)\}, \:T(n) \in O(n)
$$

>**Ex:**
>
>```python
>foo(k):
>    for i = 1 to k:
>        print("k")
>```
>
>What’s the number of calls to print? If we know that $1\le k\le6$, and each is equally likely, let’s find the average number of times `print` is called (number of iterations).
>$$
>\begin{align}
>T(6) &= \frac16\sum_{i=1}^6i
>\\ &= \frac{21}6
>\end{align}
>$$
>We take the average run-time of each instance. Remember to **consider all inputs**, where each are **equally likely**.

==Theorem==: $T(n) \in \Theta(n)$.

==Proof==: 

| $i$  | size of max subproblem |
| ---- | ---------------------- |
| 0    | $n-1$                  |
| 1    | $n-2$                  |
| 2    | $n-3$                  |
| ...  | ...                    |

Lets be lazy and consider fewer cases. 

```text
----------------------------------------  \\ +: 1\2 of the time i will be here
|            |            |            |  \\ #: 1\2 of the time i will be here
|++++++++++++|############|++++++++++++|
|            |            |            |
----------------------------------------
            n\4        (3n)\4
```

So where the $T(n)$ term is the `+++` sections, and $T(\frac{3n}4)$ is the `###` section. We are choosing the largest subproblem of these two groups, each of which happens $\frac12$ of the time,
$$
\begin{align}
T(n) &\le cn + \frac12T(n)+\frac12T(\frac{3n}4), \: n\ge 2
\\ 2T(n) &\le 2cn + T(n) + T(\frac{3n}4)
\\ T(n) &\le 2cn + T(\frac{3n}4) \text{,  we will use this as our substitution formula!}
\\ &\le 2cn + 2c(\frac{3n}4) + T(\frac{9n}{16})
\\ &\le 2cn + 2c(\frac{3n}4) + 2c(\frac{9n}{16}) + T(\frac{27n}{64})
\\ & \dots
\\ T(n) &\le d + 2nc \sum_{i=0}^\infty (\frac34)^i
\\ &\le d + 2nc(4)
\end{align}
$$
$d, c$ are both constants, so now we have an upper bound! So $T(n) \in O(n)$

Remember that in best case, we have $T(n) \in \Theta(n)$, and we can use this as a lower-bound on our average run-time. With this we have both the upper and lower bounds, and so average run-time $T(n) \in \Theta(n)$, as required.

# Randomized Algorithms

A ==randomized algorithm== is one which relies on some **random numbers** in addition to the input. The cost will depend on the input and the random numbers used.

**Goal**: *no more bad instances, just unlucky numbers*. So we’ve shifted the dependency of costs from what we can’t control (the input) to what we can control (the random numbers).

## Expected Running Time

We define $T(I, R)$ to be the running time of the randomized algorithm for an instance I and the sequence of random numbers $R$. 

The ==expected running time== $T^{\text{(exp)}}(I)$ for instance $I$ is the expected value for $T(I, R)$, where $Pr[R]$ is the probability that we have $R$ is
$$
T^{\text{(exp)}}(I) = E[T(I,R)] = \sum_R(T(I,R)\cdot Pr[R])
$$

### Worst Case

$$
T^{\text{(exp)}}_{\text{worst}} = \text{max}_{I: size(I)=n} T^{\text{(exp)}}(I)
$$

### Average Case

$$
T^{\text{(exp)}}_{\text{avg}} = \frac1{|\{I: size(I)=n\}|} \sum_{I: size(I)=n}T^{\text{(exp)}}(I)
$$

For well designed random algorithms, these are the same.

## Randomized QuickSelect: Shuffle

`random(n)` returns an integer uniformly from $\{0, 1, ..., n-1\}$.

==Idea 1==: Randomly permute the input using `shuffle`:

```python
shuffle(A):
    for i = 0 to n-2 do:
        swap(A[i], A[i+random(n-i)])
```

Expected cost becomes the same as the average cost: $\Theta(n)$.

==Idea 2==: We can change the pivot selection.

```python
choose-pivot2(A)
	return random(n)

quick-select2(A, k):
    p = choose-pivot2(A)
    ...
```

With probability $\frac1n$ the random pivot has index $i$, the analysis is just like that for the average-case. The expected running time is again $\Theta(n)$. Generally, this is the fastest `quick-select` implementation.