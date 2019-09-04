---
typora-root-url: ..\Images
---

CS 240 L04 | January 17, 2019

# Techniques for Algorithm Analysis

```ruby
Test2(A, n)
max = 0
for i = 1 to n do
    for j = i to n do
        sum = 0
        for k = i to j do
            sum = A[k]
return max
```

Each iteration is $\Theta(1)$ time, and the number of iterations, $N$,
$$
\begin{align} N &= \sum_{i=1}^n \sum_{j=i}^n \sum_{k=i}^j 1 \\ &= \sum_{i=1}^n \sum_{j=i}^n (j - i + 1)  \end{align})
$$
Now we separate out part of the sum that depends on $j$ (the index):
$$
\begin{align} &= \sum_{i=1}^n [\sum_{j=i}^n - \sum_{j=i}^n (i-1)] \\ &= \sum_{i=1}^n [\sum_{j = i}^n j - (n - i + 1)(i - 1)]\end{align}
$$
But now we need to put $\sum_{j=i}^n$ into a form we know
$$
\begin{align} &= \sum_{i=1}^n [\sum_{j=1}^n j- \sum_{j=1}^{i-1}j-(n-i+1)(i-1)]\end{align}
$$
Notice that $(n-i+1)(i-1)$ is not part of the summation. We continue to use algebra to expand to get
$$
= \frac {1}{6}n^3 + \frac{1}{2}n^2 + \frac{1}{3}n
$$
Alternatively, we could get $O$ and $\Omega$ separately:
$$
N = \sum
$$

## Insertion Sort

```ruby
Test3(A, n)
# A: array of size n
for i = 1 to n - 1 do
    j = i
    while j > 0 and A[j] > A[j-1] do
        swap A[j] and A[j-1]
        j = j-1
```

Let $T_A(I)$ denote the running time of an algorithm A on instance $I$

| Best Case                                                    | Worst Case                                                   | Average Case                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| The list is already sorted, so the while loop will do 1 comparison. Thus *best* case is $\Theta (n)$, where we run through the array once per value of $i$. | If the array is in reverse sorted order, then we will always do $j$ iterations for every $i$ to $n$. Thus our runtime is now $\Theta(n^2)$ . | average over all inputs of size $n$, which is $n!$ different inputs (every permutation of the $n$ numbers. |



**Best Case**: in the while loop we will only do 1 comparison each time if the list is already sorted. So the runtime in the *best* case is $\Theta (n)$, where we run through the array once per value of $i$.

**Worst Case**: If the array is in reverse sorted order, then we will always do $j$ iterations for every $i$ to $n$. Thus our runtime is now $\Theta(n^2)$ . So for any input $I$ of size $n$,
$$
T_A(n) = max\{T_A(I): Size(I) = n\}
$$


**Average Case Complexity**: average over all inputs $I$ of size $n$, which is $n!$ different inputs (every permutation of the $n$ numbers.
$$
T_A^{avg}(n) =  \frac{1}{|\{I: Size(I) = n\}|} \sum_{\{I: Size(I) = n\}} T_A(I)
$$

> Remember to not make comparisons between algorithms using O-notation. For example, suppose $A_1$ and $A_2$ both solve the same problem, $A_1$ has worst-case run-time $O(n^3)$ and $A_2$ has worst-case run-time of $O(n^2)$. The

## Merge Sort

To avoid copying sub-arrays, the recursion uses parameters that give the range of the array that needs to be sorted.

```ruby
# MergeSort(A, l = 0, r = n-1)
# A: array of size n, 0 <= l <= r <= n-1
if (r <= l) then
    return
else
    m = (r + l)/2
    MergeSort(A, l, m)
    MergeSort(A, m+1, r)
    Merge(A, l, m, r)
```

`Merge` takes $O(n)$ time to merge $n$ items. We know that since we are cutting the array by half each time, so there are at most $log(n)$ iterations! We run this for each element, thus we run it $n$ times, so the run-time comes out to be $O(nlog(n))$. `MergeSort` actually has a recurrence relation that we can analyze to find its run-time.

# Priority Queues

The run-time of this ADT depends on how we choose to implement the priority queue. It is sometimes written as $O(n+n * insert + n * deleteMax)$. Let’s look at some methods of implementation:

## Array

Arrays are easy to insert at the end, but we will often need to shift elements to close/open a space. Here, we’ll assume that we are using *dynamic arrays*. 

|           | Unsorted Array             | Sorted Array |
| --------- | -------------------------- | ------------ |
| Insert    | $O(1)$                     | $O(1)$       |
| deleteMax | $O(n)$ amortized to $O(1)$ | $O(1)$       |

So we find that using sorted vs unsorted is identical. Turns out using **linked lists** is also identical.

## Binary Heap

Binary Heaps are certain types of binary trees. Recall that a binary tree with $n$ nodes has height at least $log(n+1) -1 \in \Omega(log \space n)$ . Here’s an example heap:

![Example_Heap](/Example_Heap.JPG)

There are 2 properties to this max heap structure:

1. All the levels of a heap are completely filled, except (possibly) the last level. The filled in items in the last level are **left justified**
   1. Thus, the height of the heap with $n$ nodes is $\Theta(log\space n)$ 
2. The root has the highest priority
   1. in particular, the parent of a node will always have greater priority

We will store our heap of $n$ nodes in an **array**. For the $i$^th^ element,

| Root | Left Child  | Right Child | Parent                               | Last Node |
| ---- | ----------- | ----------- | ------------------------------------ | --------- |
| A[0] | A[$2i + 1$] | A[$2i + 2$] | $(i\ne 0)$ A[floor($\frac{i-1}{2}$)] | A[$n-1$]  |

### insert

1. We place the new key at the first free leaf

2. The heap order may now be violated. Perform a `fix-up`:

   ```php
   # fix-up(A, k)
   # A: array storing a heap
   # k: current index
   while parent(k) exists and A[parent(k)] < A[k] do
       swap A[k] and A[parent(k)]
       k = parent(k)
   ```

   The new item will then bubble up until it reaches the correct place in the heap. Our tree is of height $log \space n$ so the run-time is $O(log\space n)$ .

### deleteMax

The maximum value in our heap is the **root node**. So,

1. Replace root with last leaf

2. Ordering property may be violated, so perform a `fix-down`:

   ```php
   # fix-down(A, n, k)
   # A: array that stores heap of size n
   # k: an index corresponding to our current node
   while k is not a leaf do
       # Find the child with the larger key
       j = left child of k
       if (j is not last(n)and A[j+1] > A[j])
           j = j + 1
       if A[k] => A[j] break
       swap A[j] and A[k]
       k = j
   ```

   Also run-time of $O(log \space n)$.

### Sorting with Priority Queue

So now we can insert all $n$ items into our priority queue, then remove them in order!

```php
PQ-SortWithHeaps(A):
initialize H to empty heap
for k = 0 to n-1 do
    H.insert(A[k])
for k = n-1 down to 0 do
    A[k] = H.deleteMax()
```

This takes $O(nlog\space n)$ time!

### Building a Heap by Bubble-down

Given $n$ items in an array $A$, build a heap containing all of them.

If we use `fix-down`s,

```php
heapify(A)
n = A.size()
for i = parent(last(n)) down to 0 do
    fix-down(A, n, i)
```

This yields a worst-case complexity of $\Theta (n)$ .

