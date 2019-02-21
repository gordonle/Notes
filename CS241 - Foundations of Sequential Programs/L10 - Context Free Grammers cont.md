CS241 L10 | February 7, 2019

# Context Free Grammars

Consider these expressions and languages.

$\Sigma_1 = \{a,b,c,+,-,*,/\}$, $L_1=\{\text{arithmetic expressions over }\Sigma_1\}$ The grammar would then be:

 $s \to \text{a | b | c | S OP S}$, and $OP \to \text{+ | - | * | /}$.

$\Sigma_2 = \Sigma_1 \cup \{(,)\} $, and $L_2 = \{ \text{arithmetic expressions over }\Sigma_2\}$. The grammar would then be:

$s \to \text{a | b | c | S OP S | (S)}$, with $OP \to \text{+ | - | * | /}$.

So, lets show the derivation for $s \implies^* a + b$.
$$
\begin{align}
	s &\implies^*a+b
	\\ &\implies S \:\: OP \:\: S \:\:\:\text{ (we have a choice of which non-terminal to substitute)}
	\\ &\implies a \:\: OP \:\: S
	\\ &\implies a \:\: + \:\: S
	\\ &\implies a + b
\end{align}
$$
==Leftmost Derivation==: we always expand the leftmost non-terminal. Similarly, we can do ==rightmost derivation==. 

Derivations can be expressed naturally and succinctly as a tree:

<svg width="500" height="275" version="1.1" xmlns="http://www.w3.org/2000/svg">
	<ellipse stroke="black" stroke-width="1" fill="none" cx="206.5" cy="37.5" rx="30" ry="30"/>
	<text x="202.5" y="43.5" font-family="Times New Roman" font-size="20">s</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="116.5" cy="131.5" rx="30" ry="30"/>
	<text x="110.5" y="137.5" font-family="Times New Roman" font-size="20">S</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="206.5" cy="131.5" rx="30" ry="30"/>
	<text x="193.5" y="137.5" font-family="Times New Roman" font-size="20">OP</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="297.5" cy="131.5" rx="30" ry="30"/>
	<text x="291.5" y="137.5" font-family="Times New Roman" font-size="20">S</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="77.5" cy="223.5" rx="30" ry="30"/>
	<text x="73.5" y="229.5" font-family="Times New Roman" font-size="20">a</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="206.5" cy="223.5" rx="30" ry="30"/>
	<text x="200.5" y="229.5" font-family="Times New Roman" font-size="20">+</text>
	<ellipse stroke="black" stroke-width="1" fill="none" cx="325.5" cy="223.5" rx="30" ry="30"/>
	<text x="320.5" y="229.5" font-family="Times New Roman" font-size="20">b</text>
	<polygon stroke="black" stroke-width="1" points="185.753,59.169 137.247,109.831"/>
	<polygon fill="black" stroke-width="1" points="137.247,109.831 146.391,107.51 139.168,100.594"/>
	<polygon stroke="black" stroke-width="1" points="104.791,159.121 89.209,195.879"/>
	<polygon fill="black" stroke-width="1" points="89.209,195.879 96.935,190.465 87.728,186.562"/>
	<polygon stroke="black" stroke-width="1" points="206.5,161.5 206.5,193.5"/>
	<polygon fill="black" stroke-width="1" points="206.5,193.5 211.5,185.5 201.5,185.5"/>
	<polygon stroke="black" stroke-width="1" points="206.5,67.5 206.5,101.5"/>
	<polygon fill="black" stroke-width="1" points="206.5,101.5 211.5,93.5 201.5,93.5"/>
	<polygon stroke="black" stroke-width="1" points="227.366,59.054 276.634,109.946"/>
	<polygon fill="black" stroke-width="1" points="276.634,109.946 274.662,100.72 267.477,107.676"/>
	<polygon stroke="black" stroke-width="1" points="306.235,160.2 316.765,194.8"/>
	<polygon fill="black" stroke-width="1" points="316.765,194.8 319.219,185.691 309.652,188.602"/>
</svg>

Every leftmost (or rightmost) derivation corresponds to a **unique** ==parse tree==.

## Ambiguity

