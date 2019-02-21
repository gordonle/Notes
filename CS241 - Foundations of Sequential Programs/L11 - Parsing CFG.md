CS241 | February 14^th^

# Parsing Context Free Grammars

Given grammar $G$, start symbol $s$, input string $w$ (ie. a sequence of tokens from source code), find the steps that make $s \to \cdots \to w$, or ==ERROR==. How do we do this?

1. Top-down (forwards)
   - Start at $s​$, figure out how to derive $w​$.
2. Bottom-up (backwards)
   - Start at $w$, figure out rules that could have produced $w$, work backwards until we arrive at $s$.

Our initial approach is to **brute-force** it. This takes a lot of time, but we’re going to try it first anyways.

## Top-Down

Start at $s$, and apply our rules to derive $w​$.
$$
s \to \alpha_1 \to \alpha_2 \to \cdots \to \alpha_k \to w
$$
where each $\alpha_i$ are intermediate steps. We use a `stack` to store intermediates in reverse, matched against the *chars* in $w$. Let’s define our ==invariant==: consumed input + reverse (stack contents) = $\alpha_i$. When the top of the stack is a ==terminal==, we pop and match it with our input. When the top of the stack is a non-terminal $A$, we then pop $A$ and push $\alpha^R$ (reverse of $\alpha$) where $A \to \alpha$ is a rule in the grammar. We accept when the input and the stack are **both empty**. 

> **Ex:** Here’s our grammar.
> $$
> \begin{align}
> s &\to AyB
> \\ A &\to ab
> \\ A &\to cd
> \\ B &\to z
> \\ B &\to wx
> \end{align}
> $$
> We “augment the grammar” by adding new symbols $\vdash, \dashv$. New rule: $s’ \to \:\: \vdash s \dashv$.
>
> So now suppose that $w = \:\vdash \text{abywx} \dashv$.
>
> | Stack $\to$                                            | Read                         | Unread                       | Action                                                       |
> | ------------------------------------------------------ | ---------------------------- | ---------------------------- | ------------------------------------------------------------ |
> | $s’$                                                   | $\epsilon$                   | $\vdash \text{abywx} \dashv$ | Pop $s’$, push $\dashv\text{ , s, } \vdash$ (reverse of RHS of Rule) |
> | $\dashv\text{ s } \vdash$ (  $\vdash$ is top of stack) | $\epsilon$                   | $\vdash \text{abywx} \dashv$ | Match $\vdash$.                                              |
> | $\dashv\text{ s }$                                     | $\vdash$                     | $\text{abywx} \dashv$        | Pop $s$, push our string in reverse order $\text{B, y, A}$   |
> | $\dashv \text{ B y A}$ (from grammar)                  | $\vdash$                     | $\text{abywx} \dashv$        | Pop $A$, push $\text{b, a}$                                  |
> | $\dashv \text{ B y b a}$                               | $\vdash$                     | $\text{abywx} \dashv$        | Match $a$                                                    |
> | $\dashv \text{ B y b}$                                 | $\vdash \text{ a}$           | $\text{bywx } \dashv$        | Match $b$                                                    |
> | $\dashv \text{ B y }$                                  | $\vdash \text{ ab}$          | $\text{ywx } \dashv$         | Match $y$                                                    |
> | $\dashv \text{ B }$                                    | $\vdash \text{ aby}$         | $\text{wx } \dashv$          | Pop $B$, push $\text{x, w}$                                  |
> | $\dashv \text{ xw}$                                    | $\vdash \text{ aby}$         | $\text{wx } \dashv$          | Match $w$                                                    |
> | $\dashv \text{ x}$                                     | $\vdash \text{abyw} $        | $\text{x } \dashv$           | Match $x$                                                    |
> | $\dashv$                                               | $\vdash \text{abywx}$        | $\dashv$                     | Match $\dashv$                                               |
> | $\epsilon$                                             | $\vdash \text{abywx} \dashv$ | $\epsilon$                   | Accept                                                       |

What if there’s more than one grammar rule for $A$? How do we choose which $\alpha$ to apply?

### Brute-Force

Try all combinations - this is very inefficient! We want a deterministic procedure. 

