CS466 Lecture 01 | May 12, 2020

## CS341 Course Overview

- Divide and conquer
- Greedy
- Dynamic Programming
- Local search (augmenting path algorithm)
- Reductions to prove NP-completeness

These are elegant, insightful and combinatorial. They are deterministic and output optimal solutions in polynomial time.

# CS466 Course Outline

This is what we will be learning:

- Problems in NP-complete:
    - Approximation algorithms (main focus)
    - Faster exact algorithms (fixed parameter algorithms)
- Problems in P:
    - Simpler and faster algorithms
    - Parallel algorithms (use multiple CPUs)
    - Distributed algorithms
    - Sublinear time/space algorithms (data streaming)
    - Online algorithms

## Modern Techniques

1. Probabilistic (1/2 of the course)
2. Linear algebraic / spectral methods (1/4 of the course)
3. Continuous optimization / linear programming (1/4 of the course)

### Probabilistic / Randomized Algorithms

Basic tools used to design these are:

- concentration inequalities (eg. Chernoff bounds)
- algebraic methods (eg. hashing)
- random walks
- probabilistic methods (eg. local lemma)

Applications:

- Graph sparsification (fast algorithms)
    - If we have a dense graph, we pick some edges based on density and probability and delete them, and we argue that the sparse graph is able to maintain certain properties of the dense graph so if we solve it on sparse it's similar to solving on dense
- Data streaming (sublinear space)
- Parallel matching (parallel algorithms)
- Network coding (distributed algorithms)
- Random sampling

### Linear Algebra / Spectral Methods

We treat the adjacency matrix as a matrix instead of just a data structure! Here are some topics:

- Basic spectral graph theory
- Cheeger's inequality, graph partitioning
- Analysis of mixing time (random sampling) of random walks
- Think of a graph as an electrical network
- Spectral (graph) sparsification
- Laplacian linear equations

### Continuous Optimization / Linear Programming

We use continuous techniques to solve discrete problems. Some topics:

- linear programming, extreme point solutions
- general framework to design exact and approximation algorithms (eg. for NP-complete)
- Duality Theorem
- multiplicative update method (online computation)

Example with 

> Max s-t flow = max set of edge disjoint s-t paths
>
> Min s-t cut = minimum set of edges to disconnect s and t
>
> Example:
>
> [ here ]
>
> Classical results:
>
> - max s-t flow = min s-t cut (**max-flow min-cut theorem**)
> - polynomial time combinatorial algorithms using augmenting paths
> - fast algorithm using advanced data structures, **Goldberg-Rao**

#### Probabilistic techniques

#### Linear Programming

We can formulate the problem as a continuous optimization program. Let's solve maximum flow in *directed graphs*. 

$x_e\in\{0,1\}$.

Learn:

- there is *always an optimal integral solution*
- LP duality theorem => max-flow min-cut theorem
- How to turn/"round" a fractional solution into an integral solution using *random walks*!

## Course Style

We will focus on main ideas and basic techniques. We won't see as many examples as possible, but we also won't see the hardest results in the areas. We'll be going for a more broad overview of current techniques (which are useful in other areas as well). 

## Course Project

Choose a topic of own interest for a deeper study. The basic requirement is to read papers and write a survey/report/summary. 

Original content is strongly encouraged;

- different proofs, simpler proofs, unified proofs
- some extensions, generalizations, variants

Up to two per group, project proposal due July 13, full report due August 14.

Each assignment is posted at minimum two weeks before the due date, recorded lectures should be available around 3-4 hours after live lecture. Slides will also be posted.

# Minimum Cut

Find a minimum cardinality subset of edges to disconnect the graph.

A simple idea: min-cut is also a min s-t cut for some s, t. So try to run min s-t cut for all s, t and return the minimum one. This solves the global min cut problem. The runtime would be $O(n^2\times maxflow)$, $maxflow = O(mn)$.

To improve, we fix an s, try all t. This takes $O(n \times maxflow)$.

In 1987, Matula used a graph search $O(m)$ to prove that after searching once, he could find edge $(u, v)$ such that this edge is on one side of the cut in some optimal solution. Knowing this, we can contract this edge to make them into a single node $(u, v) \to w$. We reduce the problem into a smaller graph with $n-1$ nodes, so we will contract at most $n$ iterations. Thus runtime is $O(mn)$.

