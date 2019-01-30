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

