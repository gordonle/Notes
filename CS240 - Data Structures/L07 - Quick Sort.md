CS240 L07 | January 29, 2019

# Quick Sort

Hoare combined `partition` and `quick-select` to create `quick-sort`:

```python
quick-sort1(A):
# A: Array of size n
	if n <= 1: return
    p = choose-pivot1(A)
    i = partition(A, p)
    quick-sort(A[0, 1, ..., i-1])
    quick-sort(A[i+1, ..., n-1])
```

**<u>Worst Case:</u>** $T^{(\text{worst})}(n) = T^{(\text{worst})}(n-1) + \Theta(n)$, so it’s the same as `quick-select1`: $T^{(\text{worst})}(n) \in \Theta(n^2)$.

**<u>Best Case:</u>** $T^{(\text{best})}(n) = T^{(\text{best})}(\lfloor \frac{n-1}{2}\rfloor) + T^{(\text{best})}(\lceil \frac{n-1}{2}\rceil) + \Theta(n)$, which is similar to `merge-sort`, where we have that 

$T^{(\text{best})}(n) \in \Theta(n \log n)$.

**<u>Average Case:</u>** As before, we have that $\frac1n$ of permutations have pivot index $i$. The recursive work is then $T^{(\text{avg})}(i) + T^{(\text{avg})}(n-i-1)$. So, the average running time is thus
$$
T^{(\text{avg})}(n) = c \cdot n + \frac1n \sum_{i=0}^{n-1}(T^{(\text{avg})}(i) + T^{(\text{avg})}(n-i-1)), \: n \ge 2
$$
Let’s prove that $T^{(\text{avg})}(n) \in \Theta(n \log n)$.

// need to prove

If we randomize our `quick-sort` by using `choose-pivot2`, it would give an *expected time* of $\Theta(n \log n)$. 

The auxiliary space is $\Omega(\text{recursion depth})$

- This is $\Theta(n)$ in the worst-case
- Can be reduced to $\Theta(\log n)​$ worst-case by recursing in a smaller sub-array first and replacing the other recursion by a while-loop

One should stop recursing when $n \le 10$. One run of `insertion-sort` at the end then sorts everything in $O(n)$ time since all items are within 10 units of their required position. Arrays with many duplicates can be sorted faster by changing `partition` to produce three subsets: |  $\le v$  |  $ = v$  |  $\ge v $  |. In practice, `quick-sort` is often the fastest. 

