CS240 L05 | January 22, 2019

# Binary Heaps

> **Recall**: A binary heap is ***NOT*** a Binary Search Tree (BST), we actually store it in an **array**. We do this for space efficiency - there aren’t many holes in the middle of the array, so we’re actually using almost (if not all) of it, and we don’t need to store pointers to the right & left children.

**Lemma**: Height of a heap with n nodes is $\Theta(log\space n)$. Note that all levels *except the last* must be full.

**Proof**: Suppose the height of the tree is $h$. We know that the number of nodes $n$ must include at least 1 node on level $h$, so we can give it a lower bound, resulting in an upper bound on $h$.
$$
\begin{align} n &\ge 2^0+2^1+...+2^{h-1}+1 = 2^h
\\ n &\ge 2^h
\\ log(n) &\ge log(2^h) = hlog(2)
\\ \implies h &\le log(n)
\\ \implies h &\in O(log\space n)
\end{align}
$$
Similarly, we give $n$ an upper bound to get a lower bound on $h$ 
$$
\begin{align}
n &\le 2^0+2^1+...+2^{h-1}+2^h = 2^{h+1} -1
\\n+1 &\le 2^{h+1}
\\ \implies h &\ge log(n+1) -1
\\ \implies h &\in \Omega(log\space n)
\\ \therefore h &\in \Theta(log\space n)
\end{align}
$$

## Sorting using Heaps

In HeapSort, we can sort an array by inserting all the elements into the array, then removing them. Using this method will have a run-time of $O(nlog\space n)$, since we know that `insert` and `deleteMax` each run in $O(log\space n)$ time, and we have $n$ nodes. We can improve this with two simple tricks:

1. If we know all input in advance
2. Can use the same array for input and for the heap ( $O(1)$ additional space! )

> Given n items (in A[0 · · · n − 1]) build a heap containing all of them.

We can build our heaps either by Bubbling-Up or Bubbling-Down

### Bubble-Up

Start with an empty heap and insert items in one at a time:

```python
# A is the array
simpleHeapBuilding(A):
    initialize H as an empty heap
    for i = 0 to size(A)-1 do:
        H.insert(A[i])
```

This means we must call `fix-up` each insertion, and has a running time of $\Theta(nlog\space n)$

### Bubble-Down

Use `fix-downs` instead

```python
# A is the array
heapify(A):
    n = A.size()
    for i = parent(last(n)) downto 0 do:
        fix-down(A, n, i)
```

Run-time: we can consider the nodes by level.  For a tree of height $h$ with $n$ nodes, 

| Level | # of nodes | Height of tree where node is root |
| ----- | ---------- | --------------------------------- |
| 0     | 1          | $h$                               |
| 1     | 2          | $h-1$                             |
| 2     | 4          | $h-2$                             |
| $h$   | $\le 2^h$  | 0                                 |

So, we have no work to do if we are at the bottom level!

**Lemma:** $n \le 2^{h+1} -1$

**Lemma:** 

for $i$ in {0, 1 , 2, ..., h }, # nodes with height $i \le 2^{h-1}$

\# of swaps for fix-down from height $i$ is $\le i$

Total # of swaps:
$$
\sum_{i=0}^hi*2^{h-1} \le \sum_{i=0}^hn\frac{i}{2^i} \lt n \sum_{i=1}^\infin \frac{i}{2^i} = 2n
$$
Thus we have a run-time of $\Theta(n)​$. The benefits of this is that we are using the same array, so no additional space is required.

So finally, our `HeapSort` will look like this: 

```python
HeapSort(A, n):
    # heapify it in linear time
    n = A.size()
    for i = parent(last(n)) downto 0 do:
        fix-down(A, n, i)
    while n > 1:
        # deleteMax
        swap items at A[root()] and A[last(n)]
        decrease n
        fix-down(A, n root())
```

`Heapify` takes $O(n)$ and `deleteMax` takes $O(nlog\space n)$ so our `HeapSort` takes $O(nlog\space n)$.

> The $k$th-max problem asks to find the $k$th largest item in an array A of n numbers.

 **Solution 3:** Scan the array and maintain the k largest numbers seen so far in a min-heap 

