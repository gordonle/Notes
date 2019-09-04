CS241 L12 | February 26^th^

Revisiting $Nullables$ and prediction,

$Predict(A, a) = \{A \to \beta \: | \:a\in First(\beta)\} \:\cup\:\{A\to\beta\: | \: Nullable(\beta), a\in Follow(A)\}$ with the grammar rules
$$
\begin{align}
	A &\to aB
	\\A &\to C
	\\C&\to\epsilon
	\\D&\to aB
	\\A&\to A^*\epsilon D \:\:\:\:\text{(*$First(D)$ will be what follows A)}
\end{align}
$$
$Nullable(A) = true$ if $\beta \implies^* \epsilon$, $false$ otherwise, $Follow(A) = \{b\: | \: s’ \implies^*aAbB\}$.

# Computing 

## $First(First\_Base)$

We use an array, and for each ==non-terminal==, 

```python
Initialize First[A] = [] for all A in N
repeat:
    for each rule A -> B_1, B_2, B_3, ..., B_k:
        for i = 1...k:
            if B_i is a terminal "a":
                First(A) union [a]
                break
            else:
                First(A) union First(B_i)
                if not Nullable(B_i): # A->CD, C->a, C->epsilon, D->b
                	break
```

> **Ex:** Consider the grammar
> $$
> \begin{align}
> 	s'&\to\:\vdash s \dashv
> 	\\s&\to bSd
> 	\\s&\to pSq
> 	\\s&\to c
> 	\\c&\to lc
> 	\\c&\to \epsilon
> \end{align}
> $$
> Then $B_i \in V = \Sigma \cup N$ , where $\Sigma$ are terminals and $N$ are non-terminals. Now, let’s look at a few iterations
>
> | First | Iterations (0) | 1            | 2            |
> | ----- | -------------- | ------------ | ------------ |
> | $s’$  | $\{\}$         | $\{\vdash\}$ | $\{\vdash\}$ |
> | $s$   | $\{\}$         | $\{b,p\}$    | $\{b,p,l\}$  |
> | $c$   | $\{\}$         | $\{l\}$      | $\{l\}$      |
>
> and we repeat until nothing changes. 

## $First^*(\beta)$

The “final set” for a string of symbols $\beta\in V^* = \{\Sigma\cup N\}$.

```python
First*(Y_1,...,Y_n):
    result = null
    for i = 1,...,n:
        if Y_i not in Sigma: # not a terminal, or Y_i \in N
            result += First[Y_i] # lookup in memory from First_Base
            if not Nullable[Y_i]:
                break
        elif Y_i in Sigma:
            result += {Y_i} # the terminal
            break
    return result
```

> **Ex:** $First^*(ABc) = \{a,b,c\}$
> $$
> \begin{align}
> 	A&\to a
> 	\\A&\to \epsilon
> 	\\B&\to b
> 	\\B&\to \epsilon
> \end{align}
> $$
> 

**<u>NOTE</u>**: These algorithms are 100% going to be on the midterm or final

## Follow

```python
Initialize Follow[A] = {} for all A not in S'
repeat until nothing changes:
    for each rule A->B_1, B_2, ..., B_n:
        for i = 1 to n:
            if B_i in N: # only do Follow sts for non-terminals
                Follow[B_i] += First*(B_i+1, ..., B_n)
                if all of B_i+1,...,B_n are Nullable:
                    Follow[B_i] += Follow[A]
```

> **Ex:**  
> $$
> \begin{align}
> 	A&\to \underline{B}Dc
> 	\\A&\to\underline{B}\:\underline{D}
> 	\\B&\to b
> 	\\B&\to\epsilon
> 	\\D&\to d
> 	\\S&\to AC
> \end{align}
> $$

# LL(1)

A grammar is LL(1) if the following conditions hold:

1. No two distinct productions with the same LHS can generate the same first terminal symbol
   - the ==predictor table== has only 1 entry per cell, therefore deterministic
2. No nullable symbol $A$ has the same terminal symbol $a$ in both its $First$ and $Follow$ sets
3. There is only 1 way to send a nullable symbol to $\epsilon$
   - Ex: $A\to\epsilon, A\to B, B\to\epsilon$.

# Some Review

$$
\begin{align}
s&\to a|b|b|S\:OP\:S|(S)
\\OP&\to +|*
\end{align}
$$

==Problem:== Ambiguous

---

$$
\begin{align}
E&\to E\:OP\:T | T
\\T&\to a|b|c|(E)
\\OP&\to +|*
\end{align}
$$

==Problem:== Not ambiguous. We want to add procedures (left recursive)

---

$$
\begin{align}
E&\to E+T | (T)
\\T&\to T * F | F
\\F&\to a|b|c|(E)
\end{align}
$$

This has a procedure! Is this LL(1)? **No**, it is not. 



Midterm content ends here.







