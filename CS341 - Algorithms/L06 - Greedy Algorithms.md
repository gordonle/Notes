CS341 L06 | September 23, 2019

# Greedy Algorithms

A classic example of a greedy algorithm is change generation! For example, if we want $3.47, what’s the minimum number of coins that we need to get this?
$$
\begin{align}
	1 &\times $2 \\
	1 &\times $1 \\
	1 &\times 25¢ \\
	2 &\times 10¢ \\
	2 &\times 1¢
\end{align}
$$
Does this work for every system of coins though? What if our denominations were 1¢, 6¢ and 7¢, and we wanted 12¢? If we followed greedy here, we would get $1\times 7¢, 5\times 1¢$, whereas the minimum number of coins needed is just $2\times 6¢$.

> Ex: **<u>Interview Scheduling, or “Activity Selection”</u>**
>
> ```
>   9  10  11  12   1   2   3   4   5   6   7   8
> --|---|---|---|---|---|---|---|---|---|---|---|---|
> 
> |-----|   |---|---|               |--------|
> CS Class  (sem)(lunch)             math news
>             |-----|-----|     |-------|
>              math  science      soccer
>           |--------------------------------|
>                      bike trip
> ```
>
> Given a set of activities, each with specific intervals, select a maximum number of intervals that do not overlap. 
>
> If we follow a “greedy” approach, we would:
>
> 1. Pick one activity (only one works)
>    - by start time
>    - smallest interval
>    - by end time
>    - minimum number of conflicts
> 2. Remove conflicting activities
> 3. Repeat

In the above example, here are proofs as to why three of the options for picking an activity don’t work. 

1. Start Time

   Given the example, if we have an event that starts first but spans a very long time, conflicting with many other activities, then that gives us the wrong answer. 

2. Smallest Interval

   ```
   |-----|-----|
       |---|
   ```

   If we choose smallest interval, then we would choose 1 and not 2 activities.

3. End Time

   This one is correct! Let’s see a simple implementation for it. 

   ```
   def greedy(activities):
   	sort activities 1..n by end time
   	A = []
   	for i = 1...n:
   		if activities[i] doesn't overlap w anything in A (just check last activity in A):
   			A.append(activities[i])
   	return A
   ```

   $\text{Runtime = sort + loop} =O(n\log n) + O(n) \in O(n\log n)$.

4. Minimum # of conflicts

   ```
   |-----|-----|-----|-----|
             |---|
       |---|       |---|
       |---|       |---|
       |---|       |---|
   ```

   In this case, we would see that the max number of activities are the top 4, yet those each have many conflicts. So we would have to choose the one in the middle, then one from either stack, yielding 3 and not 4 activities. 

## Correctness

How do we show correctness for our algorithm? There are two basic correctness approaches, both of which really are just induction.

1. Greedy always stays ahead
2. “Exchange proof”

### I. Greedy Always Stays Ahead

<u>Lemma</u>: This algorithm returns a max size set $A$ of disjoint intervals. 

<u>Proof</u>: Let $A = \{a_1,...,a_k\}$ sorted by end time. Let $B=\{b_1,...,b_l\}$ be an optimum solution, sorted by end time. Since $B$ is optimum, we know that $l\ge k$. We want to prove that $l=k$. The idea here is to show that at every step, if $b_i \ne a_i$, we could replace $b_i$ with $a_i$ and still have an optimal solution.

<u>Claim</u>: $a_1,...,a_i,b_{i+1},...,b_l$ is an optimum solution $\forall i$. We’ll prove this by induction on $i$. 

Our base case is for $i=1$. ($i=0$ would be fine as well, and is trivial). So we want to show that $a_1,b_2,...,b_l$ is optimal. We know that $b_2,...,b_l$ are disjoint. We know that the $end(a_1)\le end(b_1)$ by greedy algorithm. So $a_1$ does not overlap with $b_2$. 

Suppose that $a_1,...,a_{i-1},b_i,...,b_l$ is an optimal solution. We must show that $a_i$ is disjoint from $a_{i-1}$ and $b_{i+1}$. We know it doesn’t overlap with $a_{i-1}$ since it’s chosen from greedy algorithm together. As a consequence of using the greedy approach, we know that $end(a_i) \le end(b_i)$. Greedy only chooses non-overlapping intervals, so then we know that $b_i$ is a candidate to be chosen since it does not overlap with $a_{i-1}$. Thus $a_i$ is disjoint from $b_{i+1}$. 

Therefore, $a_1,...,a_i,b_{i+1},...b_l$ is an optimal solution. 

How do we use this claim to prove $l=k$? From the claim, we get that $a_1,...,a_k,b_{k+1},...,b_l$ is an optimum solution as well. Suppose $l>k$. But then the greedy algorithm would have picked $b_{k+1}$, since its endpoint is later and there are no conflicts. So then $l=k$. 

> Ex: **<u>Scheduling to Minimize Lateness</u>**
>
> | Assignments | Time Required (hrs) | Deadline (hrs) |
> | ----------- | ------------------- | -------------- |
> | CS 341      | 4                   | 9              |
> | Math        | 2                   | 6              |
> | Philosophy  | 3                   | 14             |
> | CS 350      | 10                  | 25             |
>
> No sleeping, no eating, can we get this all done by their deadlines? We could also think about an optimization version of this problem, where we want to minimize the maximum lateness. Note that this is different from minimizing the sum of the lateness. 
>
> Each job $j_i$ takes time $t_i$ and has deadline $d_i$. Whenever you start a job you must finish it. Ideas for picking jobs:
>
> - Do job with earliest deadline
> - Jobs with less “slack first”, where slack $=d_i - t_i$
> - do short jobs first
>
> Try to find counter examples for these!

