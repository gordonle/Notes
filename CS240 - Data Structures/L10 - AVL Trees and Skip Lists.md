---
typora-root-url: ..\Images
---

CS240 L10 | February 7, 2019

# AVL Trees

Recall, when modifying AVL trees, it is important to maintain the property that the heights of either subtree at any given node can only differ by at most 1. Every node in the left subtree must be less, every node in the right greater than.

## Height of AVL Trees

From last time, $N(h)$ is the least number of nodes in an AVL tree of height $h$.
$$
\begin{align}
	N(h) &= 1 + N(h-1) + N(h-2)\text{, for $h\ge 1$}
	\\ &= 1\text{, for $h = 0$}
	\\ &= 0\text{, for $h=1$}
\end{align}
$$
Now,
$$
\begin{align}
	N(h) = 1+N(h-1)+N(h-2) &> 2N(h-2)
	\\ &> 2^iN(h-2i) \ge 2^{\lfloor \frac h2 \rfloor}N[0] = 2^{\lfloor \frac h2 \rfloor}
\end{align}
$$
$\therefore n > N(h) > 2^{\lfloor \frac h2 \rfloor}$. Solve for $h$, we get that $h < c\log n \implies h\in \Omega(\log n)$. 

## AVL Insertion

Recall, the maximum number of nodes in an AVL tree of height $h$ is ==$2^{h+1} - 1$==.  Here’s some pseudocode:

```python
def AVL-insert(r, k, v):
    # r is root, k is key, v is value
    z = BST-insert(r, k, v)
    z.height = 0
    while (z is not the root):
        z = parent of z
        if (|z.left.height - z.right.height| > 1):
            let y be taller child of z (breaks ties arbitrarily)
            let x be taller child of y (break ties to prefer left-left or right-right)
            z = restructure(x)
            break
        setHeightFromSubtrees(z)
```

and

```python
def setHeightFromSubtrees(u):
    if u is not an empty subtree:
        u.height = 1 + max(u.left.height, u.right.height)
```

Consider if we just added the node `16` to this tree. It is unbalanced at node `10`!

<svg width="550" height="400" version="1.1" xmlns="http://www.w3.org/2000/svg">
	<ellipse stroke="black" stroke-width="1" fill="none" cx="185.5" cy="115.5" rx="30" ry="30"/>
	<text x="180.5" y="121.5" font-family="Times New Roman" font-size="20">3</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="112.5" cy="181.5" rx="30" ry="30"/>
	<text x="107.5" y="187.5" font-family="Times New Roman" font-size="20">1</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="338.5" cy="115.5" rx="30" ry="30"/>
	<text x="328.5" y="121.5" font-family="Times New Roman" font-size="20">10</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="262.5" cy="50.5" rx="30" ry="30"/>
	<text x="257.5" y="56.5" font-family="Times New Roman" font-size="20">5</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="396.5" cy="181.5" rx="30" ry="30"/>
	<text x="386.5" y="187.5" font-family="Times New Roman" font-size="20">15</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="270.5" cy="181.5" rx="30" ry="30"/>
	<text x="265.5" y="187.5" font-family="Times New Roman" font-size="20">8</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="338.5" cy="258.5" rx="30" ry="30"/>
	<text x="328.5" y="264.5" font-family="Times New Roman" font-size="20">11</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="451.5" cy="258.5" rx="30" ry="30"/>
	<text x="441.5" y="264.5" font-family="Times New Roman" font-size="20">17</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="396.5" cy="340.5" rx="30" ry="30"/>
	<text x="386.5" y="346.5" font-family="Times New Roman" font-size="20">16</text>
	<polygon stroke="black" stroke-width="1" points="163.247,135.619 134.753,161.381"/>
	<polygon fill="black" stroke-width="1" points="134.753,161.381 144.041,159.724 137.334,152.307"/>
	<polygon stroke="black" stroke-width="1" points="316.973,136.394 292.027,160.606"/>
	<polygon fill="black" stroke-width="1" points="292.027,160.606 301.25,158.622 294.286,151.446"/>
	<polygon stroke="black" stroke-width="1" points="358.303,138.035 376.697,158.965"/>
	<polygon fill="black" stroke-width="1" points="376.697,158.965 375.171,149.655 367.66,156.256"/>
	<polygon stroke="black" stroke-width="1" points="285.299,69.999 315.701,96.001"/>
	<polygon fill="black" stroke-width="1" points="315.701,96.001 312.871,87.001 306.372,94.601"/>
	<polygon stroke="black" stroke-width="1" points="239.576,69.852 208.424,96.148"/>
	<polygon fill="black" stroke-width="1" points="208.424,96.148 217.763,94.809 211.312,87.167"/>
	<polygon stroke="black" stroke-width="1" points="413.937,205.912 434.063,234.088"/>
	<polygon fill="black" stroke-width="1" points="434.063,234.088 433.482,224.672 425.344,230.484"/>
	<polygon stroke="black" stroke-width="1" points="434.789,283.415 413.211,315.585"/>
	<polygon fill="black" stroke-width="1" points="413.211,315.585 421.82,311.727 413.515,306.156"/>
	<polygon stroke="black" stroke-width="1" points="378.45,205.463 356.55,234.537"/>
	<polygon fill="black" stroke-width="1" points="356.55,234.537 365.357,231.156 357.369,225.139"/>
