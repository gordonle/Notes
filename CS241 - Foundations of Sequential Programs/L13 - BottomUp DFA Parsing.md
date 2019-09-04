CS241 L13 | February 28^th^, 2019

# Bottom-Up Parsing

We go from $w$ to $S$. The `stack` stores partially reduced info read so far,
$$
w \gets \alpha_k\gets\alpha_{k-1}\gets\cdots\gets\alpha_1\gets S
$$
==Invariant==: the `stack` + entire unread input $= \alpha_i$ (or $w$ or $S$)

> **Ex**: Reading in: “ $\vdash abywx \dashv​$  ”, with our grammar:
> $$
> \begin{align}
> 	S' &\to \: \vdash S \dashv \text{ (added to augment our grammar)}
> 	\\ S &\to AyB
> 	\\ A &\to ab
> 	\\ A &\to cd
> 	\\ B &\to z
> 	\\ B &\to wx
> \end{align}
> $$
>
> | Stack              | Read                   | Unread                | Action                                                       |
> | ------------------ | ---------------------- | --------------------- | ------------------------------------------------------------ |
> | $\epsilon$         | $\epsilon$             | $\vdash abywx \dashv$ | Shift $\vdash$                                               |
> | $\vdash$           | $\vdash$               | $abywx \dashv$        | Shift $a$                                                    |
> | $\vdash  a$        | $\vdash  a$            | $bywx \dashv$         | Shift $b$                                                    |
> | $\vdash  ab$       | $\vdash  ab$           | $ywx \dashv$          | Reduce $A\to ab$: pop $b$, pop $a$, push $A$                 |
> | $\vdash  A$        | $\vdash  ab$           | $ywx \dashv$          | Shift $y$                                                    |
> | $\vdash  Ay$       | $\vdash  aby$          | $wx\dashv$            | Shift $w$                                                    |
> | $\vdash  Ayw$      | $\vdash  abyw$         | $x\dashv$             | Shift $x$                                                    |
> | $\vdash  Aywx$     | $\vdash  abywx$        | $\dashv$              | Reduce $B\to wx$: pop $x$, pop $w$, push $B$                 |
> | $\vdash  AyB$      | $\vdash  abywx$        | $\dashv$              | Reduce $S\to AyB$: pop $B$, pop $y$, pop$A$, push $S$        |
> | $\vdash  S$        | $\vdash  abywx$        | $\dashv$              | Shift $\dashv$                                               |
> | $\vdash  S \dashv$ | $\vdash  abywx \dashv$ | $\epsilon$            | Reduce $S’\to \:\vdash S \dashv$: pop $\dashv$, pop $S$, pop $\vdash$, push $S’$ |
> | $S’$               | $\vdash  abywx\dashv $ | $\epsilon$            | Accept                                                       |
>
> At any step, we either **Shift** or **Reduce**, or **Accept** once we reach an end terminal.
>
> What if we introduced the rule $B\to xwx​$, and our `stack` is currently $xwx​$? We have multiple choices. This does not work with our grammar, and results in a *non-deterministic* algorithm. We want *deterministic* algorithms.

At each individual step, we have two choices:

1. **Shift** a character from input to our stack
2. **Reduce** if we have identified that the top of our stack contains a derivation of our grammar. In other words, if the top of our stack is the RHS of some grammar rule, replace it with the LHS of this grammar rule.

At the very end, we have conditions we need to check if we want to **Accept**:

1. We have no more input
2. Start symbol is the *only* item on the stack

How do we know when to shift or reduce? We can check the next character of input to help us decide. But this doesn’t really solve our problem that well. We want to build some sort of predictor table, some mechanism that helps us choose. This is outside of the scope of this course, even profs don’t/can’t do it.

==**Theorem**==: By Donald Knuth. The set $\{wa | \exists x, S \implies ^*wax\}$, where $w$ is the `stack`, and $a$ is the next input is a ***<u>Regular Language</u>***. This means that it can be described by a DFA. This will serve as our decision mechanism.

