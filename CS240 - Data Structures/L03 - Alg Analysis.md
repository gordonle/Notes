CS 240 | January 15, 2019

\*\*\*\***THIS NOTE WILL BE COMPLETED AT A LATER DATE**\*\*\*\*

From last time, 

> Show that $2019n^2 + 1388n \in o(n^3)$.
>
> We need to show that $\forall c \gt 0, \exists \ n_o \gt 0$ such that $2019n^2 + 1388n \lt c *n^3$.

*Proof*: Let $c > 0$ be given (arbitrary). **Note**: $0 < c < 1$ is possible.
$$
\begin{align}2019n^2 + 1388n &< 5000n^2 \space \space \forall  n\ge1 \\ &\le \frac {5000} {n} * n^3 \\ &\le c * n^3\end{align}
$$

> **Note:** $\frac{5000} {n} \le c \implies \forall n \ge \frac {5000} {n}$, so for any $c$, choose $n_o = \frac {5000} {c}$, where $n_o$ may depend on a given $c$

## Algebra Order of Notations

### Identity Rule



### Maximum Rule

Suppose that $f(n) > 0$ and $g(n) > 0$ for all $ n \ge n_0$. Then

$O(f(n) + g(n)) = O(max\{f(n),  g(n)\})$

### Transitivity Rule

## Techniques for Order Notation

Suppose that $f(n) > 0$ and $g(n) > 0$ for all $ n \ge n_0$. Suppose that $L = \lim \frac {f(n)} {g(n)} $ exists. Use L’Hopitals



 

