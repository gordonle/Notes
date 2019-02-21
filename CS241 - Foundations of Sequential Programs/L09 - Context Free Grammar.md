CS241 L09 | February 5, 2019

# Maximal Munch Algorithm

- Run DFA (without $\epsilon$-moves) until no, non-error move is available
- If in an accepting state, output the found token
- else
  - backup to most recent accepting state, using a variable to keep track of where we were
  - the input to that point is the next token
- $\epsilon$-move back to the start state

> $L = \{aa, aaa\}, w=aaaa$. The longest token in $w$ is $aaa$, with leftover that has no match. But $aa,aa$ is a valid match! This is where we have to backtrack.
>
> 
>
> In C, if we have the following code:
>
> ```C
> int a = 1;
> int b = 2;
> a+++b;
> // is this a++ +b  or a + ++b? 
> ```
>
> In fact, it is `a++ +b` since `+b` is a valid token, where `a++` is a maximal token.

## Simplified Maximal Munch

This is the same as MM. If not in an accepting state when no transitions possible, we ERROR. 

> In practice, the Simplified MM is good enough. Languages are designed to facilitate scanning by simplified MM.

For example, C++ (before 11): `vector<pair<string, int>>` has the bit-shift `>>` operator at the end!

# Context Free Grammars

Consider $\Sigma = \{(, )\} \:\: L=\{w \text{ |  $w$ is a string of balanced parentheses}\}$. Then $\epsilon, (), (()), ()(()), ()(), \cdots \in L$ and $)(, ()) \notin L$. What would our DFA look like? It would be an increasing amount of states, where increasing by 1 state would let us recognize an additional closing and opening parenthesis. 

> **Ex:** palindromes over {a, b, c}.
>
> Our grammar would look like $S \to aSa | bSb | cSc | \epsilon | a | b | c$
>
> Typically, we want to group rules, so maybe we would refactor it like so:
>
> $S \to aSa | bSb | cSc | M​$
>
> $M \to \epsilon | a | b | c​$
>
> Show $S \implies ^* abcba$. We must give the derivation. $S\implies aSa \to abSba \to abMba \to abcba$.