> **Ex:** leftmost derivation for $\text{a+b*c}$.
>
> $ s \implies S \:\:OP \:\:S \implies a \:\:OP \:\:S \implies a + S \implies a + S \:\:OP \:\:S \implies a + b \:\:OP\:\:S \implies a+b*S \implies a + b * c$ 
>
> We could also expand our non-terminals first, getting $s\implies S\:\:OP\:\:S\:\:OP\:\:S$. Then these two paths have created two different trees!
>
> <svg width="765" height="350" version="1.1" xmlns="http://www.w3.org/2000/svg">
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="161.5" cy="33.5" rx="30" ry="30"/>
> 	<text x="157.5" y="39.5" font-family="Times New Roman" font-size="20">s</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="67.5" cy="113.5" rx="30" ry="30"/>
> 	<text x="61.5" y="119.5" font-family="Times New Roman" font-size="20">S</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="161.5" cy="113.5" rx="30" ry="30"/>
> 	<text x="148.5" y="119.5" font-family="Times New Roman" font-size="20">OP</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="262.5" cy="113.5" rx="30" ry="30"/>
> 	<text x="256.5" y="119.5" font-family="Times New Roman" font-size="20">S</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="47.5" cy="212.5" rx="30" ry="30"/>
> 	<text x="43.5" y="218.5" font-family="Times New Roman" font-size="20">a</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="115.5" cy="212.5" rx="30" ry="30"/>
> 	<text x="109.5" y="218.5" font-family="Times New Roman" font-size="20">+</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="196.5" cy="212.5" rx="30" ry="30"/>
> 	<text x="190.5" y="218.5" font-family="Times New Roman" font-size="20">S</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="270.5" cy="212.5" rx="30" ry="30"/>
> 	<text x="257.5" y="218.5" font-family="Times New Roman" font-size="20">OP</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="341.5" cy="212.5" rx="30" ry="30"/>
> 	<text x="335.5" y="218.5" font-family="Times New Roman" font-size="20">S</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="196.5" cy="290.5" rx="30" ry="30"/>
> 	<text x="191.5" y="296.5" font-family="Times New Roman" font-size="20">b</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="270.5" cy="290.5" rx="30" ry="30"/>
> 	<text x="265.5" y="296.5" font-family="Times New Roman" font-size="20">*</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="341.5" cy="290.5" rx="30" ry="30"/>
> 	<text x="337.5" y="296.5" font-family="Times New Roman" font-size="20">c</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="617.5" cy="33.5" rx="30" ry="30"/>
> 	<text x="613.5" y="39.5" font-family="Times New Roman" font-size="20">s</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="503.5" cy="113.5" rx="30" ry="30"/>
> 	<text x="497.5" y="119.5" font-family="Times New Roman" font-size="20">S</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="617.5" cy="113.5" rx="30" ry="30"/>
> 	<text x="604.5" y="119.5" font-family="Times New Roman" font-size="20">OP</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="696.5" cy="113.5" rx="30" ry="30"/>
> 	<text x="690.5" y="119.5" font-family="Times New Roman" font-size="20">S</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="431.5" cy="212.5" rx="30" ry="30"/>
> 	<text x="425.5" y="218.5" font-family="Times New Roman" font-size="20">S</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="503.5" cy="212.5" rx="30" ry="30"/>
> 	<text x="490.5" y="218.5" font-family="Times New Roman" font-size="20">OP</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="577.5" cy="212.5" rx="30" ry="30"/>
> 	<text x="571.5" y="218.5" font-family="Times New Roman" font-size="20">S</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="431.5" cy="290.5" rx="30" ry="30"/>
> 	<text x="427.5" y="296.5" font-family="Times New Roman" font-size="20">a</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="503.5" cy="288.5" rx="30" ry="30"/>
> 	<text x="497.5" y="294.5" font-family="Times New Roman" font-size="20">+</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="577.5" cy="288.5" rx="30" ry="30"/>
> 	<text x="572.5" y="294.5" font-family="Times New Roman" font-size="20">b</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="649.5" cy="212.5" rx="30" ry="30"/>
> 	<text x="644.5" y="218.5" font-family="Times New Roman" font-size="20">*</text>
> 	<ellipse stroke="black" stroke-width="1" fill="none" cx="718.5" cy="212.5" rx="30" ry="30"/>
> 	<text x="714.5" y="218.5" font-family="Times New Roman" font-size="20">c</text>
> 	<polygon stroke="black" stroke-width="1" points="138.654,52.944 90.346,94.056"/>
> 	<polygon fill="black" stroke-width="1" points="90.346,94.056 99.679,92.679 93.198,85.064"/>
> 	<polygon stroke="black" stroke-width="1" points="61.559,142.906 53.441,183.094"/>
> 	<polygon fill="black" stroke-width="1" points="53.441,183.094 59.926,176.243 50.124,174.262"/>
> 	<polygon stroke="black" stroke-width="1" points="148.859,140.707 128.141,185.293"/>
> 	<polygon fill="black" stroke-width="1" points="128.141,185.293 136.047,180.145 126.978,175.932"/>
> 	<polygon stroke="black" stroke-width="1" points="161.5,63.5 161.5,83.5"/>
> 	<polygon fill="black" stroke-width="1" points="161.5,83.5 166.5,75.5 156.5,75.5"/>
> 	<polygon stroke="black" stroke-width="1" points="185.017,52.127 238.983,94.873"/>
> 	<polygon fill="black" stroke-width="1" points="238.983,94.873 235.817,85.986 229.608,93.825"/>
> 	<polygon stroke="black" stroke-width="1" points="245.859,138.462 213.141,187.538"/>
> 	<polygon fill="black" stroke-width="1" points="213.141,187.538 221.739,183.656 213.418,178.109"/>
> 	<polygon stroke="black" stroke-width="1" points="264.916,143.403 268.084,182.597"/>
> 	<polygon fill="black" stroke-width="1" points="268.084,182.597 272.423,174.221 262.456,175.026"/>
> 	<polygon stroke="black" stroke-width="1" points="281.212,136.949 322.788,189.051"/>
> 	<polygon fill="black" stroke-width="1" points="322.788,189.051 321.706,179.679 313.89,185.916"/>
> 	<polygon stroke="black" stroke-width="1" points="196.5,242.5 196.5,260.5"/>
> 	<polygon fill="black" stroke-width="1" points="196.5,260.5 201.5,252.5 191.5,252.5"/>
> 	<polygon stroke="black" stroke-width="1" points="270.5,242.5 270.5,260.5"/>
> 	<polygon fill="black" stroke-width="1" points="270.5,260.5 275.5,252.5 265.5,252.5"/>
> 	<polygon stroke="black" stroke-width="1" points="341.5,242.5 341.5,260.5"/>
> 	<polygon fill="black" stroke-width="1" points="341.5,260.5 346.5,252.5 336.5,252.5"/>
> 	<polygon stroke="black" stroke-width="1" points="592.943,50.733 528.057,96.267"/>
> 	<polygon fill="black" stroke-width="1" points="528.057,96.267 537.477,95.765 531.733,87.579"/>
> 	<polygon stroke="black" stroke-width="1" points="617.5,63.5 617.5,83.5"/>
> 	<polygon fill="black" stroke-width="1" points="617.5,83.5 622.5,75.5 612.5,75.5"/>
> 	<polygon stroke="black" stroke-width="1" points="638.579,54.846 675.421,92.154"/>
> 	<polygon fill="black" stroke-width="1" points="675.421,92.154 673.357,82.948 666.242,89.975"/>
> 	<polygon stroke="black" stroke-width="1" points="485.855,137.762 449.145,188.238"/>
> 	<polygon fill="black" stroke-width="1" points="449.145,188.238 457.894,184.709 449.807,178.827"/>
> 	<polygon stroke="black" stroke-width="1" points="503.5,143.5 503.5,182.5"/>
> 	<polygon fill="black" stroke-width="1" points="503.5,182.5 508.5,174.5 498.5,174.5"/>
> 	<polygon stroke="black" stroke-width="1" points="521.461,137.529 559.539,188.471"/>
> 	<polygon fill="black" stroke-width="1" points="559.539,188.471 558.754,179.07 550.744,185.057"/>
> 	<polygon stroke="black" stroke-width="1" points="626.727,142.046 640.273,183.954"/>
> 	<polygon fill="black" stroke-width="1" points="640.273,183.954 642.57,174.804 633.055,177.88"/>
> 	<polygon stroke="black" stroke-width="1" points="703.008,142.786 711.992,183.214"/>
> 	<polygon fill="black" stroke-width="1" points="711.992,183.214 715.138,174.32 705.376,176.49"/>
> 	<polygon stroke="black" stroke-width="1" points="431.5,242.5 431.5,260.5"/>
> 	<polygon fill="black" stroke-width="1" points="431.5,260.5 436.5,252.5 426.5,252.5"/>
> 	<polygon stroke="black" stroke-width="1" points="503.5,242.5 503.5,258.5"/>
> 	<polygon fill="black" stroke-width="1" points="503.5,258.5 508.5,250.5 498.5,250.5"/>
> 	<polygon stroke="black" stroke-width="1" points="577.5,242.5 577.5,258.5"/>
> 	<polygon fill="black" stroke-width="1" points="577.5,258.5 582.5,250.5 572.5,250.5"/>
> </svg>
>
> But these can be interpreted differently! This means that our grammar is **ambiguous**. The **left** tree is correct.