</svg>

We have to rotate our tree, moving `15` up and swapping `11` to be the child of `10` instead of `17`.

<svg width="500" height="300" version="1.1" xmlns="http://www.w3.org/2000/svg">
	<ellipse stroke="black" stroke-width="1" fill="none" cx="185.5" cy="115.5" rx="30" ry="30"/>
	<text x="180.5" y="121.5" font-family="Times New Roman" font-size="20">3</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="112.5" cy="181.5" rx="30" ry="30"/>
	<text x="107.5" y="187.5" font-family="Times New Roman" font-size="20">1</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="338.5" cy="115.5" rx="30" ry="30"/>
	<text x="328.5" y="121.5" font-family="Times New Roman" font-size="20">15</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="262.5" cy="50.5" rx="30" ry="30"/>
	<text x="257.5" y="56.5" font-family="Times New Roman" font-size="20">5</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="396.5" cy="181.5" rx="30" ry="30"/>
	<text x="386.5" y="187.5" font-family="Times New Roman" font-size="20">17</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="270.5" cy="181.5" rx="30" ry="30"/>
	<text x="260.5" y="187.5" font-family="Times New Roman" font-size="20">10</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="338.5" cy="258.5" rx="30" ry="30"/>
	<text x="328.5" y="264.5" font-family="Times New Roman" font-size="20">11</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="455.5" cy="258.5" rx="30" ry="30"/>
	<text x="445.5" y="264.5" font-family="Times New Roman" font-size="20">16</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="193.5" cy="258.5" rx="30" ry="30"/>
	<text x="188.5" y="264.5" font-family="Times New Roman" font-size="20">8</text>
	<polygon stroke="black" stroke-width="1" points="163.247,135.619 134.753,161.381"/>
	<polygon fill="black" stroke-width="1" points="134.753,161.381 144.041,159.724 137.334,152.307"/>
	<polygon stroke="black" stroke-width="1" points="316.973,136.394 292.027,160.606"/>
	<polygon fill="black" stroke-width="1" points="292.027,160.606 301.25,158.622 294.286,151.446"/>
	<polygon stroke="black" stroke-width="1" points="358.303,138.035 376.697,158.965"/>
	<polygon fill="black" stroke-width="1" points="376.697,158.965 375.171,149.655 367.66,156.256"/>
	<polygon stroke="black" stroke-width="1" points="285.299,69.999 315.701,96.001"/>
	<polygon fill="black" stroke-width="1" points="315.701,96.001 312.871,87.001 306.372,94.601"/>
	<polygon stroke="black" stroke-width="1" points="239.576,69.852 208.424,96.148"/>
	<polygon fill="black" stroke-width="1" points="208.424,96.148 217.763,94.809 211.312,87.167"/>
	<polygon stroke="black" stroke-width="1" points="249.287,202.713 214.713,237.287"/>
	<polygon fill="black" stroke-width="1" points="214.713,237.287 223.906,235.165 216.835,228.094"/>
	<polygon stroke="black" stroke-width="1" points="290.358,203.987 318.642,236.013"/>
	<polygon fill="black" stroke-width="1" points="318.642,236.013 317.094,226.707 309.598,233.327"/>
	<polygon stroke="black" stroke-width="1" points="414.746,205.313 437.254,234.687"/>
	<polygon fill="black" stroke-width="1" points="437.254,234.687 436.357,225.296 428.419,231.378"/>
