CS240 L19 | March 28^th^, 2019

# Lempel-Ziv-Welch

This method of compression takes advantage of the fact that certain *substrings* are more common than others. There are two main ingredients to this:

1. Take advantage of such substrings *without* needing to know beforehand what they are
2. Use ==adaptive encoding==:
   - There is a fixed initial dictionary $D_0$ (ie. ASCII)
   - For $i \ge 0, D_i$ is used to determine the $i$th output character
   - After writing the $i$th character to output, both encoder and decoder update $D_i$ to $D_{i+1}$. 

Note that both the *encoder* and the *decoder* must know how our dictionary changes.

**LZW** is a family of adaptive compression algorithms! Each character in the coded text $C$ either refers to a single character in $\Sigma_S$, or a *substring* of $S$ that both the encoder and decoder have already seen. Let’s look at the encoding steps specifically:

## Encoding

We start with a dictionary $D_0$ for $|\Sigma_S|$. For English, $\Sigma_S$ = ASCII, then this uses codenumbers 0, ... , 127. 

Every step then adds to the dictionary a multi-character string, using codenumbers 128, 129, ... . Now, we encode it.

1. Store the current $D_i$ as a trie. 
2. Parse the trie to find the longest prefix $x$ already in $D_i$ so that all of $x$ can be encoded with one number
3. Add to the dictionary the *<u>prefix that would have been useful</u>*:
   - add $xK$ where $K$ is the character that follows $x$ in $S$. 
4. This creates one child in the trie at the leaf where we stopped.

The output is simply a list of numbers, which is usually converted to bit-string with fixed-width encoding on 12 bits. Thus we are limited to 4096 patterns (or codenumbers).

![LZW-Encoding](C:\Users\gordo\Documents\Notes\Images\LZW-Encoding.JPG)

## Decoding

When encoding, after using encoding $B$ we lookahead 1 character in $S$ and add $BA$. So we’ve found a path in the trie and we extend the path used by 1 more node. 

When <u>decoding</u>, we are one step behind. Most available codes are easily looked up in the dictionary, and we add new codes mimicking the encoder.

![LZW-Decoding](C:\Users\gordo\Documents\Notes\Images\LZW-Decoding.JPG)

==Special Case==: When we need to get code that would have been added to the dictionary, but the decoder is 1 step behind. Here, we add the previous pattern used + first character of the current pattern. 

So, say we have that 84: BAC, 132: ANB, 133: ???. If we just used 84, then are asked to use 133, we get BAC==B==.

## Dictionary is full

What if the dictionary fills up? We have at most $2^{12}$ different codenumbers, or 4096. There are a few options we can try

1. Stop adding patterns
   - this is fast, but is bad if the data changes
2. Discard the least frequently used entry and add the new pattern here
   - this is a lot to keep track of
3. Make the dictionary larger
   - if we want to do this, we need to increase the number of bits used per encoding
   - we’ll have to recognize when the fixed-width changes from 12 to say 14 bits
4. Overwrite the dictionary
   - start at the beginning again

==NOTE==: Remember that whatever scheme we pick for the encoder, the decoder must also work the same way. If the encoder is convoluted and complicated, the decoder will be just as convoluted and complicated. 

# bzip2

To achieve an even better compression, bzip2 uses ==*text transform*==. This changes the input into a different text that is not necessarily shorter, but has other desirable qualities. 

> **Ex**: 
>
> Input = “the quick brown fox jumped over the lazy dog”
>
> Sorted(transformed) = “________abcddeeefghhijklnoooopqrsttuvwxyz”
>
> The sorted string is much easier to compress, but we can’t uniquely decode it back into our input.

## Move-to-Front transform

We take advantage of *locality* in the data. If we see a character now, we’ll probably see it again soon. With our dictionary of size $|\Sigma_S|$, we simply move the accessed character’s index to the front, shifting everything back. 

> **Ex**: 
>
> Source $S$ = “MISSISSIPPI”
>
> Coded $C$ = 12 9 18 0 1 1 0 1 16 0 1

What does a run in $S$ encode to in $C$?

- This will encode to “# 0 0 0 0 0 ....”

What does a run in $C$ mean about the source $S$?

- A common substring!

## Burrows-Wheeler Transform

This is a ==*block* compression method== that transforms the source text to a coded text with the same letters, just in different order. The coded text *will be more easily compressible* with MTF. 

We need to add the *end-of-word* character \$ that occurs nowhere else in the string. We must perform ==cyclic shifts== on $S$. Once we’ve calculated all of these, sort them! Once sorted, take the last column.

> **Ex**: $S = \text{dalek\$}$. Then the cyclic shifts are as follows:
> $$
> \text{dalek\$}\\
> \text{alek\$d}\\
> \text{lek\$da}\\
> \text{ek\$dal}\\
> \text{k\$dale}\\
> \text{\$dalek}\\
> $$
> Now let’s sort it:
> $$
> \text{\$dalek}\\
> \text{alek\$d}\\
> \text{dalek\$}\\
> \text{ek\$dal}\\
> \text{k\$dale}\\
> \text{lek\$da}\\
> $$
> So the coded string is $C = \text{kd\$lea}​$ 

So how would we decode this? If we know $C$, then we know the last column *and* the first column. We disambiguate by row-index, so we start from $\$$ and recover $S$.

>$C = \text{kd\$lea}$, so the first column is just this sorted! 
>
>|  0   |  1   |  2   |  3   |  4   |  5   |
>| :--: | :--: | :--: | :--: | :--: | :--: |
>| $, 2 |      |      |      |      | k, 0 |
>| a, 5 |      |      |      |      | d, 1 |
>| e, 4 |      |      |      |      | $, 2 |
>| d, 1 |      |      |      |      | l, 3 |
>| k, 0 |      |      |      |      | e, 4 |
>| l, 3 |      |      |      |      | a, 5 |
>
>So when decoding, we start at $ and recover the rest, using the indices that we’ve assigned. We don’t care what is inside the rest of the table. 
>
>So we get $\text{2 1 5 3 4 0}$, which translates to $\text{dalek\$}​$.

What’s the cost of this heuristic?

**Encoding:** $O(n^2)$ when using MSD radix sort. 

**Decoding**: can do counting sort in $O(n)$ time since dictionary is of fixed length. 