We do NOT want ambiguous grammars! One correct interpretation for every derivation is what we want.

- Formal Languages: often care about accept/reject states
- Compiler (practical things): don’t want ambiguity.
  - We also want to know *why* a $w \in L(G)$, where $w$ is a token of a program and $L(G)$ is the spec of a language
- Shape of the parse tree: describes the “meaning” of the input with respect to the grammar
  - an input that has more than one parse tree may have multiple meanings

How can we fix ambiguity?

> **Ex:**
>
> ```text
> if then
> if then
> else
> ```
>
> Which `if` statement does the `else` belong to? Depends what our compiler has, this might be a special sequence of tokens that makes the `else` belong to the (inner/outer) `if`. Who knows? In `Python`, they force us to use indentation to specify what belongs where. This isn’t implemented in `C` though.

1. Use heuristic (“precedence”) to guide the derivation process

2. Make the grammar unambiguous

   - this is not always possible - some grammars are inherently ambiguous

     > Fixing the unambiguity from the example above, 
     >
     > $E \to E \:\: OP \:\: T \:\:| \:\: T$, 
     >
     > $T \to\text{a | b | c | (E)}​$, 
     >
     > $OP \to \text{+ | - | * | / }$. Then
     >
     > $a+b*c: E\implies E\:\:OP\:\:T\implies E\:\:OP\:\:T\:\:OP\:\:T\implies T\:\:OP\:\:T\:\:OP\:\:T \implies \cdots\implies a+b*c​$ .
     >
     > This will build the 2^nd^, rightmost tree. But we said the left one was correct!

     A good ==exam question==: how do we add exponents to our grammar?

     What if we want multiplication and division to have higher precedence over addition and subtraction? We split $OP$ into two different sections - `*, /` and `+, -`. The idea is to have the `+, -` at the top of the tree and have the `*, /` appear lower down in the tree. 

   >To fix this, we build `+,-` form first, then at a lower level we add the `*, /`.
   >
   >$E \to\text{$E$ $PM$ $T$ | $T$}$
   >
   >$T \to\text{$T$ $\:TD$  $F$ | $F$}$
   >
   >$PM \to\text{+ | -}​$
   >
   >$TD\to\text{* | / }$
   >
   >$F\to\text{a | b | c | ($E$)}$
   >
   >Then with the input string $a+a*a-a/a$, it builds the tree
   >
   ><svg width="710" height="450" version="1.1" xmlns="http://www.w3.org/2000/svg">
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="394.5" cy="35.5" rx="30" ry="30"/>
   >	<text x="388.5" y="41.5" font-family="Times New Roman" font-size="20">E</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="212.5" cy="102.5" rx="30" ry="30"/>
   >	<text x="206.5" y="108.5" font-family="Times New Roman" font-size="20">E</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="394.5" cy="113.5" rx="30" ry="30"/>
   >	<text x="380.5" y="119.5" font-family="Times New Roman" font-size="20">PM</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="578.5" cy="102.5" rx="30" ry="30"/>
   >	<text x="572.5" y="108.5" font-family="Times New Roman" font-size="20">T</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="69.5" cy="182.5" rx="30" ry="30"/>
   >	<text x="63.5" y="188.5" font-family="Times New Roman" font-size="20">E</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="168.5" cy="182.5" rx="30" ry="30"/>
   >	<text x="154.5" y="188.5" font-family="Times New Roman" font-size="20">PM</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="315.5" cy="190.5" rx="30" ry="30"/>
   >	<text x="309.5" y="196.5" font-family="Times New Roman" font-size="20">T</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="394.5" cy="190.5" rx="30" ry="30"/>
   >	<text x="391.5" y="196.5" font-family="Times New Roman" font-size="20">-</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="477.5" cy="190.5" rx="30" ry="30"/>
   >	<text x="471.5" y="196.5" font-family="Times New Roman" font-size="20">T</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="69.5" cy="261.5" rx="30" ry="30"/>
   >	<text x="63.5" y="267.5" font-family="Times New Roman" font-size="20">T</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="69.5" cy="341.5" rx="30" ry="30"/>
   >	<text x="63.5" y="347.5" font-family="Times New Roman" font-size="20">F</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="168.5" cy="273.5" rx="30" ry="30"/>
   >	<text x="163.5" y="279.5" font-family="Times New Roman" font-size="20">+</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="243.5" cy="273.5" rx="30" ry="30"/>
   >	<text x="237.5" y="279.5" font-family="Times New Roman" font-size="20">T</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="315.5" cy="273.5" rx="30" ry="30"/>
   >	<text x="302.5" y="279.5" font-family="Times New Roman" font-size="20">TD</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="394.5" cy="273.5" rx="30" ry="30"/>
   >	<text x="388.5" y="279.5" font-family="Times New Roman" font-size="20">F</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="578.5" cy="190.5" rx="30" ry="30"/>
   >	<text x="565.5" y="196.5" font-family="Times New Roman" font-size="20">TD</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="672.5" cy="190.5" rx="30" ry="30"/>
   >	<text x="666.5" y="196.5" font-family="Times New Roman" font-size="20">F</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="212.5" cy="416.5" rx="30" ry="30"/>
   >	<text x="208.5" y="422.5" font-family="Times New Roman" font-size="20">a</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="69.5" cy="416.5" rx="30" ry="30"/>
   >	<text x="65.5" y="422.5" font-family="Times New Roman" font-size="20">a</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="315.5" cy="352.5" rx="30" ry="30"/>
   >	<text x="310.5" y="358.5" font-family="Times New Roman" font-size="20">*</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="394.5" cy="352.5" rx="30" ry="30"/>
   >	<text x="390.5" y="358.5" font-family="Times New Roman" font-size="20">a</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="212.5" cy="341.5" rx="30" ry="30"/>
   >	<text x="206.5" y="347.5" font-family="Times New Roman" font-size="20">F</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="477.5" cy="273.5" rx="30" ry="30"/>
   >	<text x="471.5" y="279.5" font-family="Times New Roman" font-size="20">F</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="477.5" cy="352.5" rx="30" ry="30"/>
   >	<text x="473.5" y="358.5" font-family="Times New Roman" font-size="20">a</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="672.5" cy="273.5" rx="30" ry="30"/>
   >	<text x="668.5" y="279.5" font-family="Times New Roman" font-size="20">a</text>
   >	<ellipse stroke="black" stroke-width="1" fill="none" cx="578.5" cy="273.5" rx="30" ry="30"/>
   >	<text x="575.5" y="279.5" font-family="Times New Roman" font-size="20">/</text>
   >	<polygon stroke="black" stroke-width="1" points="69.5,212.5 69.5,231.5"/>
   >	<polygon fill="black" stroke-width="1" points="69.5,231.5 74.5,223.5 64.5,223.5"/>
   >	<polygon stroke="black" stroke-width="1" points="69.5,291.5 69.5,311.5"/>
   >	<polygon fill="black" stroke-width="1" points="69.5,311.5 74.5,303.5 64.5,303.5"/>
   >	<polygon stroke="black" stroke-width="1" points="186.319,117.147 95.681,167.853"/>
   >	<polygon fill="black" stroke-width="1" points="95.681,167.853 105.104,168.311 100.222,159.584"/>
   >	<polygon stroke="black" stroke-width="1" points="198.042,128.786 182.958,156.214"/>
   >	<polygon fill="black" stroke-width="1" points="182.958,156.214 191.194,151.613 182.432,146.794"/>
   >	<polygon stroke="black" stroke-width="1" points="235.309,121.987 292.691,171.013"/>
   >	<polygon fill="black" stroke-width="1" points="292.691,171.013 289.857,162.015 283.361,169.618"/>
   >	<polygon stroke="black" stroke-width="1" points="168.5,212.5 168.5,243.5"/>
   >	<polygon fill="black" stroke-width="1" points="168.5,243.5 173.5,235.5 163.5,235.5"/>
   >	<polygon stroke="black" stroke-width="1" points="366.347,45.864 240.653,92.136"/>
   >	<polygon fill="black" stroke-width="1" points="240.653,92.136 249.888,94.064 246.433,84.68"/>
   >	<polygon stroke="black" stroke-width="1" points="394.5,65.5 394.5,83.5"/>
   >	<polygon fill="black" stroke-width="1" points="394.5,83.5 399.5,75.5 389.5,75.5"/>
   >	<polygon stroke="black" stroke-width="1" points="422.689,45.765 550.311,92.235"/>
   >	<polygon fill="black" stroke-width="1" points="550.311,92.235 544.504,84.8 541.083,94.196"/>
   >	<polygon stroke="black" stroke-width="1" points="394.5,143.5 394.5,160.5"/>
   >	<polygon fill="black" stroke-width="1" points="394.5,160.5 399.5,152.5 389.5,152.5"/>
   >	<polygon stroke="black" stroke-width="1" points="295.842,213.162 263.158,250.838"/>
   >	<polygon fill="black" stroke-width="1" points="263.158,250.838 272.177,248.072 264.624,241.519"/>
   >	<polygon stroke="black" stroke-width="1" points="315.5,220.5 315.5,243.5"/>
   >	<polygon fill="black" stroke-width="1" points="315.5,243.5 320.5,235.5 310.5,235.5"/>
   >	<polygon stroke="black" stroke-width="1" points="336.183,212.23 373.817,251.77"/>
   >	<polygon fill="black" stroke-width="1" points="373.817,251.77 371.923,242.528 364.68,249.422"/>
   >	<polygon stroke="black" stroke-width="1" points="69.5,371.5 69.5,386.5"/>
   >	<polygon fill="black" stroke-width="1" points="69.5,386.5 74.5,378.5 64.5,378.5"/>
   >	<polygon stroke="black" stroke-width="1" points="231.056,300.797 224.944,314.203"/>
   >	<polygon fill="black" stroke-width="1" points="224.944,314.203 232.812,308.998 223.713,304.849"/>
   >	<polygon stroke="black" stroke-width="1" points="212.5,371.5 212.5,386.5"/>
   >	<polygon fill="black" stroke-width="1" points="212.5,386.5 217.5,378.5 207.5,378.5"/>
   >	<polygon stroke="black" stroke-width="1" points="315.5,303.5 315.5,322.5"/>
   >	<polygon fill="black" stroke-width="1" points="315.5,322.5 320.5,314.5 310.5,314.5"/>
   >	<polygon stroke="black" stroke-width="1" points="394.5,303.5 394.5,322.5"/>
   >	<polygon fill="black" stroke-width="1" points="394.5,322.5 399.5,314.5 389.5,314.5"/>
   >	<polygon stroke="black" stroke-width="1" points="555.881,122.208 500.119,170.792"/>
   >	<polygon fill="black" stroke-width="1" points="500.119,170.792 509.435,169.307 502.866,161.767"/>
   >	<polygon stroke="black" stroke-width="1" points="578.5,132.5 578.5,160.5"/>
   >	<polygon fill="black" stroke-width="1" points="578.5,160.5 583.5,152.5 573.5,152.5"/>
   >	<polygon stroke="black" stroke-width="1" points="600.401,123.003 650.599,169.997"/>
   >	<polygon fill="black" stroke-width="1" points="650.599,169.997 648.176,160.88 641.342,168.18"/>
   >	<polygon stroke="black" stroke-width="1" points="578.5,220.5 578.5,243.5"/>
   >	<polygon fill="black" stroke-width="1" points="578.5,243.5 583.5,235.5 573.5,235.5"/>
   >	<polygon stroke="black" stroke-width="1" points="477.5,220.5 477.5,243.5"/>
   >	<polygon fill="black" stroke-width="1" points="477.5,243.5 482.5,235.5 472.5,235.5"/>
   >	<polygon stroke="black" stroke-width="1" points="477.5,303.5 477.5,322.5"/>
   >	<polygon fill="black" stroke-width="1" points="477.5,322.5 482.5,314.5 472.5,314.5"/>
   >	<polygon stroke="black" stroke-width="1" points="672.5,220.5 672.5,243.5"/>
   >	<polygon fill="black" stroke-width="1" points="672.5,243.5 677.5,235.5 667.5,235.5"/>
   ></svg>
   >
   >Does this apply BEDMAS though? Yes! Since we are doing left recursions, we evaluate from left to right. The left ones will be lower in the tree.

## Recognizer 

What class of computer programs is needed to recognize a context-free language?

- Regular Languages: DFA
- Context-Free Languages:
  - DFA + stack, something with infinite memory but in FILO order, called PDA (pushdown automata)

We want more than just accept and reject states though. We want the derivations (parse trees). The “problem” with finding the derivation is called ==“parsing”==.

> Given grammar $G$, start symbol $S$, string $w$, find $s\implies \cdots \implies w$ or `ERROR`.

