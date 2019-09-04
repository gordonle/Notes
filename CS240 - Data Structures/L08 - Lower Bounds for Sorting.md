CS240 L08 | January 31, 2019

# `quick-sort3`

$\Theta(n \log n)​$ worst-case, *not* $\Theta(n^2)​$. Here, we look for the **median of medians** to get our pivot. So, given an array $A​$ of size $n​$,

1. Group elements into blocks of 5

2. Find **Median** of each block

3. Then take the **Median of Medians** as pivot

   $\to$ this guarantees that the pivot will be “close enough” to the middle. 

   $\to$ Steps 1. and 2. guarantee that there will be keys $\le$ pivot & $\ge$ pivot.

# Lower Bounds for Sorting

|       Sort       |    Running time    |   Analysis   |
| :--------------: | :----------------: | :----------: |
| `selection-sort` |   $\Theta(n^2)$    |  worst-case  |
| `insertion-sort` |   $\Theta(n^2)$    |  worst-case  |
|   `merge-sort`   | $\Theta(n \log n)$ |  worst-case  |
|   `heap-sort`    | $\Theta(n \log n)$ |  worst-case  |
|  `quick-sort1`   | $\Theta(n \log n)$ | average-case |
|  `quick-sort2`   | $\Theta(n \log n)$ |   expected   |
|  `quick-sort3`   | $\Theta(n \log n)$ |  worst-case  |

**<u>Question</u>**: Can one do better than $\Theta(n \log n)$ running time?

**<u>Answer</u>**: Yes and no! ***It depends on what we allow***. No, since comparison-based sorting lower bound is  $O(n\log n)$. Yes, since non-comparison-based sorting can achieve $O(n)$, under certain restrictions.

```
quick-sort3:
```

> BFRPT: Blum, Floyd, Rivest, Pratt, and Tarjan. Mathematicians that have done important work. 

## The Comparison Model

In this model, data can only be accessed in two ways:

1. comparing two elements
2. moving elements around (ie. copying, swapping)

This allows us to make minimal assumptions concerning the items we are sorting. We count the number of above operation to analyze the running time. So far, we’ve only seen algorithms that belong in the comparison model.

We are typically just considering the boolean operators $\lt, \gt, =$. From this, we make our **decision tree**. 