There's a randomized algorithm by Karger that can get to $\tilde O(n^2)$ improved to $\tilde O(m)$.

## Karger's Algorithm

The idea is to choose a ***random*** edge to contract.

```
while there are more than two vertices:
	choose a uniformly random edge uv and contract it
output the edges between the remaining two vertices
```

*note*: edges delete if there are self-loops.

Since it's random, it doesn't always output the correct answer. We want to give a lower bound for the success probability. Here are some observations:

1. minimal cut corresponds to $\delta(S)$ = set of edges with one endpoint in $S$ and one endpoint is $V-S$ 
2. each cut in every intermediate graph from Karger's algorithm corresponds to a cut from the original graph

$\implies$ **<u>Corollary</u>**: min-cut in an intermediate graph $\ge$ min-cut in original graph.

**<u>Theorem</u>**: Success probability of returning a min-cut is at least $\frac2{n(n-1)}$, where $n =$ # of vertices.

**<u>Proof</u>**: Let $F\in E$ be a minimum cut, $|F| = k$. Our algorithm will succeed if we focus on $F$ and never contract them. In the end we would only have the edges in $F$ left, and we'd return it.

What is the probability that we don't choose an edge in $F$ in the $i$-th iteration?

$|F| = k$. The probability of making a mistake is $P($an edge in $F$ picked$) = \frac{|F|}{|E|}$. On the $i$-th iteration, we have exactly $n-i+1$ vertices. By observation, min-cut $\ge k$ in intermediate graph, $\implies$ min deg $\ge k$ 

> since $k$ is the minimum cut size. If there was a degree of $k-1$, then we just cut that node out which contradicts our assumption

Then # of edges $\ge \frac{(n-i+1)k}{2} \implies P($edge in $F$ is chosen$)\le \frac{k}{\frac{(n-i+1)k}{2}}=\frac2{n-i+1}$. So,

$P($succeed in all iterations$)=(1-\frac2n)(1-\frac2{n-1})...(1-\frac23) = \frac{n-2}n \cdot\frac{n-3}{n-1}\cdots\frac24\cdot\frac13=\frac2{n(n-1)}$ 

This completes the proof.

How do we boost the success probability? The idea is to repeat it $T$ many times, and return the best solution so far. What is the (failure) probablity that we haven't found the min-cut in $T$ steps? We can only fail if *all* iterations fail. 

$P($all executions fail$)\le(1-\frac2{n(n-1)})^T\le e^{-\frac{2T}{n(n-1)}}$ from the inequality $1-x\le e^{-x}$.

If we set $T=200n(n-1)\in O(n^2)$, then $e^{-\frac{2T}{n(n-1)}} = e^{-400}$. 

Total runtime = $O(n^2)\cdot O(n^2)=O(n^4)$ for each execution, where each execution takes $O(n^2)$. 

Let's improve this to $O(n^2)$.

> look at drawing in my notes

As you can see, the probability to fail at the beginning $(\frac2n)$ is much less than at the end of the contractions $(\frac23)$. So the idea is to minimize the failure probability / maximize success.

### Karger-Stein Algorithm

The idea is to repeat more in the later iterations, not the early ones, since 

$(\frac2n)(\frac2{n-1})(\frac2{n-2})\cdots(\frac23) \approx\frac14$, so then $(\frac2n)(\frac2{n-1})(\frac2{n-2})\cdots(\frac n{\sqrt2})\approx(\frac12)$. By using a tree, the success probability $\ge\frac1{\log n}$, and one run through of a tree takes $\approx O(n^2)$ so the total runtime is now $O(n^2\log n)$. 

## Combinatorial Structure

How many minimum cuts can there be in an undirected graph?

> If the graph is just  a cycle of $n$ nodes, then the # of min-cuts = $\binom n 2$.

For min-cut $S$, the surviving probability $\ge\frac2{n(n-1)} = \frac1{\binom{n}{2}}$. 

Let $S_1, S_2, ..., S_k$ be min cuts. Let event $E_i = $ cut $S_i$ survives after Karger's algorithm. Each event is disjoint, so then

$1\ge P(\cup^k_{i=1}E_i) = \sum_{i=1}^{k}P(E_i)=k\cdot\frac2{n(n-1)}\implies k\le \frac n{n(n-1)}$

## Discussions

The algorithm can be extended to give a $n^{O(k)}$ 



Read chapter 1 and 2 of Mitzenmacher and Upfal.