</svg>

```python
def rotate-right(z):
    y = z.left
    z.left = y.right
    z.right = y
    setHeightFromSubtrees(z)
    setHeightFromSubtrees(y)
    return y # the new root of the subtree
```

These are all ==**single rotations**==: the order property is maintained, and it is still a valid BST. We can do single right rotations or left ones. What if we need two rotations though?

### Double Rotations

Consider these trees. From left to right, we have done two rotations to fix the height property of our tree.

<svg width="700" height="300" version="1.1" xmlns="http://www.w3.org/2000/svg">
	<ellipse stroke="black" stroke-width="1" fill="none" cx="182.5" cy="47.5" rx="30" ry="30"/>
	<text x="177.5" y="53.5" font-family="Times New Roman" font-size="20">9</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="95.5" cy="142.5" rx="30" ry="30"/>
	<text x="90.5" y="148.5" font-family="Times New Roman" font-size="20">7</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="182.5" cy="227.5" rx="30" ry="30"/>
	<text x="177.5" y="233.5" font-family="Times New Roman" font-size="20">8</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="385.5" cy="47.5" rx="30" ry="30"/>
	<text x="380.5" y="53.5" font-family="Times New Roman" font-size="20">9</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="334.5" cy="142.5" rx="30" ry="30"/>
	<text x="329.5" y="148.5" font-family="Times New Roman" font-size="20">8</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="278.5" cy="233.5" rx="30" ry="30"/>
	<text x="273.5" y="239.5" font-family="Times New Roman" font-size="20">7</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="506.5" cy="98.5" rx="30" ry="30"/>
	<text x="501.5" y="104.5" font-family="Times New Roman" font-size="20">8</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="438.5" cy="188.5" rx="30" ry="30"/>
	<text x="433.5" y="194.5" font-family="Times New Roman" font-size="20">7</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="570.5" cy="188.5" rx="30" ry="30"/>
	<text x="565.5" y="194.5" font-family="Times New Roman" font-size="20">9</text>
	<polygon stroke="black" stroke-width="1" points="162.239,69.624 115.761,120.376"/>
	<polygon fill="black" stroke-width="1" points="115.761,120.376 124.852,117.853 117.477,111.099"/>
	<polygon stroke="black" stroke-width="1" points="161.042,206.535 116.958,163.465"/>
	<polygon fill="black" stroke-width="1" points="116.958,163.465 119.186,172.632 126.175,165.479"/>
	<polygon stroke="black" stroke-width="1" points="371.31,73.932 348.69,116.068"/>
	<polygon fill="black" stroke-width="1" points="348.69,116.068 356.879,111.384 348.068,106.655"/>
	<polygon stroke="black" stroke-width="1" points="318.777,168.05 294.223,207.95"/>
	<polygon fill="black" stroke-width="1" points="294.223,207.95 302.674,203.757 294.157,198.516"/>
	<polygon stroke="black" stroke-width="1" points="523.886,122.949 553.114,164.051"/>
	<polygon fill="black" stroke-width="1" points="553.114,164.051 552.553,154.634 544.403,160.429"/>
	<polygon stroke="black" stroke-width="1" points="488.415,122.436 456.585,164.564"/>
	<polygon fill="black" stroke-width="1" points="456.585,164.564 465.397,161.195 457.418,155.167"/>
</svg>

Double rotations are useful for fixing right-left or left-right imbalances. 

![Double_Right_Rotation](/Double_Right_Rotation.JPG)



We’ve done a left rotation on $y$, then a right rotation on $x$.

## AVL Deletion