> Ex: $n=3$, $[x_1, x_2, x_3] \in \{[3,2,1], [2,1,3],[1,2,3],[3,1,2],[2,3,1],[1,3,2]\}$ . Our decision tree is as follows:
>
> <svg width="700" height="450" version="1.1" xmlns="http://www.w3.org/2000/svg">
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="367.5" cy="103.5" rx="30" ry="30"/>
> 	<text x="344.5" y="109.5" font-family="Times New Roman" font-size="20">x1:x2</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="235.5" cy="178.5" rx="30" ry="30"/>
> 	<text x="212.5" y="184.5" font-family="Times New Roman" font-size="20">x3:x2</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="490.5" cy="178.5" rx="30" ry="30"/>
> 	<text x="467.5" y="184.5" font-family="Times New Roman" font-size="20">x1:x3</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="141.5" cy="279.5" rx="30" ry="30"/>
> 	<text x="111.5" y="285.5" font-family="Times New Roman" font-size="20">x3x2x1</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="313.5" cy="279.5" rx="30" ry="30"/>
> 	<text x="290.5" y="285.5" font-family="Times New Roman" font-size="20">x1:x3</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="415.5" cy="279.5" rx="30" ry="30"/>
> 	<text x="385.5" y="285.5" font-family="Times New Roman" font-size="20">x3x1x2</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="573.5" cy="279.5" rx="30" ry="30"/>
> 	<text x="550.5" y="285.5" font-family="Times New Roman" font-size="20">x2:x3</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="490.5" cy="393.5" rx="30" ry="30"/>
> 	<text x="460.5" y="399.5" font-family="Times New Roman" font-size="20">x1x3x2</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="220.5" cy="394.5" rx="30" ry="30"/>
> 	<text x="190.5" y="400.5" font-family="Times New Roman" font-size="20">x2x1x3</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="391.5" cy="394.5" rx="30" ry="30"/>
> 	<text x="361.5" y="400.5" font-family="Times New Roman" font-size="20">x2x3x1</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="652.5" cy="387.5" rx="30" ry="30"/>
> 	<text x="622.5" y="393.5" font-family="Times New Roman" font-size="20">x1x2x3</text>
> 	<polygon stroke="black" stroke-width="1" points="341.416,118.32 261.584,163.68"/>
> 	<polygon fill="black" stroke-width="1" points="261.584,163.68 271.009,164.075 266.069,155.38"/>
> 	<text x="285.5" y="131.5" font-family="Times New Roman" font-size="20">&lt;</text>
> 	<polygon stroke="black" stroke-width="1" points="215.061,200.461 161.939,257.539"/>
> 	<polygon fill="black" stroke-width="1" points="161.939,257.539 171.049,255.09 163.729,248.277"/>
> 	<text x="171.5" y="220.5" font-family="Times New Roman" font-size="20">&lt;</text>
> 	<polygon stroke="black" stroke-width="1" points="253.837,202.244 295.163,255.756"/>
> 	<polygon fill="black" stroke-width="1" points="295.163,255.756 294.231,246.369 286.316,252.481"/>
> 	<text x="257.5" y="249.5" font-family="Times New Roman" font-size="20">&gt;</text>
> 	<polygon stroke="black" stroke-width="1" points="393.114,119.118 464.886,162.882"/>
> 	<polygon fill="black" stroke-width="1" points="464.886,162.882 460.659,154.448 455.453,162.986"/>
> 	<text x="412.5" y="162.5" font-family="Times New Roman" font-size="20">&gt;</text>
> 	<polygon stroke="black" stroke-width="1" points="472.615,202.586 433.385,255.414"/>
> 	<polygon fill="black" stroke-width="1" points="433.385,255.414 442.169,251.972 434.14,246.011"/>
> 	<text x="435.5" y="221.5" font-family="Times New Roman" font-size="20">&lt;</text>
> 	<polygon stroke="black" stroke-width="1" points="509.547,201.678 554.453,256.322"/>
> 	<polygon fill="black" stroke-width="1" points="554.453,256.322 553.237,246.967 545.511,253.316"/>
> 	<text x="515.5" y="249.5" font-family="Times New Roman" font-size="20">&gt;</text>
> 	<polygon stroke="black" stroke-width="1" points="294.636,302.827 239.364,371.173"/>
> 	<polygon fill="black" stroke-width="1" points="239.364,371.173 248.283,368.097 240.507,361.809"/>
> 	<text x="250.5" y="328.5" font-family="Times New Roman" font-size="20">&lt;</text>
> 	<polygon stroke="black" stroke-width="1" points="330.34,304.328 374.66,369.672"/>
> 	<polygon fill="black" stroke-width="1" points="374.66,369.672 374.308,360.245 366.032,365.858"/>
> 	<text x="335.5" y="356.5" font-family="Times New Roman" font-size="20">&gt;</text>
> 	<polygon stroke="black" stroke-width="1" points="555.842,303.753 508.158,369.247"/>
> 	<polygon fill="black" stroke-width="1" points="508.158,369.247 516.909,365.723 508.824,359.837"/>
> 	<text x="514.5" y="328.5" font-family="Times New Roman" font-size="20">&lt;</text>
> 	<polygon stroke="black" stroke-width="1" points="591.212,303.714 634.788,363.286"/>
> 	<polygon fill="black" stroke-width="1" points="634.788,363.286 634.101,353.878 626.03,359.782"/>
> 	<text x="595.5" y="353.5" font-family="Times New Roman" font-size="20">&gt;</text>
> </svg>

In general, with $n$ items, there are $n!$ leaves (possible outcomes). Every internal node has two children (comparison), and thus we need $n! - 1$ internal nodes. Internally, our sorting algorithms simulate this tree, since otherwise we would be taking $n!-1$ space if we actually created it. We want to go down just *one* of these paths. So how does this lead to $n\log n$?

We can then say that the height $h \ge \log(n!) \in \Omega(n \log n)$. This is because 
$$
\begin{align}
\log(n!) &= \log(n) + \log(n-1)+\log(n-2) + \cdots + \log(1)
\\ &\ge \log(n) + \log(n-1) + \cdots + \log(\frac n2)
\\ &\ge \log(\frac n2) + \cdots + \log(\frac n2) = \frac n2\log(\frac n2) = \frac n2\log n - \frac n2 \log2 \in \Omega(n \log n)
\end{align}
$$
We cut out half the terms, then we use the smallest value ($\frac n2$) to continue to build the inequality.

