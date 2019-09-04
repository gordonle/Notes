CS241 L07 | January 29, 2019

# Deterministic Finite Automata (DFA)

Recall from last time, a DFA is a 5-tuple $M = (\Sigma, Q, q_0, A, \delta)​$. States represent the pattern recognized so far, and finite states are the finite number of “patterns” that can be recognized.

- $\Sigma$ is a finite, non-empty **alphabet**
- $Q​$ is a finite, non-empty **set of states**
- $q_0 \in Q$ is our **start state**
- $A \subseteq Q$ is the set of **accepting states**
- $\delta : (Q \times \Sigma) \to Q​$ is our transition function
  - From a given state, on given input symbol, we get the next state
  - It consumes a single symbol, and never goes back or stores previous input
  - We can extend $\delta​$ to consume a word: $\delta ^* (q, cw) = \delta ^* (\delta (q, c), w)​$ where $c \in \Sigma​$ and $w \in \Sigma^*​$
- We accept if $\delta ^*(q_0, w) \in A​$. This means we start a $q_0​$ on input $w​$, and end up in an Accepting State 

> Ex: A DFA for $L = \{\text{even number of a's, odd number of b's}\}$
>
> Our DFA will have:
>
> - A $q_0$ state = {even number of $a$’s and even number of $b$’s}
> - The other states in $Q$:
>   - {odd number of $a$’s and even number of $b$’s}
>   - {even number of $a$’s and odd number of $b$’s} $\to$ this is our accepting state $A$
>   - {odd number of $a$’s and odd number of $b$’s}
> - Our $\delta$ given either an $a$ or a $b$ is to move between these different states given the new state if we add that to the current state

**Theorem (Kleene)**: $L$ is regular $\iff L = L(M)$ for some DFA $M$.

## Implementing a DFA

```c++
int state = q_0;
char ch;
while (cin >> ch) {
    case state of:
    	q_0: case ch of:
    		a: state = ...; \\ some other q_i where (0 <= i <= n)
    		b: state = ...;
    	q_1: case ch of:
    		a: state = ...;
    		b: state = ...;
    	...;
    	q_n: case ch of:
    		a: state = ...;
    		b: state = ...;
    end case
}
return state in A;
```

## DFA’s with Actions

We can attach a computation to each transition. This allows us to check more than just if our state is in $A$.

