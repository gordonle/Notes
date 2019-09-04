CS241 L08 | January 31, 2019

From last time, 

> Ex:** Something more complex, $\Sigma = \{a,b,c\}$, $L = \{cab\} \cup \{\text{strings with even # of a's}\}$
>
> NFA:
>
> <svg width="600" height="350" version="1.1" xmlns="http://www.w3.org/2000/svg">
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="66.5" cy="136.5" rx="30" ry="30"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="66.5" cy="136.5" rx="24" ry="24"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="141.5" cy="52.5" rx="30" ry="30"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="248.5" cy="52.5" rx="30" ry="30"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="347.5" cy="52.5" rx="30" ry="30"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="347.5" cy="52.5" rx="24" ry="24"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="177.5" cy="178.5" rx="30" ry="30"/>
> 	<text x="155.5" y="184.5" font-family="Times New Roman" font-size="20">odd a</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="319.5" cy="178.5" rx="30" ry="30"/>
> 	<text x="293.5" y="184.5" font-family="Times New Roman" font-size="20">even a</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="319.5" cy="178.5" rx="24" ry="24"/>
> 	<polygon stroke="black" stroke-width="1" points="16.5,136.5 36.5,136.5"/>
> 	<polygon fill="black" stroke-width="1" points="36.5,136.5 28.5,131.5 28.5,141.5"/>
> 	<polygon stroke="black" stroke-width="1" points="86.48,114.122 121.52,74.878"/>
> 	<polygon fill="black" stroke-width="1" points="121.52,74.878 112.462,77.516 119.921,84.176"/>
> 	<text x="109.5" y="115.5" font-family="Times New Roman" font-size="20">c</text>
> 	<polygon stroke="black" stroke-width="1" points="171.5,52.5 218.5,52.5"/>
> 	<polygon fill="black" stroke-width="1" points="218.5,52.5 210.5,47.5 210.5,57.5"/>
> 	<text x="190.5" y="73.5" font-family="Times New Roman" font-size="20">a</text>
> 	<polygon stroke="black" stroke-width="1" points="278.5,52.5 317.5,52.5"/>
> 	<polygon fill="black" stroke-width="1" points="317.5,52.5 309.5,47.5 309.5,57.5"/>
> 	<text x="293.5" y="73.5" font-family="Times New Roman" font-size="20">b</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 312.099,207.502 A 128.295,128.295 0 0 1 64.133,166.338"/>
> 	<polygon fill="black" stroke-width="1" points="312.099,207.502 304.563,213.177 313.898,216.763"/>
> 	<text x="148.5" y="310.5" font-family="Times New Roman" font-size="20">b, c</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 186.803,206.898 A 22.5,22.5 0 1 1 160.618,203.157"/>
> 	<text x="146.5" y="268.5" font-family="Times New Roman" font-size="20">b, c</text>
> 	<polygon fill="black" stroke-width="1" points="160.618,203.157 151.459,205.418 158.637,212.381"/>
> 	<polygon stroke="black" stroke-width="1" points="94.559,147.117 149.441,167.883"/>
> 	<polygon fill="black" stroke-width="1" points="149.441,167.883 143.729,160.376 140.19,169.729"/>
> 	<text x="108.5" y="178.5" font-family="Times New Roman" font-size="20">a</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 205.131,166.945 A 148.972,148.972 0 0 1 291.869,166.945"/>
> 	<polygon fill="black" stroke-width="1" points="205.131,166.945 214.24,169.399 211.328,159.833"/>
> 	<text x="244.5" y="151.5" font-family="Times New Roman" font-size="20">a</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 292.398,191.222 A 136.025,136.025 0 0 1 204.602,191.222"/>
> 	<polygon fill="black" stroke-width="1" points="292.398,191.222 283.213,189.071 286.44,198.536"/>
> 	<text x="244.5" y="219.5" font-family="Times New Roman" font-size="20">a</text>
> 	<path stroke="black" stroke-width="1" fill="none" d="M 330.843,150.854 A 22.5,22.5 0 1 1 348.344,170.687"/>
> 	<text x="375.5" y="125.5" font-family="Times New Roman" font-size="20">b, c</text>
> 	<polygon fill="black" stroke-width="1" points="348.344,170.687 356.78,174.909 355.835,164.953"/>
> </svg>
>
> This is non-deterministic, since if we start with a ‘c’ we have two options to pick. We order each state left to right, top to bottom. Above, there are 6 states. Let’s make a DFA from this.
>
> <svg width="600" height="300" version="1.1" xmlns="http://www.w3.org/2000/svg">
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="204.5" cy="132.5" rx="30" ry="30"/>
> 	<text x="189.5" y="138.5" font-family="Times New Roman" font-size="20">{1}</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="204.5" cy="132.5" rx="24" ry="24"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="316.5" cy="56.5" rx="30" ry="30"/>
> 	<text x="301.5" y="62.5" font-family="Times New Roman" font-size="20">{5}</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="284.5" cy="228.5" rx="30" ry="30"/>
> 	<text x="259.5" y="234.5" font-family="Times New Roman" font-size="20">{2, 6}</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="284.5" cy="228.5" rx="24" ry="24"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="375.5" cy="132.5" rx="30" ry="30"/>
> 	<text x="360.5" y="138.5" font-family="Times New Roman" font-size="20">{6}</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="375.5" cy="132.5" rx="24" ry="24"/>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="447.5" cy="228.5" rx="30" ry="30"/>
> 	<text x="422.5" y="234.5" font-family="Times New Roman" font-size="20">{3, 5}</text>
> 	<polygon stroke="black" stroke-width="1" points="125.5,132.5 174.5,132.5"/>
> 	<polygon fill="black" stroke-width="1" points="174.5,132.5 166.5,127.5 166.5,137.5"/>
> 	<polygon stroke="black" stroke-width="1" points="229.324,115.655 291.676,73.345"/>
> 	<polygon fill="black" stroke-width="1" points="291.676,73.345 282.248,73.7 287.863,81.974"/>
> 	<text x="265.5" y="115.5" font-family="Times New Roman" font-size="20">a</text>
> 	<polygon stroke="black" stroke-width="1" points="223.706,155.547 265.294,205.453"/>
> 	<polygon fill="black" stroke-width="1" points="265.294,205.453 264.014,196.107 256.332,202.509"/>
> 	<text x="230.5" y="200.5" font-family="Times New Roman" font-size="20">c</text>
> 	<polygon stroke="black" stroke-width="1" points="234.5,132.5 345.5,132.5"/>
> 	<polygon fill="black" stroke-width="1" points="345.5,132.5 337.5,127.5 337.5,137.5"/>
> 	<text x="285.5" y="153.5" font-family="Times New Roman" font-size="20">b</text>
> 	<polygon stroke="black" stroke-width="1" points="305.139,206.727 354.861,154.273"/>
> 	<polygon fill="black" stroke-width="1" points="354.861,154.273 345.729,156.639 352.987,163.518"/>
> 	<text x="335.5" y="201.5" font-family="Times New Roman" font-size="20">b, c</text>
> 	<polygon stroke="black" stroke-width="1" points="314.5,228.5 417.5,228.5"/>
> 	<polygon fill="black" stroke-width="1" points="417.5,228.5 409.5,223.5 409.5,233.5"/>
> 	<text x="361.5" y="249.5" font-family="Times New Roman" font-size="20">a</text>
> </svg>
>
> Each right-most state has more connected paths, but the amount increases exponentially as we increase the number of states. Notice, any state set that contains a 1, 4, or 6 (includes an accepting state from the NFA) is accepting!

When converting an NFA to DFA, for all reachable states we need to ask:

1. What states can I be in at the start?

2. From that state, 

   - Where can I go on an ‘a’?

   - Where can I go on a ‘b’?

   - Where can I go on a ‘c’?

3. Repeat step 2 for all reachable states

==**Every DFA is an NFA**==, ==**Every NFA ca be converted into a DFA**==. 

# $\epsilon$ - NFAs

We can change states without consuming an input symbol! This is a  *free pass* to a new state. It makes it easier to “glue” smaller automata together. 

<svg width="700" height="350" version="1.1" xmlns="http://www.w3.org/2000/svg">
	<ellipse stroke="black" stroke-width="1" fill="none" cx="155.5" cy="165.5" rx="30" ry="30"/>
	<text x="150.5" y="171.5" font-family="Times New Roman" font-size="20">1</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="241.5" cy="100.5" rx="30" ry="30"/>
	<text x="236.5" y="106.5" font-family="Times New Roman" font-size="20">2</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="356.5" cy="100.5" rx="30" ry="30"/>
	<text x="351.5" y="106.5" font-family="Times New Roman" font-size="20">3</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="467.5" cy="100.5" rx="30" ry="30"/>
	<text x="462.5" y="106.5" font-family="Times New Roman" font-size="20">4</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="582.5" cy="100.5" rx="30" ry="30"/>
	<text x="577.5" y="106.5" font-family="Times New Roman" font-size="20">5</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="582.5" cy="100.5" rx="24" ry="24"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="292.5" cy="221.5" rx="30" ry="30"/>
	<text x="287.5" y="227.5" font-family="Times New Roman" font-size="20">6</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="292.5" cy="221.5" rx="24" ry="24"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="473.5" cy="221.5" rx="30" ry="30"/>
	<text x="468.5" y="227.5" font-family="Times New Roman" font-size="20">7</text>
	<polygon stroke="black" stroke-width="1" points="179.433,147.411 217.567,118.589"/>
	<polygon fill="black" stroke-width="1" points="217.567,118.589 208.17,119.424 214.2,127.401"/>
	<text x="203.5" y="153.5" font-family="Times New Roman" font-size="20">&#949;</text>
	<polygon stroke="black" stroke-width="1" points="497.5,100.5 552.5,100.5"/>
	<polygon fill="black" stroke-width="1" points="552.5,100.5 544.5,95.5 544.5,105.5"/>
	<text x="520.5" y="121.5" font-family="Times New Roman" font-size="20">b</text>
	<polygon stroke="black" stroke-width="1" points="386.5,100.5 437.5,100.5"/>
	<polygon fill="black" stroke-width="1" points="437.5,100.5 429.5,95.5 429.5,105.5"/>
	<text x="407.5" y="121.5" font-family="Times New Roman" font-size="20">a</text>
	<polygon stroke="black" stroke-width="1" points="271.5,100.5 326.5,100.5"/>
	<polygon fill="black" stroke-width="1" points="326.5,100.5 318.5,95.5 318.5,105.5"/>
	<text x="294.5" y="121.5" font-family="Times New Roman" font-size="20">c</text>
	<path stroke="black" stroke-width="1" fill="none" d="M 446.153,233.757 A 188.437,188.437 0 0 1 319.847,233.757"/>
	<polygon fill="black" stroke-width="1" points="446.153,233.757 436.94,231.727 440.291,241.149"/>
	<text x="378.5" y="265.5" font-family="Times New Roman" font-size="20">a</text>
	<path stroke="black" stroke-width="1" fill="none" d="M 321.205,212.835 A 263.937,263.937 0 0 1 444.795,212.835"/>
	<polygon fill="black" stroke-width="1" points="321.205,212.835 330.153,215.823 327.812,206.101"/>
	<text x="378.5" y="196.5" font-family="Times New Roman" font-size="20">a</text>
	<polygon stroke="black" stroke-width="1" points="183.27,176.851 264.73,210.149"/>
	<polygon fill="black" stroke-width="1" points="264.73,210.149 259.217,202.494 255.433,211.75"/>
	<text x="210.5" y="214.5" font-family="Times New Roman" font-size="20">&#949;</text>
	<path stroke="black" stroke-width="1" fill="none" d="M 297.26,251.001 A 22.5,22.5 0 1 1 271.979,243.223"/>
	<text x="241.5" y="307.5" font-family="Times New Roman" font-size="20">b, c</text>
	<polygon fill="black" stroke-width="1" points="271.979,243.223 262.579,244.027 268.583,252.024"/>
	<path stroke="black" stroke-width="1" fill="none" d="M 500.905,233.414 A 22.5,22.5 0 1 1 480.713,250.499"/>
	<text x="522.5" y="293.5" font-family="Times New Roman" font-size="20">b, c</text>
	<polygon fill="black" stroke-width="1" points="480.713,250.499 476.318,258.847 486.291,258.108"/>
</svg>

Considering the above on ‘caba’,

|    Read    |   Unread   |   State   |
| :--------: | :--------: | :-------: |
| $\epsilon$ |   ‘caba’   | {1, 2, 6} |
|    ‘c’     |   ‘aba’    |  {3, 6}   |
|    ‘ca’    |    ‘ba’    |  {4, 7}   |
|   ‘cab’    |    ‘a’     |  {5, 7}   |
|   ‘caba’   | $\epsilon$ |    {6}    |

So we accept.

### Converting $\epsilon$ - NFA to DFA

Where can I get to an ‘a’? Also following any $\epsilon$’s before or after the ‘a’.

<svg width="600" height="230" version="1.1" xmlns="http://www.w3.org/2000/svg">
	<ellipse stroke="black" stroke-width="1" fill="none" cx="234.5" cy="121.5" rx="30" ry="30"/>
	<text x="204.5" y="127.5" font-family="Times New Roman" font-size="20">{1,2,6}</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="416.5" cy="46.5" rx="30" ry="30"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="416.5" cy="121.5" rx="30" ry="30"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="416.5" cy="196.5" rx="30" ry="30"/>
	<polygon stroke="black" stroke-width="1" points="262.237,110.07 388.763,57.93"/>
	<polygon fill="black" stroke-width="1" points="388.763,57.93 379.461,56.355 383.271,65.601"/>
	<text x="330.5" y="105.5" font-family="Times New Roman" font-size="20">a</text>
	<polygon stroke="black" stroke-width="1" points="264.5,121.5 386.5,121.5"/>
	<polygon fill="black" stroke-width="1" points="386.5,121.5 378.5,116.5 378.5,126.5"/>
	<text x="320.5" y="142.5" font-family="Times New Roman" font-size="20">b</text>
	<polygon stroke="black" stroke-width="1" points="262.237,132.93 388.763,185.07"/>
	<polygon fill="black" stroke-width="1" points="388.763,185.07 383.271,177.399 379.461,186.645"/>
	<text x="311.5" y="180.5" font-family="Times New Roman" font-size="20">c</text>
</svg>

### Simulator

The states = $\epsilon$-closure ($\{q_0\}$), where closure are the states from $q_0$ (start state) that we can also reach by following $\epsilon$.

```python
while not eof do:
    ch = read(c)
    states = e-closure(union of delta(q, ch) for all q in states)
end do

return (intersection of states, A) != empty
```

So in the above example, $\epsilon$-closure({1}) = {1, 2, 6}.

We can always convert $\epsilon$ - NFAs to a DFA $\to$ $\epsilon$ - NFAs exactly recognize regular languages. This is part of Kleene’s Thm.

==**Kleene**==: regexp $\implies$ $\epsilon$ - NFA $\implies$ DFA

1. $\empty$

   <svg width="200" height="100" version="1.1" xmlns="http://www.w3.org/2000/svg">
   	<ellipse stroke="black" stroke-width="1" fill="none" cx="71.5" cy="42.5" rx="30" ry="30"/>
   	<polygon stroke="black" stroke-width="1" points="10.5,42.5 41.5,42.5"/>
   	<polygon fill="black" stroke-width="1" points="41.5,42.5 33.5,37.5 33.5,47.5"/>
   </svg>

2. $\epsilon$

   <svg width="200" height="100" version="1.1" xmlns="http://www.w3.org/2000/svg">
   	<ellipse stroke="black" stroke-width="1" fill="none" cx="71.5" cy="42.5" rx="30" ry="30"/>
   	<ellipse stroke="black" stroke-width="1" fill="none" cx="71.5" cy="42.5" rx="24" ry="24"/>
   	<polygon stroke="black" stroke-width="1" points="10.5,42.5 41.5,42.5"/>
   	<polygon fill="black" stroke-width="1" points="41.5,42.5 33.5,37.5 33.5,47.5"/>
   </svg>

3. ‘a’

   <svg width="250" height="100" version="1.1" xmlns="http://www.w3.org/2000/svg">
   	<ellipse stroke="black" stroke-width="1" fill="none" cx="71.5" cy="42.5" rx="30" ry="30"/>
   	<ellipse stroke="black" stroke-width="1" fill="none" cx="189.5" cy="42.5" rx="30" ry="30"/>
   	<ellipse stroke="black" stroke-width="1" fill="none" cx="189.5" cy="42.5" rx="24" ry="24"/>
   	<polygon stroke="black" stroke-width="1" points="10.5,42.5 41.5,42.5"/>
   	<polygon fill="black" stroke-width="1" points="41.5,42.5 33.5,37.5 33.5,47.5"/>
   	<polygon stroke="black" stroke-width="1" points="101.5,42.5 159.5,42.5"/>
   	<polygon fill="black" stroke-width="1" points="159.5,42.5 151.5,37.5 151.5,47.5"/>
   	<text x="126.5" y="63.5" font-family="Times New Roman" font-size="20">a</text>
   </svg>

4. $E_1 | E_2$

   We connect a new start state to the start states of $E_1$ and $E_2$ with $\epsilon$ paths.

5. $E_1E_2$

   We connect the accepting states from $E_1$ to the start states of $E_2$ with $\epsilon$ paths. The accepting states in $E_1$ are now regular states.

6. $E^*$

   We make a new starting state $q_0$, join it to the starting state of $E$ with $\epsilon$, and join the accepting states of $E$ back to $q_0$. Notice that $q_0$ is thus also an accepting state.

## Scanning

When creating our assembler, we simply have to create a DFA! This is a simplified tokenizer:

<svg width="700" height="500" version="1.1" xmlns="http://www.w3.org/2000/svg">
	<ellipse stroke="black" stroke-width="1" fill="none" cx="202.5" cy="151.5" rx="30" ry="30"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="372.5" cy="69.5" rx="30" ry="30"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="372.5" cy="69.5" rx="24" ry="24"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="407.5" cy="151.5" rx="30" ry="30"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="407.5" cy="151.5" rx="24" ry="24"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="407.5" cy="245.5" rx="30" ry="30"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="407.5" cy="245.5" rx="24" ry="24"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="385.5" cy="329.5" rx="30" ry="30"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="385.5" cy="329.5" rx="24" ry="24"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="208.5" cy="393.5" rx="30" ry="30"/>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="208.5" cy="393.5" rx="24" ry="24"/>
	<polygon stroke="black" stroke-width="1" points="141.5,151.5 172.5,151.5"/>
	<polygon fill="black" stroke-width="1" points="172.5,151.5 164.5,146.5 164.5,156.5"/>
	<polygon stroke="black" stroke-width="1" points="229.521,138.466 345.479,82.534"/>
	<polygon fill="black" stroke-width="1" points="345.479,82.534 336.101,81.506 340.446,90.513"/>
	<text x="243.5" y="101.5" font-family="Times New Roman" font-size="20">label</text>
	<polygon stroke="black" stroke-width="1" points="232.5,151.5 377.5,151.5"/>
	<polygon fill="black" stroke-width="1" points="377.5,151.5 369.5,146.5 369.5,156.5"/>
	<text x="300.5" y="172.5" font-family="Times New Roman" font-size="20">#</text>
	<polygon stroke="black" stroke-width="1" points="229.77,164.004 380.23,232.996"/>
	<polygon fill="black" stroke-width="1" points="380.23,232.996 375.042,225.116 370.874,234.206"/>
	<text x="295.5" y="219.5" font-family="Times New Roman" font-size="20">,</text>
	<polygon stroke="black" stroke-width="1" points="224.005,172.417 363.995,308.583"/>
	<polygon fill="black" stroke-width="1" points="363.995,308.583 361.747,299.42 354.774,306.589"/>
	<text x="218.5" y="261.5" font-family="Times New Roman" font-size="20">keyword</text>
	<polygon stroke="black" stroke-width="1" points="203.244,181.491 207.756,363.509"/>
	<polygon fill="black" stroke-width="1" points="207.756,363.509 212.557,355.388 202.56,355.636"/>
	<text x="140.5" y="278.5" font-family="Times New Roman" font-size="20">register</text>
	<path stroke="black" stroke-width="1" fill="none" d="M 178.86,397.639 A 124.443,124.443 0 0 1 172.692,148.835"/>
	<polygon fill="black" stroke-width="1" points="172.692,148.835 164.539,144.088 164.852,154.083"/>
	<path stroke="black" stroke-width="1" fill="none" d="M 202.053,121.62 A 98.247,98.247 0 0 1 349.393,50.55"/>
	<polygon fill="black" stroke-width="1" points="202.053,121.62 208.104,114.382 198.199,113.009"/>
</svg>

This is our tokenizer; it’s scanning and finding what we have. So from this, is C regular?

- C Keywords
- Identifiers
- Literals
- Operators (`+`, `-`, `*`, `/`, `%`)
- Comments (`/*`, `//`)
- Punctuation

A valid sequence of these is also a regular language, since there are a finite amount of combinations. Thus we can use a finite automata to tokenize (scan) our input.

**<u>Note:</u>** though there may be infinite combinations, not all of them are valid C code. 

We need:

- Input string $w$ (source code)
- Break $w$ into $w_1, w_2, \cdots , w_n$ such that $w_i \in L$ (C tokens)
  - Else, error
- Output each $w_i$

$L = \text{{valid C tokens}}$ is regular, $LL^* = \text{{1 or more valid C tokens concatenated}}$.

**<u>Question</u>**: Does this guarantee a unique decomposition? `++` is one token, but `+` and `+` are two tokens. :open_mouth:

