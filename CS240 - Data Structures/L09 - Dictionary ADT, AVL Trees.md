CS240 L09 | February 5, 2019

Recall,

### LSD-Radix Sort

```python
LSD-radix-sort(A):
# A: array of size n containing m-digit radix-R numbers
    for d = m down to 1 do:
        key-indexed-count-sort(A, d)
```

A is then sorted with respect to digits $d, ..., m$ of each entry. Time cost is $\Theta(m(n + R))$, auxiliary space $\Theta(n+R)$. With this, we avoid the recursion problem we had in MSD-Radix sort. $m = \text{# of digits}, n = \text{size of array}, R=\text{radix}$, and usually $n >> R$. But what if $n = R​$? Then we have linear time.

# Dictionary ADT

A *dictionary* is a collection of *items*, each of which contains a **key** and some **data**. These are called **key-value pairs** (KVP), where keys can be compared and are typically unique.

| Operations     | Unordered                    | Ordered                                |
| -------------- | ---------------------------- | -------------------------------------- |
| `search(k)`    | $\Theta(n)$                  | $\Theta(n \log n)$ (via binary search) |
| `insert(k, v)` | $\Theta(1)$                  | $\Theta(n)$                            |
| `delete(k)`    | $\Theta(n)$ (need to search) | $\Theta(n)$                            |

(other types of operations: `closestKeyBefore`, `join`, `isEmpty`, `size`)

When writing these, we assume that our dictionary has $n$ items, each KVP taking constant space, and keys are comparable in constant time.

## BST Search and Insert

This behaves the same way regular BST operations do; the keys represent the value seen in each node, and the value of each key does not affect the way in which our tree is built. We also want to build a *balanced tree* when possible. This will guarantee a height of $(\log n)$. 

`bst-insert()` and `bst-search()` are relatively easy. What about `bst-delete()`?

### `bst-delete()`

```python
bst-delete(B, k):
    # B is our tree, k is the key we want to delete
    x = bst-search(B, k)
    if x is leaf:
        delete x
    elif x has one child:
        replace x with its one child
    elif x has two children:
        y = smallest key in right subtree
        swap_key_values(x, y)
       	delete(y)
```

If $x$ has two children, go right then as left as possible to find node $y$. By doing so, we have taken the smallest key in the right subtree. This is choosing the *in-order successor*, which is convention. We can also choose the *in-order predecessor.* Swap keys and values at $x$ with $y$, then delete $y$. 

Search, insert, and delete all have cost $\Theta(h)$, where $h = \text{height of tree} = \text{max path length from root to leaf}$. If $n$ items are `bst-insert`ed one-at-a-time, how big is $h$?

- Worst-case: $n-1=\Theta(n)$

- Best-case: $\Theta(\log n)$.

  Any binary tree with $n$ nodes has height $h \ge \log(n+1)-1$

- Average Case: $\Theta(\log n)$

# AVL Trees

An **AVL Tree** is a BST with an additional *height-balance* property:

> The heights of the left subtree $L$ and right subtree $R$ differ by at most 1. 

When counting height, we are counting *edges*. This means an empty tree is defined as -1.

When implementing this, we store the height of the subtrees $hS =height(R) - height(L)$ in each node. At each non-empty subtree, we require $hS \in \{-1, 0, 1\}$:

- $-1$ means the tree is *left heavy*
- $0$ means the tree is balanced
- $1$ means the tree is *right heavy*

## Height of an AVL Tree

The height of an AVL Tree is $h = \Theta(\log n)$. All the operations (search, insert, delete) all cost $\Theta(\log n)$ as well!

**<u>Proof:</u>** Define $N(h)$ to be the least number of nodes in a height - $h$ AVL tree $T$. What is the recurrence relation for $N(h)$? What does this recurrence relation resolve to? Let’s find out.

Let $n \ge N(h)$ be the number of nodes in $T$. From the root node, we know that one subtree must have at least height $h-1$, and the other $h-2$, so that when we count the root node it gets height $h$. Both subtrees cannot be $h-1$, otherwise $N(h)$ will not be minimal.
$$
\begin{align}
	N(h) &= 1 + N(h-1) + N(h-2)\text{, for  }h\ge1
	\\ &= 1 \text{, for h = 0 (leaf)}
	\\ &= 0 \text{, for h = -1 (empty)}
\end{align}
$$
This is our recurrence relation! Notice that this is similar to the **Fibonacci Sequence**. 

| Fibonacci | $N(h)$      | Relation        |
| --------- | ----------- | --------------- |
| $F_0 = 0$ | $N(-1) = 0$ |                 |
| $F_1 = 1$ | $N(0) = 1$  | $= F_3 -1$      |
| $F_2 = 1$ | $N(1) = 2$  | $= F_4 -1$      |
| $F_3 = 2$ | $N(2) = 4$  | $= F_5-1$       |
| $F_4 = 3$ | ...         | ...             |
| $F_5 = 5$ | $N(h)$      | $= F_{h+3} - 1$ |

So by using the general formula for Fibonacci,
$$
\begin{align}
	F_n &= \lceil \frac{\varphi^n}{\sqrt5} \rfloor \text{  (integer closest to)}
	\\ N(h) &= \lceil \frac{\varphi^{h+3}}{\sqrt5} \rfloor - 1 \implies n= \lceil \frac{\varphi^{h+3}}{\sqrt5} \rfloor - 1
	\\ \text{where } \varphi &= \frac{1+\sqrt5}2, \text{ the Golden Ratio}
\end{align}
$$
Alternatively, $N(h) > 2N(h-2) > 4N(h-4) > 8N(h-8) > ... > 2^iN(h-2i)$ . When does this stop? How many times can we subtract 2? Until we hit a base case that $(h-2i)$ is 0 or 1. So,
$$
n \ge N(h) > \cdots > 2^iN(h-2i) \ge 2^{\lfloor \frac h2 \rfloor}
$$
We’ve thus found a lower bound on $h$, so $h \in \Omega(\log n)$. What about the upper bound? What’s the maximum number of nodes in a tree of height $h$? There then must be $h+1$ levels. How many nodes populate these levels? $2^{h+1}-1$. So $h \in O(\log n)$. 

## AVL Insertion

Insertion works similar to regular trees. Once inserted, move up from the new leaf nodes and update the heights. If at node $z$ the height different $\pm 2$, then $z$ is *unbalanced*. We must re-structure the tree to rebalance it, through rotation.

### Right Rotation

Performing a right rotation on $z$ results like so

<svg width="525" height="400" version="1.1" xmlns="http://www.w3.org/2000/svg">
	<ellipse stroke="black" stroke-width="1" fill="none" cx="348.5" cy="62.5" rx="30" ry="30"/>
	<text x="344.5" y="68.5" font-family="Times New Roman" font-size="20">z</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="218.5" cy="151.5" rx="30" ry="30"/>
	<text x="213.5" y="157.5" font-family="Times New Roman" font-size="20">y</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="148.5" cy="261.5" rx="30" ry="30"/>
	<text x="143.5" y="267.5" font-family="Times New Roman" font-size="20">x</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="280.5" cy="261.5" rx="30" ry="30"/>
	<text x="273.5" y="267.5" font-family="Times New Roman" font-size="20">C</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="477.5" cy="151.5" rx="30" ry="30"/>
	<text x="470.5" y="157.5" font-family="Times New Roman" font-size="20">D</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="91.5" cy="359.5" rx="30" ry="30"/>
	<text x="84.5" y="365.5" font-family="Times New Roman" font-size="20">A</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="202.5" cy="359.5" rx="30" ry="30"/>
	<text x="195.5" y="365.5" font-family="Times New Roman" font-size="20">B</text>
	<polygon stroke="black" stroke-width="1" points="323.745,79.447 243.255,134.553"/>
	<polygon fill="black" stroke-width="1" points="243.255,134.553 252.68,134.159 247.031,125.908"/>
	<polygon stroke="black" stroke-width="1" points="202.394,176.81 164.606,236.19"/>
	<polygon fill="black" stroke-width="1" points="164.606,236.19 173.12,232.125 164.683,226.756"/>
	<polygon stroke="black" stroke-width="1" points="373.193,79.536 452.807,134.464"/>
	<polygon fill="black" stroke-width="1" points="452.807,134.464 449.061,125.805 443.382,134.036"/>
	<polygon stroke="black" stroke-width="1" points="233.23,177.635 265.77,235.365"/>
	<polygon fill="black" stroke-width="1" points="265.77,235.365 266.197,225.941 257.486,230.851"/>
	<polygon stroke="black" stroke-width="1" points="133.417,287.433 106.583,333.567"/>
	<polygon fill="black" stroke-width="1" points="106.583,333.567 114.927,329.166 106.283,324.138"/>
	<polygon stroke="black" stroke-width="1" points="162.978,287.775 188.022,333.225"/>
	<polygon fill="black" stroke-width="1" points="188.022,333.225 188.54,323.805 179.782,328.631"/>
</svg>

becomes

<svg width="575" height="310" version="1.1" xmlns="http://www.w3.org/2000/svg">
	<ellipse stroke="black" stroke-width="1" fill="none" cx="218.5" cy="143.5" rx="30" ry="30"/>
	<text x="213.5" y="149.5" font-family="Times New Roman" font-size="20">x</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="148.5" cy="261.5" rx="30" ry="30"/>
	<text x="141.5" y="267.5" font-family="Times New Roman" font-size="20">A</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="280.5" cy="261.5" rx="30" ry="30"/>
	<text x="273.5" y="267.5" font-family="Times New Roman" font-size="20">B</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="482.5" cy="143.5" rx="30" ry="30"/>
	<text x="478.5" y="149.5" font-family="Times New Roman" font-size="20">z</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="351.5" cy="49.5" rx="30" ry="30"/>
	<text x="346.5" y="55.5" font-family="Times New Roman" font-size="20">y</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="542.5" cy="261.5" rx="30" ry="30"/>
	<text x="535.5" y="267.5" font-family="Times New Roman" font-size="20">D</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="418.5" cy="261.5" rx="30" ry="30"/>
	<text x="411.5" y="267.5" font-family="Times New Roman" font-size="20">C</text>
	<polygon stroke="black" stroke-width="1" points="203.194,169.302 163.806,235.698"/>
	<polygon fill="black" stroke-width="1" points="163.806,235.698 172.188,231.369 163.587,226.267"/>
	<polygon stroke="black" stroke-width="1" points="232.454,170.057 266.546,234.943"/>
	<polygon fill="black" stroke-width="1" points="266.546,234.943 267.251,225.535 258.399,230.186"/>
	<polygon stroke="black" stroke-width="1" points="468.197,169.871 432.803,235.129"/>
	<polygon fill="black" stroke-width="1" points="432.803,235.129 441.012,230.481 432.222,225.713"/>
	<polygon stroke="black" stroke-width="1" points="496.097,170.242 528.903,234.758"/>
	<polygon fill="black" stroke-width="1" points="528.903,234.758 529.734,225.361 520.82,229.894"/>
	<polygon stroke="black" stroke-width="1" points="375.874,66.99 458.126,126.01"/>
	<polygon fill="black" stroke-width="1" points="458.126,126.01 454.541,117.284 448.711,125.408"/>
	<polygon stroke="black" stroke-width="1" points="327.001,66.815 242.999,126.185"/>
	<polygon fill="black" stroke-width="1" points="242.999,126.185 252.418,125.651 246.646,117.485"/>
</svg>

where $x,y,z$ are nodes and  $A, B, C, D$ are subtrees.