> **Ex:** $L =\{ \text{binary #s with no leading 0s}\}$
>
> We simultaneously compute the value in base 10, as well as accept/reject states.
>
> <svg width="700" height="400" version="1.1" xmlns="http://www.w3.org/2000/svg">
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="154.5" cy="213.5" rx="30" ry="30"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="378.5" cy="120.5" rx="30" ry="30"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="378.5" cy="120.5" rx="24" ry="24"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="362.5" cy="307.5" rx="30" ry="30"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="362.5" cy="307.5" rx="24" ry="24"/>
> 	<polygon stroke="black" stroke-width="1" points="88.5,213.5 124.5,213.5"/>
> 	<polygon fill="black" stroke-width="1" points="124.5,213.5 116.5,208.5 116.5,218.5"/>
> 	<polygon stroke="black" stroke-width="1" points="182.207,201.997 350.793,132.003"/>
> 	<polygon fill="black" stroke-width="1" points="350.793,132.003 341.487,130.453 345.322,139.689"/>
> 	<text x="270.5" y="188.5" font-family="Times New Roman" font-size="20">1(N = 1)</text>
> 	<polygon stroke="black" stroke-width="1" points="181.838,225.855 335.162,295.145"/>
> 	<polygon fill="black" stroke-width="1" points="335.162,295.145 329.931,287.294 325.813,296.407"/>
> 	<text x="180.5" y="281.5" font-family="Times New Roman" font-size="20">0 (N = 0)</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 380.579,90.689 A 22.5,22.5 0 1 1 403.426,104.017"/>
> 	<text x="417.5" y="53.5" font-family="Times New Roman" font-size="20">1(N = N*2 + 1) or 0 (N = N*2)</text>
> 	<polygon fill="black" stroke-width="1" points="403.426,104.017 412.762,105.373 408.736,96.219"/>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 375.753,280.717 A 22.5,22.5 0 1 1 391.82,301.728"/>
> 	<text x="421.5" y="258.5" font-family="Times New Roman" font-size="20">ERROR</text>
> 	<polygon fill="black" stroke-width="1" points="391.82,301.728 399.94,306.53 399.695,296.533"/>
> </svg>
>
> 

# Non-Deterministic Finite Automata (NFA)

With NFAs, we allow more than 1 transition on a symbol from the same state. This means that we have more than one path to get to an accepting pattern state.

> **Ex:** $L = \{w\in \{a,b\}^* | \:\text{w ends in abb}\}​$
>
> <svg width="600" height="200" version="1.1" xmlns="http://www.w3.org/2000/svg">
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="134.5" cy="151.5" rx="30" ry="30"/>
> 	<text x="117.5" y="157.5" font-family="Times New Roman" font-size="20">start</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="241.5" cy="97.5" rx="30" ry="30"/>
> 	<text x="228.5" y="103.5" font-family="Times New Roman" font-size="20">"a"</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="362.5" cy="96.5" rx="30" ry="30"/>
> 	<text x="344.5" y="102.5" font-family="Times New Roman" font-size="20">"ab"</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="503.5" cy="96.5" rx="30" ry="30"/>
> 	<text x="480.5" y="102.5" font-family="Times New Roman" font-size="20">"abb"</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="503.5" cy="96.5" rx="24" ry="24"/>
> 	<polygon stroke="black" stroke-width="1" points="58.5,151.5 104.5,151.5"/>
> 	<polygon fill="black" stroke-width="1" points="104.5,151.5 96.5,146.5 96.5,156.5"/>
> 	<polygon stroke="black" stroke-width="1" points="161.283,137.984 214.717,111.016"/>
> 	<polygon fill="black" stroke-width="1" points="214.717,111.016 205.323,110.157 209.828,119.085"/>
> 	<text x="192.5" y="145.5" font-family="Times New Roman" font-size="20">a</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 339.211,115.133 A 80.298,80.298 0 0 1 265.094,115.746"/>
> 	<polygon fill="black" stroke-width="1" points="339.211,115.133 329.8,114.468 334.489,123.3"/>
> 	<text x="297.5" y="145.5" font-family="Times New Roman" font-size="20">b</text>
> 	<polygon stroke="black" stroke-width="1" points="392.5,96.5 473.5,96.5"/>
> 	<polygon fill="black" stroke-width="1" points="473.5,96.5 465.5,91.5 465.5,101.5"/>
> 	<text x="428.5" y="117.5" font-family="Times New Roman" font-size="20">b</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 112.068,131.757 A 22.5,22.5 0 1 1 136.526,121.686"/>
> 	<text x="94.5" y="79.5" font-family="Times New Roman" font-size="20">b</text>
> 	<polygon fill="black" stroke-width="1" points="136.526,121.686 143.269,115.088 133.55,112.733"/>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 220.884,75.867 A 22.5,22.5 0 1 1 246.13,67.978"/>
> 	<text x="208.5" y="23.5" font-family="Times New Roman" font-size="20">a</text>
> 	<polygon fill="black" stroke-width="1" points="246.13,67.978 253.426,61.996 243.95,58.799"/>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 266.427,81.06 A 89.494,89.494 0 0 1 337.305,80.475"/>
> 	<polygon fill="black" stroke-width="1" points="266.427,81.06 275.764,82.406 271.728,73.257"/>
> 	<text x="297.5" y="64.5" font-family="Times New Roman" font-size="20">a</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 259.549,73.596 A 153.959,153.959 0 0 1 485.269,72.735"/>
> 	<polygon fill="black" stroke-width="1" points="259.549,73.596 268.646,71.098 261.29,64.324"/>
> 	<text x="367.5" y="14.5" font-family="Times New Roman" font-size="20">a</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 478.072,112.408 A 432.687,432.687 0 0 1 163.462,159.301"/>
> 	<polygon fill="black" stroke-width="1" points="163.462,159.301 170.122,165.982 172.386,156.242"/>
> 	<text x="323.5" y="187.5" font-family="Times New Roman" font-size="20">b</text>
> </svg>
>
> We accept if there exists a path from start to an accepting state, reading through every input one at a time. Since we only care about the end state here, we could also create 
>
> <svg width="600" height="200" version="1.1" xmlns="http://www.w3.org/2000/svg">
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="100.5" cy="79.5" rx="30" ry="30"/>
> 	<text x="95.5" y="85.5" font-family="Times New Roman" font-size="20">1</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="222.5" cy="79.5" rx="30" ry="30"/>
> 	<text x="217.5" y="85.5" font-family="Times New Roman" font-size="20">2</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="349.5" cy="79.5" rx="30" ry="30"/>
> 	<text x="344.5" y="85.5" font-family="Times New Roman" font-size="20">3</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="477.5" cy="79.5" rx="30" ry="30"/>
> 	<text x="472.5" y="85.5" font-family="Times New Roman" font-size="20">4</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="477.5" cy="79.5" rx="24" ry="24"/>
> 	<polygon stroke="black" stroke-width="1" points="130.5,79.5 192.5,79.5"/>
> 	<polygon fill="black" stroke-width="1" points="192.5,79.5 184.5,74.5 184.5,84.5"/>
> 	<text x="157.5" y="100.5" font-family="Times New Roman" font-size="20">a</text>
> 	<polygon stroke="black" stroke-width="1" points="252.5,79.5 319.5,79.5"/>
> 	<polygon fill="black" stroke-width="1" points="319.5,79.5 311.5,74.5 311.5,84.5"/>
> 	<text x="281.5" y="100.5" font-family="Times New Roman" font-size="20">b</text>
> 	<polygon stroke="black" stroke-width="1" points="379.5,79.5 447.5,79.5"/>
> 	<polygon fill="black" stroke-width="1" points="447.5,79.5 439.5,74.5 439.5,84.5"/>
> 	<text x="408.5" y="100.5" font-family="Times New Roman" font-size="20">b</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 113.725,106.297 A 22.5,22.5 0 1 1 87.275,106.297"/>
> 	<text x="86.5" y="168.5" font-family="Times New Roman" font-size="20">a, b</text>
> 	<polygon fill="black" stroke-width="1" points="87.275,106.297 78.527,109.83 86.618,115.708"/>
> 	<polygon stroke="black" stroke-width="1" points="42.5,79.5 70.5,79.5"/>
> 	<polygon fill="black" stroke-width="1" points="70.5,79.5 62.5,74.5 62.5,84.5"/>
> </svg>

Non-determinism: At state $q_0$ , we can either:

- stay in $q_0​$
- go to $q_1$

Often, there are simpler diagrams we can use. The machine “guesses” which choice to make. When we are implementing this, we need to track **both branches**, like iterating through a tree. 

Formally, NFA $M = ( \Sigma, Q, q_0, A, \delta)$, where all definitions are the same except for:

- $\delta : (Q, \Sigma) \to \text{subset of Q }(2 ^{|Q|} \text{ possible subsets})$. This is non-determinism. 
- We **accept** if some path through NFA leads to an accepting state, and reject if such a path does not exist.
- - We again extend $\delta$ to take in words. $\delta ^*$ is defined as:
    - $\delta ^* (q_s, \epsilon) = q_s$, where $q_s$ is a set of states
    - $\delta ^*(q_s, w) = \delta ^* ((\bigcup\limits_{q\in q_s} \delta(q, c)), w) \text{, where q is a set from $q_s$}​$
    - Accept $w$ if $\delta ^*(\{q_0\}, w) \and A \ne \empty$.

## Implementing an NFA

Simulating the implementation of an NFA, examine the following pseudocode,

```
states = {q_0}
while not eof do:
	ch = read()
	states = union of delta(q, ch) for all q in states
end do
if (states AND A) not equal empty accept
else reject
```

> Simulating “baabb”,
>
> | Input Read | Yet To Read |             States              |
> | :--------: | :---------: | :-----------------------------: |
> | $\epsilon$ |    baabb    |               {1}               |
> |     b      |    aabb     |               {1}               |
> |     ba     |     abb     |              {1,2}              |
> |    baa     |     bb      | $\{1,2\} \cup\empty = \{1, 2\}$ |
> |    baab    |      b      |             {1, 3}              |
> |   baabb    | $\epsilon$  |             {1, 4}              |
>
> We now accept, since $\{1,4\} \cap{4} \ne \empty$. We can then build a DFA from this, where the states of DFA are all possible subsets of $Q​$ from the NFA,
>
> <svg width="600" height="350" version="1.1" xmlns="http://www.w3.org/2000/svg">
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="128.5" cy="231.5" rx="30" ry="30"/>
> 	<text x="113.5" y="237.5" font-family="Times New Roman" font-size="20">{1}</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="247.5" cy="157.5" rx="30" ry="30"/>
> 	<text x="225.5" y="163.5" font-family="Times New Roman" font-size="20">{1,2}</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="369.5" cy="86.5" rx="30" ry="30"/>
> 	<text x="344.5" y="92.5" font-family="Times New Roman" font-size="20">{1, 3}</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="454.5" cy="157.5" rx="30" ry="30"/>
> 	<text x="429.5" y="163.5" font-family="Times New Roman" font-size="20">{1, 4}</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="454.5" cy="157.5" rx="24" ry="24"/>
> 	<polygon stroke="black" stroke-width="1" points="153.976,215.658 222.024,173.342"/>
> 	<polygon fill="black" stroke-width="1" points="222.024,173.342 212.59,173.321 217.871,181.813"/>
> 	<text x="193.5" y="215.5" font-family="Times New Roman" font-size="20">a</text>
> 	<polygon stroke="black" stroke-width="1" points="273.429,142.41 343.571,101.59"/>
> 	<polygon fill="black" stroke-width="1" points="343.571,101.59 334.142,101.292 339.172,109.935"/>
> 	<text x="293.5" y="112.5" font-family="Times New Roman" font-size="20">b</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 234.275,130.703 A 22.5,22.5 0 1 1 260.725,130.703"/>
> 	<text x="243.5" y="81.5" font-family="Times New Roman" font-size="20">a</text>
> 	<polygon fill="black" stroke-width="1" points="260.725,130.703 269.473,127.17 261.382,121.292"/>
> 	<polygon stroke="black" stroke-width="1" points="47.5,231.5 98.5,231.5"/>
> 	<polygon fill="black" stroke-width="1" points="98.5,231.5 90.5,226.5 90.5,236.5"/>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 115.275,204.703 A 22.5,22.5 0 1 1 141.725,204.703"/>
> 	<text x="123.5" y="155.5" font-family="Times New Roman" font-size="20">b</text>
> 	<polygon fill="black" stroke-width="1" points="141.725,204.703 150.473,201.17 142.382,195.292"/>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 362.084,115.411 A 85.698,85.698 0 0 1 276.301,165.334"/>
> 	<polygon fill="black" stroke-width="1" points="276.301,165.334 283.816,171.037 284.72,161.078"/>
> 	<text x="332.5" y="175.5" font-family="Times New Roman" font-size="20">a</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 431.15,176.254 A 147.402,147.402 0 0 1 270.85,176.254"/>
> 	<polygon fill="black" stroke-width="1" points="270.85,176.254 274.845,184.8 280.282,176.407"/>
> 	<text x="346.5" y="220.5" font-family="Times New Roman" font-size="20">a</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 434.26,179.623 A 272.006,272.006 0 0 1 156.308,242.716"/>
> 	<polygon fill="black" stroke-width="1" points="156.308,242.716 162.269,250.028 165.493,240.562"/>
> 	<text x="305.5" y="272.5" font-family="Times New Roman" font-size="20">b</text>
> 	<polygon stroke="black" stroke-width="1" points="392.524,105.732 431.476,138.268"/>
> 	<polygon fill="black" stroke-width="1" points="431.476,138.268 428.541,129.302 422.13,136.977"/>
> 	<text x="396.5" y="142.5" font-family="Times New Roman" font-size="20">b</text>
> </svg>
>
> All states have a path for all possible values in the language.

> **Ex:** Something more complex, $\Sigma = \{a,b,c\}$, $L = \{cab\} \cup \{\text{strings with even # of a's}\}$
>
> NFA:
>
> <svg width="600" height="400" version="1.1" xmlns="http://www.w3.org/2000/svg">
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="104.5" cy="274.5" rx="30" ry="30"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="104.5" cy="274.5" rx="24" ry="24"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="221.5" cy="215.5" rx="30" ry="30"/>
> 	<text x="208.5" y="221.5" font-family="Times New Roman" font-size="20">"c"</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="318.5" cy="163.5" rx="30" ry="30"/>
> 	<text x="301.5" y="169.5" font-family="Times New Roman" font-size="20">"ca"</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="425.5" cy="116.5" rx="30" ry="30"/>
> 	<text x="403.5" y="122.5" font-family="Times New Roman" font-size="20">"cab"</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="425.5" cy="116.5" rx="24" ry="24"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="230.5" cy="316.5" rx="30" ry="30"/>
> 	<text x="202.5" y="322.5" font-family="Times New Roman" font-size="20">odd a's</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="363.5" cy="316.5" rx="30" ry="30"/>
> 	<text x="331.5" y="322.5" font-family="Times New Roman" font-size="20">even a's</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="363.5" cy="316.5" rx="24" ry="24"/>
> 	<polygon stroke="black" stroke-width="1" points="131.287,260.992 194.713,229.008"/>
> 	<polygon fill="black" stroke-width="1" points="194.713,229.008 185.319,228.146 189.821,237.074"/>
> 	<text x="167.5" y="266.5" font-family="Times New Roman" font-size="20">c</text>
> 	<polygon stroke="black" stroke-width="1" points="247.94,201.326 292.06,177.674"/>
> 	<polygon fill="black" stroke-width="1" points="292.06,177.674 282.647,177.047 287.371,185.861"/>
> 	<text x="274.5" y="210.5" font-family="Times New Roman" font-size="20">a</text>
> 	<polygon stroke="black" stroke-width="1" points="345.967,151.435 398.033,128.565"/>
> 	<polygon fill="black" stroke-width="1" points="398.033,128.565 388.698,127.204 392.719,136.36"/>
> 	<text x="376.5" y="161.5" font-family="Times New Roman" font-size="20">b</text>
> 	<polygon stroke="black" stroke-width="1" points="132.96,283.987 202.04,307.013"/>
> 	<polygon fill="black" stroke-width="1" points="202.04,307.013 196.031,299.74 192.869,309.227"/>
> 	<text x="154.5" y="316.5" font-family="Times New Roman" font-size="20">a</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 223.102,345.453 A 22.5,22.5 0 1 1 203.019,328.239"/>
> 	<text x="152.5" y="388.5" font-family="Times New Roman" font-size="20">b, c</text>
> 	<polygon fill="black" stroke-width="1" points="203.019,328.239 194.078,325.229 196.396,334.957"/>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 254.535,298.764 A 92.966,92.966 0 0 1 339.465,298.764"/>
> 	<polygon fill="black" stroke-width="1" points="339.465,298.764 334.633,290.662 330.065,299.558"/>
> 	<text x="292.5" y="279.5" font-family="Times New Roman" font-size="20">a</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 375.239,289.019 A 22.5,22.5 0 1 1 392.453,309.102"/>
> 	<text x="420.5" y="264.5" font-family="Times New Roman" font-size="20">b, c</text>
> 	<polygon fill="black" stroke-width="1" points="392.453,309.102 400.828,313.444 400.026,303.476"/>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 339.478,334.252 A 92.891,92.891 0 0 1 254.522,334.252"/>
> 	<polygon fill="black" stroke-width="1" points="254.522,334.252 259.35,342.357 263.923,333.464"/>
> 	<text x="292.5" y="365.5" font-family="Times New Roman" font-size="20">a</text>
> 	<polygon stroke="black" stroke-width="1" points="31.5,274.5 74.5,274.5"/>
> 	<polygon fill="black" stroke-width="1" points="74.5,274.5 66.5,269.5 66.5,279.5"/>
> </svg>
>
> 