We always take the ==in-order successor==. After we delete a node, we always have to recurse back up the tree to see if this deletion has violated any height properties. This may mean fixing the immediate parent, then recursing all the way back up to the root to find that we also need to perform rotations to fix it.

```python
def AVL-delete(r, k):
    z = BST-delete(r, k)
    # assume z is the child of the BST node that was removed
    setHeightFromSubtrees(z)
    while (z is not the root):
        z = parent of z
        if (|z.left.height - z.right.height| > 1):
            let y be the tallerchild of z
            let x be the taller child of y
            z = restructure(x)
        # ALWAYS continue up the path and fix if needed
        setHeightFromSubtrees(z)
```

Notice how this is very similar to our `AVL-insert` function! It’s because for both, we need to recurse back up the tree to fix any imbalances.

| Operation    | Run-time         |
| ------------ | ---------------- |
| `AVL-search` | $\Theta(height)$ |
| `AVL-insert` | $\Theta(height)$ |
| `AVL-delete` | $\Theta(height)$ |

and $\Theta(height) = \Theta(\log n)$

# Skip Lists

Imagine a regular linked list with a transit system on top. We have another linked list that is connected to every **other** node, then one on top of that that connects every four nodes, etc. This allows us to skip over elements faster and search better. Each node is connected both up and down if there are corresponding nodes in the “transit system”.

![Skip_Lists](/Skip_Lists.JPG)

```python
def skip-search(L, k):
    p = topmost left node of L
    P = stack of nodes, initially containing p
    while below(p) != null do:
        p = below(p)
        while key(after(p)) < k do:
            p = after(p)
        push p onto P
    return P
```

$P$ collects the predecessors of $k$ at level $S_0, S_1, ...$ which will be needed later on for `insert` and `delete`. $k$ is in $L$ if and only if `after(top(P))` has key $k$. Here’s a visualization of our stack $P$, when searching for `65`.

```text

| S0   44           |
---------------------
| S1   37           |
---------------------
| S2   -infinity    | since 65 < 65 is false, we keep going down
---------------------
| S3   -infinity    |
---------------------
```

We can see that `after(top(P)) = after(44) = 65`, thus we have found the node we want. Let’s do another example, searching for `87`:

```text

| S0   83           |
---------------------
| S1   83           |
---------------------
| S2   65           |
---------------------
| S3   -infinity    |
---------------------
```

In each level, we always push one node onto the stack.

## Inserting

How do we determine how many levels are above? We randomly determine the tower height by flipping a coin. Let $i$ be the number of times the coin flips *heads*; this will be the height of the tower of $k$ : $P(\text{tower of key $k$ has height} \ge l) = (\frac 12)^t$. We have to add every node to $S_0$, then we build the appropriate levels on top.

So what’s $P(\text{tower height 3})$? It is ==at least== $\frac 18$ but ==exactly== $\frac1{16}$. (HHH vs HHHT). 

| Level | Expected Number of Nodes |
| :---: | :----------------------: |
| $S_0$ |           $n$            |
| $S_1$ |       $\frac 12 n$       |
| $S_2$ |       $\frac 14 n$       |
|  ...  |           ...            |
| $S_k$ |     $(\frac 12)^kn$      |

The total over all levels $= \sum_{i=0}^h (\frac 12)^in \approx 2n​$, with a height of $h = \log n​$.

## Backwards Analysis

Start at the end node, and work to top-left ($-\infty$). What’s the probability that a node has a tower? $\frac 12$.
$$
\begin{align}
	T(k) &= \text{# of steps we take to go up $k$ levels }
\end{align}
$$
We then take 1 step, and then:

1. half of the time we can go up;
2. half of the time we go left;

The expected number of steps to go up $k$ levels is then defined by this recurrence relation:
$$
\begin{align}
	T(k) &= 1 + \frac 12 T(k-1) + \frac 12T(k)
	\\ 2T(k) &= 2 + T(k-1) + T(k)
	\\ T(k) &= 2 + T(k-1)
	\\ &= \cdots
	\\ &= 2k\text{, where $k$ is the number of levels} \in O(\log n)
\end{align}
$$
