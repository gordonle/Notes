CS466 L02 | May 14, 2020

# Concentration Inequalities

How do we analyze randomized algorithms if their behaviour are so random/unpredictable? But in reality, concentration inequalities are used to prove that a random variable is close to its expected value with high probability.

These are very important tools in analyzing randomized algorithms, since they can be used to show that a randomized algorithm behaves almost deterministically (ie. very close to what we "expect").

So then this is a very common strategy. We need to look at the right random variables, then compute their expected values, and use concentration inequalities to prove that the outcomes are close to the expectation with high probability, and then proceed as if their behaviour is deterministic.

## Markov's Inequality

Suppose someone claims that they have an alg for sorting with expected (average) running time $2n\log n$. No further info of the algorithm. What bound can we give for the runtime of this algorithm to be more than $4n\log n$?

The answer is $\frac 12 = \frac{E(x)}{4n\log n}$. Assuming towards contradiction, say $prob > \frac 12$, then runtime $\ge 4n\log n \implies $ avg runtime > 

**<u>Markov's Inequality</u>**: Let $X$ be a non-negative (discrete) random variable. Then, for any $a \ge 0, Pr(X\ge a) \le \frac{E[X]}a$.

**<u>Proof</u>**:

$E[X] = \sum_{i=0}^{\infin}i\cdot Pr(X=i)\ge\sum_{i\ge a}i\cdot Pr(X=i)\ge\sum_{i\ge a}a\cdot Pr(X=i) = a\cdot Pr(X\ge a)$

> Coin flipping: $n$ independent fair coins, what is the prob that there are at least $\frac{3n}4$ heads?

$X = \sum_{i=1}^nX_i$, where $X_i = \{1 \text{ if i-th coin flip is head}, 0 \text{ otherwise}$}. So

$E[X] = \sum^n_{i=1}E[X_i] = \frac n2$, and then $Pr(X\ge\frac{3n}4)\le\frac{E[x]}{\frac{3n}4} = \frac{\frac n2}{\frac{3n}4}=\frac23$.

### Questions

1. Can Markov's inquality be tight? Example?
2. Does it hold for general random vairables (ie. not only non-negative)?
3. Can it be modified to bound $Pr(X\le a)$ (eg. bound $Pr(X\le \frac{E[x]}2)$)?

Both 2 and 3 fail for the same reason: if we have no control over the other side, something something. FUC

### Moments and Variance

Markov's inequality is most useful when there is no more info, or it is already enough. To prove better concentration, we need more information about the random variables. The most commonly used quantity is the ***variance***.

- $k$-th moment is defined as $E[X^k]$. Second moment is $E[X^2]$
- $Var[X]$ is defined as $E[(X-E[X])^2]$
    - ideally $E[|X-E[X]|]$, but it's difficult to compute
- Standard derivation is defined as $\sigma(X)=\sqrt{Var(X)}$
    - roughly speaking, it is trying to approximate the value of this term
- 

#### Covariance

Given two random variables $X$ and $Y$, $Cov(X,Y)$ is defined as $E[(X-E[X])(Y-E[Y])]$. $X$ and $Y$ are *positively correlated* if $Cov(X,Y) > 0$ and negatively correlated if its $< 0$. Two basic facts:

- $Var[X+Y] = Var[X] + Var[Y] + Cov(X,Y)$
- If $X$ and $Y$ are independent r.v., then $Cov(X, Y) = 0$.

## Chebyshev's Inequality

For any $a\ge 0$, $Pr(|X-E[X]| \ge a) \le \frac{Var[X]}{a^2}$.

**<u>Proof</u>**: We'll use Markov's with a change of variable. 



> Coin flip example again!

## Sum of Independent Random Variable

Our goal is to bound $P[X\ge (1+\epsilon)E[X]]$ (the upper tail) and $P[X\le(1-\epsilon)E[X]]$ (the lower tail). We consider the setting when $X$ is the sum of independent random variables. 

The **law of large numbers** says that the sum of $n$ identically distributed r.v.s is approximately $n\mu$ where $\mu$ is the mean of a r.v..

The **central limit theorem** says that 
$$
\frac{X-n\mu}{\sqrt{n\sigma^2}}\to N(0,1),
$$
where $\sigma$ is the standard deviation of a random variable. So the typical deviation from the mean is of the order $\sqrt n \sigma$. 

Chernoff bound is to give us quantitative estimate of the probabilty $X$ is far from $E[X]$ for any $n$. 

Consider a simpler setting when ther are $n$ independent coin flips, each with probabiltity $p$ head. A direct approach is to bound $Pr(X\ge k$).

> $P(X\ge k) = \sum_{i\ge k}\binom ni p^i(1-p)^{n-i}$, eg. $P(X\ge 2pn)$ is very small

This is possible but generalized. 

> Each head $p_i$

### Generalize Chebyshev's Inequality

$2k$-th moment:

> $P(|X-E[X]| \ge a) = P(|X-E[X]|^{2k} \ge a^{2k}) \le \frac{E[|X-E[X]|^{2k}]}{a^{2k}}$ (Markov's)
>
> The logic is that if we can prove that the $k$-th moment ~ $(E[X])^k$
>
> $= P(X^{2k} \ge a^{2k})$

With Chernoff, instead we compute the exponential.

> $P(X\ge a)=P(e^x\ge e^a) \le \frac{E[e^x]}{e^a}$
>
> $= P(e^{tx} \ge e^{ta}) \le \frac{E[e^{tx}]}{e^{ta}}, t\ge 0$

## Moment Generating Function

$M_X(t) = E[e^{tx}]$ is called the moment generating funciton of the random variable $X$. 

1. We can use it to compute all moments of $X$.
    $$
    \begin{align}
    M_x(t)=E[e^{tx}] &= E[\sum_{i\ge0}\frac{t^i}{i!}x^i] \\&= \sum_{i\ge0}\frac{t^i}{i!}E[X^i] \\
    M_x^{(i)}(0) &= E[X^i]
    \end{align}
    $$
    $e^{ta}$ is a very big denominator.

2. It is very easy to compute when $X$ is the sum of independent r.v.s.

    $x= x_1 + x_2$, then
    $$
    \begin{align}
    E[e^{tx}] &= E[e^{t(x_1+x_2)}]
    \\ &= E[e^{tx_1}\cdot e^{tx_2}]
    \\ &= something
    \end{align}
    $$
    

### Chernoff bound for heterogenous coin flips

Let $X_1,...,X_n$ be indep. r.v.s where $X_i=1$ with probability $p_i$ and $X_i=0$ otherwise.

[proof]



For upper tail:

For any $\epsilon > 0$, let $\mu = E[X]$ where $X$ is sum of independent heterogenous coin filps,
$$
P(X\ge(1+\epsilon)\mu)\le(\frac{e^\epsilon}{(1+\epsilon)^{1+\epsilon}})^\mu
$$
Proof:











