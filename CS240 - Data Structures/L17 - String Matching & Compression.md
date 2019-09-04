CS240 L17 | March 21^st^, 2019

# Suffix Trees

![Suffix_Tree](C:\Users\gordo\Documents\Notes\Images\Suffix_Tree.JPG)

When searching for “bb”, we go from node `0` to `3` then we have to stop here, since index > $m$. There are no more decision points, so all keys (leaves) will have the same prefix. So, we just need to check one. Either they all match, or none of them do. 

==Augmentation==: Each internal node has a link to a leaf node, since typically we want the first occurrence of a word. 

## Runtime Summary

|             | Brute-Force |        KR         |           BM            |      DFA       |  KMP   |    Suffix-Tree    |
| :---------: | :---------: | :---------------: | :---------------------: | :------------: | :----: | :---------------: |
|  Preproc.   |      -      |      $O(m)$       |    $O(m + |\Sigma|)$    | $O(m|\Sigma|)$ | $O(m)$ | $O(n^2) \to O(n)$ |
| Search Time |   $O(mn)$   | $O(n+m)$ expected | $O(n)$ but often better |     $O(n)$     | $O(n)$ |      $O(m)$       |
| Extra Space |      -      |      $O(1)$       |    $O(m + |\Sigma|)$    | $O(m|\Sigma|)$ | $O(m)$ |      $O(n)$       |

# Compression

When creating compression algorithms, there are a few key factors that we should be considering.

1. ==Processing Speed==: the time it takes to compress and decompress (arguably least important)

2. ==Reliability==: minimizing the loss of data, error-checking data. This is very important for hard-drive signal transmissions. We have error-checking codes, where the concept is to store and send some extra information to check if the packet arrived properly. 

   - <u>Ex</u>: Transmit 7 bit characters `01101001`, `1101100`, `0101110`, .... We have a parity bit that = 1 if odd # of 1s, 0 if even # of ones. Notice how these are all 8 bits, the **last** bit is the parity bit. This is valid for the majority of the time, even though if two bits mess up we wouldn’t catch it. 

3. ==Security==: Encryption. How safe is the data?

4. ==Size==: Encoding schemes that try to minimize the size of the coded text perform *data compression*. The **<u>compression ratio</u>** is
   $$
   \frac{|C|\cdot\log|\Sigma_C|}{|S|\cdot\log|\Sigma_S|}
   $$
   where 

## Types of Data Compression

==Logical== VS ==Physical==

| Logical                                                      | Physical                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| This uses the meaning of the data and only applies to a certain domain (ie sound recordings, get rid of frequencies we can’t hear) | only knows the physical bits in the data, not the meaning behind them |

==Lossy== VS ==Lossless==

| Lossy                                                        | Lossless                               |
| ------------------------------------------------------------ | -------------------------------------- |
| Achieves better compression ratios, but the decoding is approximate; the exact source text $S$ is not recoverable | Always encodes and decodes $S$ exactly |

Since we want to focus on string compression, we will be focusing on *physical, lossless* compression algorithms. 

## Character Encodings

==Definition==: Map each character in $\Sigma_S$ to a string in the coded alphabet.
$$
E: \Sigma_S \to \Sigma^*_C
$$
For $c\in\Sigma_S$, we call $E(c)$ the *codeword* of $c$. In ***fixed-length code***, all codewords have the same length. If we are using $k$-bits, we can represent $2^k$ different patterns. Conversely, we need $\lceil\log n\rceil$ bits to represent $n$ patterns.

For example, with ASCII, we have 7 bits to encode the 128 possible characters.

In ***variable-length code***, the most frequently accessed characters will have shorter length. Morse code is variable length, and so is UTF-8 (universal Unicode) which has more than 107000 characters, using 1-4 bytes. 

> **Reading UTF-8:**
>
> Look at the first bit. If it’s `0`, read it as ASCII. Otherwise, count the number of consecutive `1`s until we reach a `0`. That determines the number of bytes in the character.

### Encoding

We want our encoding to be prefix-free, as that guarantees unique encodings and avoids ambiguity. 

> **Ex:** Encoding algorithm:
> $$
> c\in\Sigma_S \to \Sigma_C^*\\
> E = 1010\\
> S=11\\
> O=1011\\
> Y=01\\
> N=0110\\
> $$
> All codes are distinct, but if you ask a Y/N question, we get `01101011` as a response. But,
> $$
> YES=01\:1010\:11\\
> NO=0110\:1011
> $$
> This is why we need prefix-free!

In ==prefix-free code==, no code is a prefix of any other code, since we want encodings to be uniquely decodable.

### Decoding

Uniquely decodable codes corresponds to a *trie* with characters of $\Sigma_S$ only at the leaves. The codewords need no end-of-string symbol \$ if $E$ is prefix-free. Just hit a leaf node.

![Decoding_Trie](C:\Users\gordo\Documents\Notes\Images\Decoding_Trie.JPG)

Runtime is $O(|C|)$, where $C$ is a text with characters in $\Sigma_C$. We can also **encode** directly from the trie, where we start at the leaf and then prepend each node until we hit the root $\to O(|T| + |C|) = O(|\Sigma_S|+|C|)​$.

## Huffman’s Algorithm

For a given source text $S$, how do we determine the “best” trie that minimizes the length of $C$.

1. Determine the frequency of each character $c \in \Sigma$ in $S$.
2. For each $c\in\Sigma$, create a `c` (height-0 trie holding $c$)
3. Assign a weight to each trie: sum of frequencies of all letters in the trie. Initially, this is just the frequency of that character.
4. Find two tries with minimum weight.
5. Merge these two tries with a new internal node, new weight is the sum.
6. Repeat 4-5 until only 1 trie left. This is our final trie $T$. 

We should use a priority queue, prioritized by their weights. Huffman’s algorithm guarantees prefix-free encoding. 

> $S = \text{LOSSLESS}$, $\Sigma_S = \{\text{L, O, S, E}\}$, with character frequencies $L:2,O:1,S:4,E:1$. 