The resulting method is LR Parsing

# LR Parsing

Left-to-Right scan, Right most derivations. 

> **Ex**: Consider the set of grammar rules,
> $$
> \begin{align}
> 	Y' &\to \: \vdash E \dashv
> 	\\ E &\to E +T
> 	\\ E &\to T
> 	\\ T &\to id
> \end{align}
> $$
> This is not LL(1), since there are multiple options ($id + id$ or $id$), if our stack is $... E ...$ So let’s use LR(0) automation.

==Item==: A production with a dot $(\cdot)$ somewhere on the RHS. This indicates a partially completed rule.

$[S’ \to \cdot\vdash E\dashv\:]$  $\to$ read in $\vdash$ $\to$ $[S'\to\vdash\cdot E \dashv]$. We label an arc with the symbol that follows the dot. When we go to the next state, we advance the dot. 

If the dot precedes a nonterminal $A$, add all productions with $A$ on the LHS to the state, with the dot in the leftmost position. The DFA is as follows (thanks Sophie Q):



## Using the Automation

==START==: start state with the empty stack

==SHIFTING==: we shift a character from input onto the stack. We then follow a transition that will be labelled with that character to the next state. If there are no valid transitions, we either **reduce** or error.

==REDUCING==: “Reduce” states have only one item, and the dot is rightmost (at the end). We do the following:

1. Reduce the Rule in the state
2. Pop RHS off the stack
3. Backtrack size(RHS) states in the DFA. 
   - to backtrack, we must remember the DFA states we’ve visited. So we push the DFA states onto the stack as well. 
4. Follow the transition for the LHS, and push the LHS onto the stack. 

Accept if $S’$ is on the stack when the input is empty. 

> Ex: Reading in $\vdash id+id+id\dashv​$, with grammar
> $$
> \begin{align}
> 	S' &\to \: \vdash E \dashv
> 	\\ E &\to E +T
> 	\\ E &\to T
> 	\\ T &\to id
> \end{align}
> $$
>
> | Stack                                | Read                  | Unread                  | Action                                                       |
> | ------------------------------------ | --------------------- | ----------------------- | ------------------------------------------------------------ |
> | $1$                                  | $\epsilon$            | $\vdash id+id+id\dashv$ | S2 (shift and go to state 2)                                 |
> | $1 \vdash 2$                         | $\vdash$              | $id + id + id \dashv$   | S6 (shift and go to state 6)                                 |
> | $1 \vdash 2 \: id \:6$               | $\vdash id$           | $+ id + id \dashv$      | Reduce $T\to id$, pop $id$ and backtrack $1$ state<br />Now in state 2, push $T$ and go to state 5 |
> | $1 \vdash 2 \: T\: 5$                | $\vdash id$           | $+ id + id \dashv$      | Reduce $E\to T$, pop $T$ and backtrack 1 state<br />Now in state 2, push $E$ and go to state 3 |
> | $1 \vdash 2 \: E\: 3$                | $\vdash id$           | $+ id + id \dashv$      | S7                                                           |
> | $1 \vdash 2 \: E\: 3 + 7$            | $\vdash id +$         | $id + id \dashv$        | S6                                                           |
> | $1 \vdash 2 \: E\: 3 + 7 \: id \: 6$ | $\vdash id + id $     | $+ id \dashv$           | R: $T\to id$                                                 |
> | $1 \vdash 2 \: E\: 3 + 7 \: T \: 8$  | $\vdash id + id$      | $+id \dashv$            | R: $E\to E + T$                                              |
> | $1 \vdash 2 \: E\: 3$                | $\vdash id + id$      | $+id\dashv$             | S7                                                           |
> | $1 \vdash 2 \: E\: 3 + 7$            | $\vdash id + id +$    | $id \dashv$             | S6                                                           |
> | $1 \vdash 2 \: E\: 3 + 7 \: id \: 6$ | $\vdash id + id + id$ | $\dashv$                |                                                              |
>
> 