## Non-Comparison-Based Sorting

Assumptions:

1. keys are all numbers in base $R$ (radix)

   $R = 2, 10, 128, 156​$ are the most common.

2. all keys have the same number of $m$ digits

   $\to$ we can achieve this by padding with leadings 0s.

3. Can sort based on individual digits.

   1. How do we sort 1-digit numbers?
   2. How do we sort multi-digit numbers?

### Single-Digit Bucket Sort

> Ex: $R = 4$, $A =[123, 230, 021, 320, 210, 232, 101]$
>
> | B    | B[0] | B[1] | B[2] | B[3] |
> | ---- | ---- | ---- | ---- | ---- |
> |      | 230  | 021  | 232  | 123  |
> |      | 320  | 101  |      |      |
> |      | 210  |      |      |      |
>
> Then we know that items ending in 0 are smallest. So $A = [230, 320, 210, 021, 101, 232, 123]$.

With this `bucket-sort`, all or elements maintain their original order in each list. We create a “bucket” for each possible digit, then copy item with digit $i$ into bucket $B[i]$. Finally, copy the elements back into $A$.

```python
bucket-sort(A,d):
#A: array of size n, contains numbers with digits {0,..., R - 1}
#d: index of digit by which we wish to sort
	initialize array B[0,...,R-1] of empty lists
    for i = 0 to n-1 do:
        append A[i] at the end of B[dth digit of A[i]]
    i = 0
    for j = 0 to R - 1 do:
        while B[j] is non-empty do:
            move first element of B[j] to A[i++]
```

Run time of $\Theta(n + R)$, auxiliary space $\Theta(n)$.

### Count Sort

Notice that `bucket-sort` wastes a lot of space - we know where each number in B goes, so we don’t actually need the lists, just the count of how many are in each.

> **Ex**: Input: $A = [4, 5, 7, 0, 5, 5, 10]$. In this case, we assume that $R=11$. 
>
> We then create an array $count[]$ with 11 elements, all initialized to 0. Now we iterate through $A$, and we count each. Then we end up with $count = [1, 0, 0, 0, 1, 3, 0, 1, 0, 0, 1]$. Now, we create an array $idx[]$ that lets us know when each type will start in the sorted array (ie. 7 starts at the $1+1+3=5$^th^ index). So, $idx = [0,1,1,1,1,2,5,5,6,6,6]$ . We have now stored the *starting index* for each item group. 
>
> From here, we need to create an auxiliary array that we insert the items into, then copy this array back into $A$. 

When creating the auxiliary array, consider the following pseudocode:

```python
aux = array of size n
for i = 0 to n - 1 do:
    aux[idx[dth digit of A[i]]] = A[i]
    increment idx[dth digit of A[i]]
```

We increment each time we add since we know we’ve already added an item in group “d^th^ digit of $A[i]$”, so the next one would be located at one index later.

### MSD-Radix Sort

*Most Significant Digit Radix Sort*. Partition using `count-sort` and sort from left to right. The disadvantage is that it takes many recursions to complete.

> **Ex:** $A = [ 829, 331, 457, 330, 436, 720,355], R = 10$
>
> We then partition them into lists based on the *first digit* with `count-sort`. Buckets: $[331, 330,355],$
>
> | B[3] | [331, 330, 355] |
> | ---- | --------------- |
> | B[4] | [457, 436]      |
> | B[7] | [720]           |
> | B[8] | [829]           |
>
> Now we recurse and count-sort each bucket by the *second*, then *third*, then *fourth*, etc. By the end, each bucket will be sorted through each digit, and we can append them all to complete the sort.

This is beneficial because we don’t care about the number of digits! For example, if we want to sort words into a dictionary, we can sort all the A’s, then B’s, then C’s, etc, regardless of the length of each word.

### LSD-Radix Sort

```python
LSD-radix-sort(A):
# A: array of size n containing m-digit radix-R numbers
    for d = m down to 1 do:
        key-indexed-count-sort(A, d)
```

A is then sorted with respect to digits $d, ..., m$ of each entry. Time cost is $\Theta(m(n + R))$, auxiliary space $\Theta(n+R)$. With this, we avoid the recursion problem we had in MSD-Radix sort. $m = \text{# of digits}, n = \text{size of array}, R=\text{radix}$, and usually $n >> R$. But what if $n = R$? Then we have linear time.





