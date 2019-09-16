CS348 L02 | September 10, 2019

# Asking **Questions** (and understanding **Answers**)

> Find all pairs of (natural) numbers that add to 5!

**<u>Question</u>**: $\{(x,y)|\text{ PLUS}(x,y,5)\}$

**<u>Answer</u>**: $\{(0,5),(1,4),(2,3),(3,2),(4,1),(5,0)\}$

Why is this? It’s because it appears in the PLUS table! So we don’t actually need to understand anything about addition, as long as we have the addition table, we just need to find where the table returns a 5. 

> Find pairs of numbers that add to the same number as they subtract to!

<u>**Question**</u>: $\{(x,y)|\exists z, \text{ PLUS}(x,y.z) \and \text{PLUS}(z,y,x)\}$

**<u>Answer</u>**: $\{(0,0), (1,0), ...\}$ . Can (5,5) be in the answer set? It all depends on the content (instance) of PLUS.

> Find the neutral element of addition!

**<u>Question</u>**: $\{(x)|\text{ PLUS}(x,x,x)\}$

**<u>Answer</u>**: $\{(0)\}$

Now how would we ask questions about employees? Let’s look at this EMP table (employee table).

| Name | Dept | Boss |
| ---- | ---- | ---- |
| Sue  | CS   | Bob  |
| Bob  | CO   | Bob  |
| Fred | PM   | Mark |
| John | PM   | Mark |
| Jim  | CS   | Fred |
| Eve  | CS   | Fred |
| Sue  | PM   | Sue  |

> Find all employees who work for “Bob”!

**<u>Question</u>**: $\{(x,y)|\text{ EMP}(x,y,\text{Bob}\}$

<u>**Answer**</u>:  $\{(Sue, CS), (Bob, CO)\}$

Lots of different questions you can ask (ie. Who works for the same boss, who’s under the same depts, etc.)

# The Relational Model

The idea here is that all information is organized in a finite number of relations. These models have several components:

- Universe
  - a set of values $D$ with equality (=)
- Relation
  - a predicate named $R$, with arity $k$ of $R$ (the number of columns)
  - an ==instance== is a relation $R \subseteq D^k$
- Database
  - a ==signature== is a finite set of $\rho$ predicate names
  - each ==instance== is a relation $R_i$ for each $R_i$

> Here’s some notation: 				**Signature**: $\rho = (R_1,...,R_n)$ ,			**Instance**: $DB =(D,=,R_1,...,R_n)$

Each predicate (also called table headers) has a name, as well as attributes (or identifiers, label columns) that it stores (ie. $AUTHOR(aid, name)$, $PUBLICATION(pubid, title)$). An instance is a predicate with real information, and relations are sets of instances (a table).

## Simple (Atomic) “Truth”

Relationships between objects (tuples) that are present in an instance are *true*, relationships absent are *false*. 

## Query Conditions

An idea we can use here is to use variables to generalize conditions! So $AUTHOR(x,y)$ will be true of any valuation $\{x\mapsto a, y\mapsto b\}$ exactly when the pair $(a,b) \in AUTHOR$ 

Another idea is to use these simple queries and combine them to make more complicated queries, using logical connectives $(\and ,\or, \neg )$ and quantifiers $(\forall, \exists)$!

So, conditions can be formulated using the language of first-order logic! GIven a database schema $\rho = (R_1, ..., R_k)$ and a set of variable names $\{x_1, x_2, ...\}$, conditions are *formulas* defined by:
$$
\begin{align}
\varphi &::= R_i(x_{i_1},....,x_{i_k}) | x_i=x_j|\varphi\and\varphi|\exists x_i\cdot\varphi| \text{  (conjunctive)}\\
&::= R_i(x_{i_1},....,x_{i_k}) | x_i=x_j|\varphi\and\varphi|\exists x_i\cdot\varphi|\varphi\or\varphi \text{ (positive)}
\\&::= R_i(x_{i_1},....,x_{i_k}) | x_i=x_j|\varphi\and\varphi|\exists x_i\cdot\varphi|\varphi\or\varphi|\neg\varphi \text{ (first-order)}\\
\end{align}
$$

## First-order Variables and Valuations

How do we *interpret* these variables? A ==valuation== is a function $\Theta$ that maps *variable names* to values in the universe $\Theta : \{x_1,x_2,..\}\to D$. To denote a modification to $\Theta$ in which variable $x$ is instead mapped to value $v$, one writes $\Theta[x\mapsto v]$. 

The idea here is that answers to queries are equivalent to valuations of free variables that make the formula true, with respect to the database. 

# Relational Calculus

A ==query== in the relational calculus is a set comprehension of the form $\{(x_1, x_2, .., x_k) | \varphi\}​$.

An ==answer== to a query $\{(x_1, x_2, .., x_k) | \varphi\}$ over DB is the relation $\{(\Theta(x_1),...,\Theta(x_k))|DB, \Theta\models\varphi\}$, where $\{x_1,...,x_k\} = FV(\varphi)^\dagger$, or the free variables of $\varphi$.

## Sample Queries

Over numbers (with addition and multiplication):

- List all composite numbers

  $\text{COMP}=\{x | \exists y_1,y_2 : \text{ TIMES}(y_1, y_2, x) \and \neg(y_1 =x) \and \neg(y_2=x)\}$

- List all prime numbers

  $\text{PRIME} = \{x | \neg\text{COMP}(x)\}​$

 Over the bibliography database:

- List all publications

  $\{x|\exists y : \text{ PUBLICATION}(y,x)\}$

- List titles of all books

  $\{y|\exists x, z, w : \text{ BOOK}(x,z,w)\and\text{PUBLICATION}(x,y)\}​$

- 