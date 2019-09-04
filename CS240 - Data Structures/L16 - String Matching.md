CS240 L16 | March 19^th^, 2019

# String Matching with Knuth-Morris-Pratt

Text $T$ has size $n$, pattern $P$ has size $m$. The goal here is an $O(n)$ runtime in worst case. With **Knuth-Morris-Pratt** ==KMP==, we compare the pattern, left to right. When a mismatch occurs, we shift the pattern “*intelligently*”, which is similar to the mismatch transitions in a ==DFA==. 

**<u>Loop invariant</u>**: if checking index $j$ of $P$ with $c$ of $T$, then we’re checking that $P[0..j-1] = T[i-j..i-1]$. Note that the previous characters of $P$ also match $T$. We *never* move backwards in the text, guaranteeing at worst case $O(n)$.

Instead of looking at the mismatch character, as done in DFAs, we make our decision on where to move the pattern that doesn’t involve the next character. The shifting is then only based on the pattern, so we have “failure” transitions.

Formally, this is not a DFA, but it still is deterministic.

| Type | Methodology                                                  |
| ---- | ------------------------------------------------------------ |
| DFA  | Mismatch on char of text, then based on this char we decide where to go next |
| KMP  | Failure transitions do NOT consider the mismatched character. The shift is only based on $P$. |

With DFAs, we need transitions on all characters in the alphabet, but for KMP, each state has $m$ transitions at most. We can store the *failure-function*, or the *failure-array* in an array $F[0..m-1]$ (takes $O(m)$ time. When a mismatch occurs at $l$, we shift by the longest prefix of the pattern that is also a suffix of the pattern.  

> If a mismatch occurs at $j = 5$ of $P$, we lookup $F[4]$ and continue checking pattern at index $3$. We’ve shifted the pattern right by 2. 

We’re using DP to build our failure array. 

```python
def failureArray(P):
    # P is a string of length m (our pattern)
    F <- array of size m
    F[0] = 0
    i = 1
    j = 0
    while i < m:
        if P[i] == P[j]:
            j = j + 1
            F[i] = j
            i = i + 1
        else if j > 0:
            j = F[j-1]
        else:
            F[i] = 0
            i = i + 1
    return F
```

# String Matching with Suffix Tries

This is a compressed trie, focusing on suffixes and prefixes. 