==Solution==: Use next symbol of input to help determine the rule to choose (1 “lookahead”). Let’s construct a **Predictor Table**. From our example earlier, the grammar rules are
$$
\begin{align}
&1.\:s' \to \:\:\vdash s \dashv
\\ &2. \:s \to AyB
\\ &3. \:A \to ab
\\ &4.\:A \to cd
\\ &5.\:B \to z
\\ &6.\:B \to wx
\end{align}
$$
and any entry that is empty is an error. In this table, we look ahead and decide which rule we should apply.

|      | $\vdash$ | a    | b    | c    | d    | w    | x    | y    | z    | $\dashv$ |
| ---- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- |
| $s’$ | 1        |      |      |      |      |      |      |      |      |          |
| $s$  |          | 2    |      | 2    |      |      |      |      |      |          |
| $A$  |          | 3    |      | 4    |      |      |      |      |      |          |
| $B$  |          |      |      |      |      | 6    |      |      | 5    |          |

What if we had another rule $7.\:A \to a$? Where does this get added in our table? We will have to change the $a, A$ value to $3, 7$. It is no longer deterministic - we don’t know which rule to apply. Thus, we want to restrict our grammar so this does not occur. 

==Note== on descriptive **ERROR** messages: `Parse error at row, col: expecting one of __, __, __, ...` where the `row` is our non-terminal, but we couldn’t match anything. `__` are the chars for which our current stack top has entries in the Predictor Table. If we have more than 1 rule per cell, this rule breaks down.

---

### LL(1)

A grammar is called ==**LL(1)**== if each cell of the predictor table contains at most 1 entry. 

- left to right scanning of input
- leftmost derivation is produced
- 1 symbol lookahead

---

We want to **automatically** create the Predictor Table. When we call `Predict(A, a)`, it should return the rule(s) that apply when $A$ is the top of the stack and $a$ is the next input symbol. So, for terminals $\Sigma$ and non-terminals $N$,
$$
=\{ A\to\beta \: | \: a \in \text{First}(\beta)\}
\\\text{First}(\beta) \text{, ~}\beta \in V^*\text{ where } V = \Sigma \cup N
\\ = \{a \: | \: \beta\implies^*a\Upsilon\} \text{ (* is 0 or more steps)}
$$
So, if $s\to AyB \to abyB\to\cdots$,  $\text{Predict}(A, a) = \{A \to \beta \: | \: \beta \implies * a\}$ as $a \in \text{First}(S)$ and $a \in \text{First}(A)$.

A ==problem== arises when we have that $A \implies *\epsilon$. Then $a$ might not come from $A$ but from something after $A$.
$$
\begin{align}
	&s\to AB
	\\&A \to \epsilon
	\\&B\to a
\end{align}
$$
So really, 
$$
Predict(A, a) = \{A\to\beta \: | \: a \in First(\beta)\} \cup \{A\to\beta\:|\:Nullable(\beta), a \in Follow(A)\}
$$
where $Nullable(A) = true$ if $\beta\implies *\epsilon$, false otherwise. 

>Grammar:
>$$
>\begin{align}
>	&1.\:s\to aA
>	\\&2.\:A\to B
>	\\&3.\:B\to\epsilon
>	\\&4.\:C\to\epsilon
>	\\&5.\:C\to a
>	\\&6.\:A\to aBC
>\end{align}
>$$
>So we have that $B, C A$ are all nullable. 

Now $Follow(A) = \{b\:|\: s’ \implies \alpha A b \beta\}$, all the terminals that come immediately after A in a derivation starting from $s’$.

> $$
> \begin{align}
> 	&1.\:s' \to AB
> 	\\&2.\: A\to Ab
> 	\\&3.\: A\to \epsilon
> 	\\&4.\: B\to c
> \end{align}	
> $$
>
> and so $b\in Follow(A), c\in Follow(A)$, $s’\to AB \to Ac \to \cdots$ .

### Computing $Nullable$

```python
Initialize[A] = false, forall A in N
repeat:
    for each rule B->B_1, ..., B_k:
        if (k == 0) or (Nullable[B_1]==Nullable[B_2]==...==Nullable[B_k] == true):
            Nullable[B] = true
```

The first pass checks which can immediate go to $\epsilon$. The second time through we can check non-terminals to see if they are nullable. We keep going until nothing changes.	