array of size $n$, heap of size $k$, heap operations are $O(log\space k) \implies$  total runtime of $O(nlog\space k)$

**Solution 4:** Make a max-heap by calling `heapify(A)`. Call `deleteMax(A)` k times.

`heapify` $\implies$ heap of size n, operations on heap are $O(log\space n)\implies $ total complexity is $\Theta(n + klog\space n)$

# Selecting & Sorting

> **Ex:** Given number 9 and array [3, 2, 8, 7, 6, 11, 12, 22, 1, 9], if sorted, what index would 9 be at? 
>
> 6 numbers less than, 3 numbers greater, so 9 should be at 6th index. This took $\Theta(n)$ time - we just went through the array once.

**Selection Problem:** Given an array $A$ of $n$ numbers, and $0\le k \lt n$, find the element that would be at position $k$ of the sorted array.

We do this by using `quick-select`, similar to quicksort. We rely on two subroutines:

`choose-pivot(A)`: Choose an index p. We will use the pivot-value $v = A[p]$ to rearrange the array

`partition(A, p)`: Rearrange $A$ and return pivot-index $i$ so that

- the pivot-value $v$ is in $A[i]$
- elements from 0 to $i-1$ is < $v$
- elements from $i+1$ to $n-1$ is > $v$

```python
partition(A, p):
    # create empty lists small and large
    v = A[p]
    for each element x in A[0, ..., p-1] or A[p+1,...,n-1]:
        if x < v append x to small
        else append x to large
    i = size(small)
    Overwrite A[0, ..., i-1] by elements in small
    Overwrite A[i] by v
    Overwrite A[i+1, ..., n-1] by elements in large
    return i
```

We want to do this within the original array, this will save space!

| 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | j=9  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 30   | 60   | 10   | 0    | 50   | 80   | 90   | 20   | 40   | v=70 |

| 0    | 1    | 2    | 3    | 4    | i=5  | 6    | 7    | j=8  | 9    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 30   | 60   | 10   | 0    | 50   | 80   | 90   | 20   | 40   | v=70 |

Swap them!

| 0    | 1    | 2    | 3    | 4    | i=5  | 6    | 7    | j=8  | 9    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 30   | 60   | 10   | 0    | 50   | 40   | 90   | 20   | 80   | v=70 |

...

| 0    | 1    | 2    | 3    | 4    | 5    | j=6  | i=7  | 8    | 9    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 30   | 60   | 10   | 0    | 50   | 40   | 20   | 90   | 80   | v=70 |

At the end, after $j$ and $i$ have crossed, then we are done! We swap the element at $i$ with our pivot!

| 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 30   | 60   | 10   | 0    | 50   | 40   | 20   | 70   | 80   | 90   |

### `quick-select` algorithm

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

$k$ = we want to find the item that will be at this index if the array was sorted

$i$ = partition, the index of the item we used as a pivot; where it is if the array is sorted!

> We’re only trying to find the index of one element, so it doesn’t matter if the indexes on the other side of $i$ in $A$ are sorted or not. Note that when looking on the right side of $i$, we have to re-index $k$ to be $k-i-1$, since we aren’t considering the first $i+1$ elements anymore.

#### Run-time Analysis

**Best Case:** $i=k​$, so we have found $k​$ right away. This takes $\Theta(n)​$ - we must partition *at least* once.

**Worst Case:** How big would the subproblem be in the worst case? $n-1$. Our pivot would be either the largest or smallest element. We end up with a recurrence relation.
$$
\begin{align}
T(n)= \space &T(n-1)+cn, n\ge 2
\\&d \text{ or }c , n=1
\end{align}
$$
Where $T(n-1)​$ is the subproblem and $cn​$ is the partition, for some constant $c > 0​$ and base case $d​$. Then,
$$
\begin{align}
T(n) = T(n-1) + cn&=[T(n-2)+c(n-1)]+cn
\\ &=[[T(n-3) + c(n-2)]+c(n-1)]+cn
\\ &...
\\ &= d + 2c + 3c + ... + (n-1)c + nc
\\ &= d + c[2 + 3 +...+n]
\\ &= d + c[(n+2)(\frac{n-1}2)]\in \Theta(n^2)
\end{align}
$$
