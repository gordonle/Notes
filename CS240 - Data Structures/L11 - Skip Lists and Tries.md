CS240 L11 | February 14^th^

# Skip Lists

## Delete

When deleting an element $k$ from our skip list $S$, we first search for $k$ to get stack $P$. This will contain all predecessors $p_0, p_1, ..., p_h$ of $k$ in lists $S_0, \cdots, S_h$. Then, for each $0 \le j \le h$, if $key(after(p_j)) = k $ then remove $after(p_j)$ from list $S_j$. Basically, $P$ holds the addresses to the nodes *before* value $k$ in each list down to the bottom, so we check if the next value of each address in $P$ is equal to $k$. If it is, we delete the next node. If not, look at the next address in $P$. 

After this, we check to see if there are more than one list in $S$ that contains only the special start and end keys. Remove all but one of them.

For example,

![Skip_Lists_Delete](C:\Users\gordo\Documents\Notes\Images\Skip_Lists_Delete.JPG)

Here, we’ve found key 65, and our $P$ stack has the nodes outlined in ==red==. At the end, we’ll need to remove the topmost list to make sure we only have one list that contains only the two special start and end keys. The resulting skip list looks like this:

![Skip_Lists_Delete_After](C:\Users\gordo\Documents\Notes\Images\Skip_Lists_Delete_After.JPG)

## Summary of Skip Lists

The ==expected space usage== is $O(n)$. The ==expected height== is $O(\log n)$. A skip list with $n$ items has at most $3\log n $ height with probability at least $1 - \frac 1{n^2}$.

**Note:** for all operations, it is crucial that we consider:

- how often do we ==drop down== (execute $p \gets below(p)$)?
- how often do we ==scan forwards== (execute $p \gets after(p)$)?

`skip-search`: $O(\log n)$ expected time, # of drop-downs = height, expected # of scan-forwards is $\le 2$ in each level

`skip-insert`: $O(\log n)$ expected time, since we just `search` then insert at each level we need to

`skip-delete`: $O(\log n)$ expected time, since we `search` then delete. 

In practice, ==Skip Lists== are fast and simple to implement. 

# Re-ordering Items

Recall that using the unordered array implementation of the ADT Dictionary results in `search`: $\Theta(n)$, `insert`: $\Theta(1)$, `delete`: $\Theta(1)$ (after a search). 

If the access of elements is equally likely, there’s no optimization here. But, if accessed items follow a probability distribution, we can make `search` more effective. The intuition here is that the frequently accessed items should be at the front of our array. The ==expected search cost== would then be $probability \times index$. 

## Optimal Static Ordering

Static ordering works when ==we know the access probabilities ahead of time==.

| Key                 | A            | B            | C            | D               | E            |
| ------------------- | ------------ | ------------ | ------------ | --------------- | ------------ |
| Frequency of access | 2            | 8            | 1            | 10              | 5            |
| Access Probability  | $\frac2{26}$ | $\frac8{26}$ | $\frac1{26}$ | $\frac{10}{26}$ | $\frac5{26}$ |

So if we kept order $ABCDE$, the expected access cost is:
$$
\frac2{26} \cdot1+\frac8{26}\cdot2+\frac1{26}\cdot3+\frac{10}{26}\cdot4+\frac5{26}\cdot5 = \frac{86}{26} \approx 3.31
$$
But, if we reordered it by its access probability, we get $DBEAC$, with an expected access cost of:
$$
\frac{10}{26} \cdot1+\frac8{26}\cdot2+\frac5{26}\cdot3+\frac2{26}\cdot4+\frac1{26}\cdot5 = \frac{66}{26} \approx 2.54
$$
The claim here is that if we sort items by non-increasing access probability, this minimized the expected access cost. To prove this, simply consider any other ordering. If we exchange two items that are out of order, the total expected access cost will decrease.

## Dynamic Ordering

What if we don’t know the access probabilities? We can use the rule of *==temporal locality==*, which states that a recently accessed item will soon be accessed again. So, once we access an element, we **move it to the front**!

There are two main ways that we can approach this:

| Method              | Description                                                  | Performance                                                  |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| MTF (Move-To-Front) | Upon a successful search, move the accessed item to the front of the list | Works well in practice, and we can show that it’s “2-competitive”, meaning no more than twice as bad as the optimal “offline” ordering |
| Transpose           | Upon a successful search, swap the accessed item with the item immediately preceding it. | Does not adapt well to changing access patterns              |

In both of these approaches, when inserting, we simply insert to the **front** of the list. These can also both be implemented with arrays or linked lists. 

