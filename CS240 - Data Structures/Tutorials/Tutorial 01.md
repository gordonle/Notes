CS240 Tutorial 1 | January 21, 2019

> Prove from first principles that $log(n!) \in \Theta(nlog\space n)​$

So proving this, we need to show $O(nlog\space n)$ and $\Omega(nlog\space n)$. 

1. Upper (O)
   $$
   \exists c_1,n_1 \text{ such that } log(n!) \le log(n) \space \forall n \gt n_1 \\
   \text{We know that } log(n!) = log(n(n-1)(n-2)...(2)(1)) \le log(n^n) = nlog(n) \text{, as required.} \\
   \text{So we can take } c_1 = 1, n_1 = 1 \text{ (the value of $n_1$ doesn't really matter, as long as $n_1 \gt 0$)}
   $$
   

2. Lower ($\Theta$)
   $$
   \begin{align}
   \exists c_2,n_2 \text{ such that } log(n!) &\ge c_2nlog(n) \space \forall n \gt n_2 \\ log(n!) &= log(n(n-1)(n-2)...(2)(1))
   \\ &= log(n) + log(n-1) + log(n-2) + \space ... + log(2) + log(1) \text{ (total of $n$ terms)}
   \\ &\ge log(n) + log(n-1) + log(n-2) + \space...+log(\frac{n}{2}) \text{ (total of $\frac{n}{2}$ terms)}
   \\ &\ge log(\frac{n}{2}) + log(\frac{n}{2}) + \space ...+ log(\frac{n}{2})
   \\ &= \frac{n}{2}log(\frac{n}{2})
   \end{align}
   $$
   And so,
   $$
   \begin{align} log(n!) \ge \frac{n}{2}log(\frac{n}{2}) = \frac{n}{2}log(n) -\frac{n}{2} &\ge c_2nlog(n)
   \\ \frac{n}2log(n) &\ge c_2nlog(n) + \frac{n}2
   \\ \frac{n}4log(n) + \frac{n}4log(n) &\ge c_2nlog(n)+\frac{n}2
   \end{align}
   \\ \text{This gives us two different inequalities}
   \\ \frac{n}4log(n) \ge c_2nlog(n) \implies c_2 \le \frac{1}4,
   \\ \frac{n}4log(n) \ge \frac{n}2 \implies n\ge4
   \\ \text{So, we conclude that}
   \\ log(n!) \ge \frac{1}4nlog(n) \space \forall n\ge 4, \text{ choose }c_2 = \frac{1}4, n_2=4
   $$
   

> Prove or disprove the following claim: If $h_1(n) \in \Theta(f(n)), h_2(n) \in \Theta(g(n)) \implies \frac{h_1(n)}{h_2(n)} \in \Theta(\frac{f(n)}{g(n)})$ . You should prove the statement from first principles or provide a counter example.

$$
h_1(n) \in \Theta(f(n)) \implies \exists c_1, c_2, n_1 \space c_1f(n) \le h_1(n) \le c_2f(n) \space \forall n \gt n_1
\\ h_2(n) \in \Theta(g(n)) \implies \exists c_3, c_4, n_2 \space c_3g(n) \le h_2(n) \le c_4g(n) \space \forall n \gt n_2
\\ \text{This tells us that} \\
\begin{align}
\frac{c_1}{c_4}\frac{f(n)}{g(n)} = \frac{c_1f(n)}{c_4g(n)}&\le \frac{h_1(n)}{h_2(n)}
\\ \text{(since $n \gt n_1$) } &\le \frac{c_2f(n)}{h_2(n)}
\\ \text{(since $n \gt n_2$) } &\le \frac{c_2f(n)}{c_3g(n)} = \frac{c_2}{c_3} \frac{f(n)}{g(n)}
\\ \text{So we choose } n_0 =max(n_1, n_2)
\end{align}
$$



> Question 4

Let $t$ be the number of iterations of the while loop. $j = 0,k,2k,3k,...$ so after $t$ iterations, $j=tk \implies t = \frac{j}k$.

The while loop terminates when:
$$
\begin{align}
j &\gt n
\\ tk &\gt n
\\ t &\gt \frac{n}k
\\ t &\approx \frac{n}k
\end{align}
$$
So the code is now
$$
\text{for } \sum_{i=1}^n O(1) + \frac{n}k = \sum_{i=1}^nO(1)+\frac{n}{2^{i-1}}
\\ \text{Then, since }k=1,2,4,8,16,... \\
\begin{align}
&= O(n) + n\sum_{i=1}^n(\frac{1}{2})^{i-1}
\\ &= O(n) + n * \Theta(1)
\\ &= O(n) + \Theta(n)
\\ &= \Theta(n)
\end{align}
$$
