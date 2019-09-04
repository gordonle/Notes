CS240 L21 | April 4^th^

### Summary

What happens is we have external memory that contains most of the data, but to be able to access and modify it we need to move it into internal memory, which is a very expensive operation.

# (a, b) - Trees

An *a-b-tree* satisfies the following points:

- Each node has at least $a$ subtrees, unless it’s a root.
- Each node has at most $b$ subtrees.
- If a node has $k$ subtrees, then it stores $k-1$ key-value pairs
- Empty subtrees are at the same level
- The keys in the node are between the keys in the corresponding subtrees.
- $a \le \lceil\frac b2\rceil$ . When $a=\lceil\frac b2\rceil$ then it’s a B-Tree.
- $h \in O(\log_a n)$, $h\in\Omega(\log_b n)$

The 2-4 Tree is a specific type of a-b Tree. 

==Note==: The number of children is always equal to the number of keys + 1. So 2-4 children corresponds to 1-4 keys.

# B-trees

A *B-tree of order* $m$ is a $(\lceil\frac m2\rceil, m)$-tree. A 2-4 tree is a B-tree of order 4.

## Analysis

If we assume that the entire B-tree is stored in internal memory, and that each node stores its key-value pair and subtree-pointers in a dictionary that supports $O(\log m)$ search, insert, and delete,

- `search`, `insert`, `delete` each require $\Theta(h)$ node operations. 
- Height $h​$ is 

The height
$$
\begin{align}
h &\in O(\log_an) \\
\text{if } a&=\lceil \frac m2\rceil \text{ then,} \\
h &\in O(\log_{\lceil \frac m2\rceil}n) \\
h &\in \Theta(\log_mn)
\end{align}
$$ {end{align}
The overall structure is a B-tree, but on each node individually they each must support something like an AVL-tree to support the $O(\log m)$ operations. So, runtime comes out to 
$$
\begin{align}
&\Theta(h) \cdot \Theta(\log m) \\=&\Theta(\log_mn)\cdot\Theta(\log_m)
\\=&\Theta(\frac{\log n}{\log m}\cdot\log m)
\\=&\Theta(\log n)
\end{align}
$$
The main application of B-trees is to store dictionaries in external memory. Recall that with AVL trees or 2-4 tree, $\Theta(\log n)$ blocks are loaded in the worst case. Instead, we’ll use a B-tree of order $m$, where $m$ is chosen so that an $m$-node fits into a single block. Typically $m\in\Theta(B)$, so each operation can be done with $\Theta(h)$ block transfers. 

The height of a B-tree is $\Theta(\log_mn) = \Theta(\log_Bn)$, which results in ***huge*** savings of block transfers.

## B-Tree Variations

==Pre-emptive splitting/merging==

- During search for insert, split *any* node close to overflow
- During search for delete, merge *any* node close to underflow
- We can then insert and delete at leaf then stop, which halves block transfers

==B^+^-Trees==:

- Only leaves have KVPs, and we link leaves sequentially
- The interior nodes store duplicates of keys to guide search-path
- Up to twice as many keys are therefore stored
- We have a larger $m$ since interior nodes do not hold values

==Cache-oblivious==:

- If we don’t know our block size $B$, we will make an initial node with $\sqrt{n}$ keys and $\sqrt{n}$ children

# Sorting

In external memory, how do we sort? Given an array $A$ stored externally of $n$ numbers, we need to sort. Remember to be able to modify these values, we need to load blocks into internal memory. 

- We could think that `Heapsort` is optimal, but it accesses $A$ at indices that are far apart, so there’s typically a one block transfer per array access
- `Mergesort` adapts well to an array stored in external memory; instead of splitting it into 2, we split into $d$ parts then sort those, then merge.

## $d$-way merge

Insert the first element of each array into a *min-heap* of size $d$. We then perform a *deleteMin* to get $A_i[j]$, then we will insert $A_i[j+1]$. For $d = 2$, we don’t need a *min-heap* since we can just compare the two values. Internally, increasing the value of $d$ won’t improve runtime, but with block transfers this optimizes sorting external memory.

The steps are as follows, where $n$ is the size of our array and $M$ is the size of our internal memory:

1. We create $\frac nM$ sorted runs of length $M$. $\Theta(\frac nB)$ block transfers.
2. Merge the first $d \approx \frac M{B-1}$ sorted runs using our *d-way* merge.
   - This is since $M$ is our limiting factor. Remember to leave one block empty for our output. 
   - Once the output block is full, we transfer from the output block to the output. 
   - Once a block gets empty, we have to load in the next block from that sorted run.
3. We keep merging the next runs to reduce the # of runs by a factor of $d$. One round of merging, so we get $\Theta(\frac nB)$ block transfers
4. We then have $\log_d(\frac nM)$ rounds of merging to create the sorted array.

The total number of block transfers results to $O(\log_d(n) \cdot \frac nB)$.

Assuming the External Memory Model (EMM), we can prove lower bounds.

# Dictionaries for Integers in External Memory

Recall that when using internal memory with direct addressing, we can get $O(1)$ insert and delete if keys are integers in $\{0, ..., U-1\}$. If keys were too large, we would simply map them to smaller integers.

But this doesn’t work well with external memory! This is because most hash strategies access many blocks (as our probe sequence is scattered), and rehashing results in loading *all* blocks.

Called *extendible hashing*, the idea here is to store tries of links to block of integers.