# Interpolation Search

When performing `binary-search`, we check the middle element of our range, then either go left or right, depending on if our value is lesser or greater than the value found at the middle. This results in a $\Theta(\log n)$ search. Can we improve this? With `interpolation-search`, we look at the values found at the ends of our range, and *predict* where the value we want could be.

So when searching for value $k$, instead of comparing at index $m = \lfloor \frac{l+r}2\rfloor = l +\lfloor\frac12(r-l)\rfloor$, we compare at index $m = l+\lfloor \frac{k-A[l]}{A[r]-A[l]}(r-l)\rfloor$. If this is not our value, we either shift our left side $l$ to $m+1$, or our right side $r$ to $m-1$.

This works well if our keys are ==uniformly distributed==, and we can show that the array in which we search has expected size of $\sqrt{n}$. Our recurrence relation is
$$
T^{\text{(avg)}}(n) = T^{\text{(avg)}}(\sqrt n) + \Theta(1) \in \Theta(\log(\log n))
$$
But, in **worst-case**, performance is of $\Theta(n)$.

When coding this, it’s very similar to `binary-search` except we compare at the interpolated index, and a few extra tests are required to avoid crashing with $A[l] = A[r]$. 

```python
def interpolationSearch(A,n,k):
    l, r = 0, n-1
    while l < r and A[l] != A[r] and k >= A[l] and k <= A[r]:
        m = interpolatedIndex(A,k,l,r)
        if A[m] < k:
            l = m + 1
        elif A[m] > k:
            r = m - 1
        else:
            return m
    if k == A[l]:
        return l
    else: 
        return "not found, but would be between l and l-1"
```

# Tries

A **trie** is a dictionary for binary strings, a.k.a. a ==Radix Tree==. It’s a tree based on **bitwise comparisons**, and works similar to `radix-sort` in the sense that we use individual bits, not the whole key. For a string $S[0...n-1]$,

| Prefix                                                  | Prefix-Free                                                  |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| A substring $S[0..i]$ of $S$ for some $0 \le i \le n-1$ | No pair of binary strings in the dictionary where one is the prefix of the other |

Our assumption here is that our dictionary is ==prefix-free==. This is satisfied when all strings

- have the **same length**
- end with a special character, say “$”

The **structure** of a trie is composed of items (or keys) that are only stored in leaf nodes. Each edge is then labelled with a corresponding bit, or $ to indicate the end of the string. For example,

![Trie](C:\Users\gordo\Documents\Notes\Images\Trie.JPG)

## Search

Let’s call `trie-search(v, d, x)`, where $v$ is our current node, $d$ is the level of $v$, and $x$ is the word to search for. We start at the root with the most significant bit of $x$, and follow the route that leads to the current bit in $x$. If that doesn’t exist, return failure.

```python
def trieSearch(v,d,x):
    if v.leaf():
        return v # v must store x
   	c = child of v labelled with x[d]
    if c is None:
        return "Not found"
   	else:
        return trieSearch(c, d+1, x)
```

With an AVL Tree, the search would take $O(\log n)$ time (# of keys). With a trie, it takes ==$O(|x|)$==, where $|x|$ is the length of our binary string. 

`trie-insert`: we search for $x$, and this should return a failure. Then add the necessary nodes to create a route for $x$.

`trie-delete`: search for $x​$ to get $v​$, then delete all ancestors of $v​$ until an ancestor with more than one child.

## Variations

### No Leaf Labels

Since the keys are stored implicitly by the path taken to get there, we don’t store the end value of our keys. This halves the amount of space needed!

### Remove Chains to Labels

We stop adding nodes to the trie as soon as a key is unique. This saves space if there are only a few bitstrings that are long.

![Trie_Var2](C:\Users\gordo\Documents\Notes\Images\Trie_Var2.JPG)



### Allow Proper Prefixes

Instead of keeping track of a `0` and `1` child, we define these implicitly with `left` and `right` children. The end of word is also removed and is replaced by a ==flag==. This is more space efficient, and creates a binary tree.

![Trie_Var3](C:\Users\gordo\Documents\Notes\Images\Trie_Var3.JPG)

## Patricia (Compressed) Tries

<u>PATRICIA</u>: Practical Algorithm To Retrieve Information Coded In Alphanumeric. Here, we only keep track of nodes with *more than one child*. Each node instead stores an ==index==, indicating the bit to be tested.

![Trie_Patricia](C:\Users\gordo\Documents\Notes\Images\Trie_Patricia.JPG)



