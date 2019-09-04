CS240 L15 | March 14^th^, 2019

# Range Trees

## Range Search

This is a two stage process, where as we search through the tree we get a series of `boundary` nodes,  `outside` nodes and `inside` nodes. Each `boundary` node has two children - one `inside` and one `outside`.  `outside` nodes are, aptly named, outside of our search (the values are either greater than or less than). We only need to continue to iterate through the `inside` nodes. There are $O(\log n)$ of these nodes, and we have to run `RangeSearch` on all of them, taking $O(\log n + s_i)$ each. 
$$
\begin{align}
	&\implies O((\log n)^2 + s) \text{ , where $s$ is the number of points reported}
	\\ &\implies O(\log n + s) \text{ (reduced)}
\end{align}
$$
When does $(\log n)^i$ become dominant over $n^j$? Comparing usages with kd-trees. 

# Range Query Data Structures Summary

| Type        | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| Quadtrees   | Simple, works well only if points are evenly distributed, and wastes space for higher dimensions |
| kd-trees    | Linear space, query-time of $O(\sqrt{n})$, insert/deletes destroy balance, and care is needed for duplicates |
| range trees | fastest range search of $O(\log^2 n)$, but wastes space and insert/delete is more complicated |

# String Matching 

We’ve got a huge amount of text $T[0\cdots n-1]$, and we want to search for a string/pattern $P[0\cdots m-1]$ in that text! We want to return the first $i$ such that $P[j] = T[i+j]$ for $0 \le j\le m-1$. 

Pattern matching algorithms consist of ***guesses*** and ***checks***. A ==guess== or ==shift== is a position $i$ such that $P$ might start at $T[i]$. A ==check== of a guess is a single position $0\le j < m$ where we compare $T[i+j] = P[j]$. We then must perform $m$ checks of a single correct guess, but fewer for incorrect guesses. 

## Brute Force Idea

Iterate through every character in $T$ and then check every successive character until there is a match or there isn’t. The worst possible input would be $P=a^{m-1}b$ and $T=a^n$. The worst case performance is then $\Theta((n-m-1) * m) \in \Theta(mn)$. There are better algorithms, that involve preprocessing $P$ and $T$.

## Karp-Rabin Fingerprint Algorithm

The idea here is to use ==hashing== to eliminate guesses. So we compute the hash function for each guess, then compare with the pattern hash. This is quite inefficient if we have to continue to recompute the hash value for each iteration every shift, taking $\Theta(mn)$ time. Instead, we can use the previous hash (==fingerprint==) to compute the next hash. We can do each of this in $O(1)$ time. (Look at end of hashing section to see how we should approach doing this for characters - multiply by a radix $R​$ to a power and mod).

**NOTE**: remember to check, at the end, if the string matches by doing `strcmp`. Hashing may result in collisions, so using a large prime $M$ to mod can help but not guarantee no collisions. 

The expected running time is then $O(m + n)$, and worst case is $\Theta(mn)$ which happens that we get a collision at every step, and only the last character during `strcmp` is different. This is unbelievably unlikely. 

This is a randomized algorithm, size we’re randomly picking our large prime $M$. ==Las Vegas== we want to guarantee correctness, but it might sacrifice some runtime $(\Theta(mn))$. ==Monte Carlo== algorithms enjoy to have a little more risk, minimizing the chances that we get an error. In this, then we just don’t do the naïve `strcmp` at the end $(\Theta(m + n))$. Sacrifices some correctness for a faster runtime. 

## Boyer-Moore Algorithm

It’s brute force but with two modifications:

1. ==Reverse-order searching==: Compare $P$ with a guess moving *backwards*
2. ==Bad character jumps==: When a mismatch occurs, then eliminate guesses where $P$ does not agree with this character of $T$

In practice, large parts of $T$ will not be looked at. This is known as the “bad character” heuristic. 

We’re hoping that there’s a mismatch at the end character, and that this character is not in $P$ at all. So we just shift by the whole size of remaining text in $P$. This takes advantage of the way in which the English language is, since each word usually has only a few unique characters. 

![Boyer-Moore](C:\Users\gordo\Documents\Notes\Images\Boyer-Moore.JPG)

We will create a last-occurrence array. 

|     c      | L(c) |
| :--------: | :--: |
|     p      |  0   |
|     a      |  1   |
|     t      |  2   |
|     i      |  5   |
|     k      |  4   |
| all others |  -1  |

This array is actually of size $|\Sigma|$. So it takes $\Theta(|\Sigma|)$ to construct it. Worst case runtime is $\Theta(mn + |\Sigma|)$ when using this “bad character” heuristic. In practice, around 25% of the text is probed. 

## Finite Automata

Just use a DFA, NFA, etc. 

