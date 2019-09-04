CS240 L13 | March 7^th^, 2019

# Multidimensional Data

Multidimensional Data has many applications, for example:

- Laptop: Price, Screen size, processor speed, RAM, hard drive, etc
- Employee: name, age, salary, team, etc

Basically it’s a **dictionary for multi-dimensional data**. In a collection of $d$-dimensional items, each item has $d$ ***aspects*** (coordinates): $(x_0, x_1, \cdots, x_d)$

# Quadtrees

We have $n$ points $S = \{(x_0, y_0), (x_1, y_1), \cdots, (x_{n-1}, y_{n-1})\}$ in the plane. We assume that all points are within a square $R$. Ideally, the width/height of $R$ is a power of 2, and we can find $R$ by computing the minimum and maximum $x$ and $y$ values in S.

## Build A Quadtree

The root $r$ of the quadtree corresponds to $R$

1. If $R$ contains 0 or 1 points, then root $r$ is a leaf that stores point
2. Else, *split*:
   - we partition $R​$ into four equal subsquares (quadrants): $R_{NE}, R_{NW}, R_{SW}, R_{SE}​$.
   - The root has four subtrees $T_{NE}, T_{NW}, T_{SW}, T_{SE}; T_i$ is associated with $R_i$
3. We recursively repeat this process at each subtree

==Convention==: points on split lines belong to the right/top side

## Quadtree Range Search

```python
def QTreeRangeSearch(T,A):
    # T is the root of a quadtree. A is the query rectangle
    R = square associated with T
    if R is subset of A:
        report all points in T
        return
    if R and A is empty:
        return
    if T stores a single point p:
        if p is in A:
            return p
        return
    for each child v of T do:
        QTreeRangeSearch(v, A)
```

Quadtrees are inefficient when the data isn’t distributed evenly.

### Analysis

What’s the height of a quadtree? Let’s consider something we call the **<u>spread factor</u>**, $S$. $\beta(S) = \frac{d_{max}}{d_{min}}$, where

- $d_{max} = \text{sidelength of R}$, 
- $d_{min} = \text{minimum distance between two points in S}​$.

Proof:

At depth $i$, the size of a square is $\frac{d_{max}}{2^i}$. The furthest distance two points can be if they are in the same region is two opposing corners. 

```text
*-----------------*
|        |        |
|        |        |
|--------|--------|
|        |        |
|        |        |
*-----------------*
```

So, the length of the diagonal $L​$ is 
$$
\begin{align}
	L &= \sqrt{2(\frac{d_{max}}{2^i})^2}
	\\&= \frac{d_{max}\sqrt 2}{2^i} \implies\text{node split, at least 2 nodes inside}
	\\&=\frac{d_{max}\sqrt 2}{2^i} \ge d_{min} \implies \frac{d_{max}\sqrt 2}{d_{min}} \ge 2^i
	\\&\implies i \le \log(\frac{d_{max}\sqrt 2}{d_{min}}) = \log(\frac{d_{max}}{d_{min}}) + \frac12
\end{align}
$$
So the height of a quadtree $h \in \Theta(log\beta(S))$.

### Summary

In summary, quadtrees are very easy to compute and handle. The only wasteful thing is space, but if points are well-distributed then there is no worry. 

# kd-Trees

Similar to quadtrees, kd-trees split the region such that (roughly) half the points are in each subtree. We continue to split, switching between $x$ and $y$ until every point is in a separate region.

To split evenly, we have to find the median value. How do we do this? We do an initial sort, then we can pick the median easily.

![KD-Tree](C:\Users\gordo\Documents\Notes\Images\KD-Tree.JPG)

## Construction of kd-trees

s

## kd-Tree Range Search

What is the runtime of this algorithm? It works similarly to that of Quadtree Range Search. When dealing with runtime here, there are a few things we actually care about. What’s our runtime based on? A few things.

- The number of points that we return (leaf nodes)
- The number of regions that contain points in the search
- The number of regions that we check but do not contain points within the search
  - Consider 1 edge of the query rectangle. how many regions can it intersect?