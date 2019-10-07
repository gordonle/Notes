CS348 | September 19, 2019

# SQL

SQL, or ==Structured Query Language==, is based on the relational calculus we were doing before. There are three major parts of the language:

1. DML (==Data Manipulation Language==)

   This means the languages in which *queries* and *updates* are made.

2. DDL (==Data Definition Language==)

   This defines the *schema* for relations, and creates/modifies/destroys database objects.

3. DCL (==Data Control Language==)

   This gives access control to the items in our database.

There are attributes in SQL which define our information. Data types such as `integer` (32 bit), `smallint` (16bit), `float` (IEEE float), `char(n)` which is a character string of length $n$, etc.

So revisiting our sample database of authors and publications, 

```
AUTHOR(aid integer, name char(20))
WROTE(author integer, publication char(8))
PUBLICATION(pubid char(8), title char(70))
...
```

==Note==: SQL is **not** case sensitive. 

## The Basic “SELECT Block”

The basic syntax defines `SELECT DISTINCT` (results), `FROM` (tables) and `WHERE` (condition). This allows us to formulate conjunctive queries of the form
$$
\{\text{<results>} | \exist\text{<unused>}.(\and\text{<tables>})\and\text{<condition>}\}
$$
where <results> specifies values in the resulting tuples from the conjunction of <tables> with <condition>. <unused> are variables *<u>not used</u>* in <results>. 

Where Relational Calculus uses *positional* notation, SQL uses *correlations* (tuple variables) and *attribute names* to assign *default variable names* to components of tuples: $R[\text{AS}]p$ in SQL stands for $R(p.a_1,...,p.a_n)$ in relational calculus, where $a_1,...,a_k$ are the *attribute names* declared for $R$. 

> To list all publications with at least two authors, in RC we would say 
> $$
> \{p | \exists a_1, a_2.WROTE(a_1,p)\and WROTE(a_2,p)\and a_1\ne a_2\}
> $$
> In SQL,
>
> ```
> SQL> select distinct r1.publication
> 	2 from wrote r1, wrote r2
> 	3 where r1.publication = r2.publication
> 	4 and r1.author != r2.author
> ```
>
> Here we cannot share a variable $p$ in the two <WROTE> relations. So we need to explicitly equate `r1.publication = r2.publication`.

### “FROM” Clause

Syntax is as follows: $\text{FROM } R_1[[\text{AS}]n_1],...,R_k[[AS]n_k]$ , where

- $R_i$ are relation (table) names
- $n_i$ are distinct identifiers
- The clause represents a **conjunction** $R_1\and ...\and R_k$ where
  - all variables of $R_i$ are distinct
  - we use (co)relation names to resolve ambiguities
- they can ONLY appear as part of the *select block*

### “SELECT” Clause

Syntax: $\text{SELECT DISTINCT } e_1[[AS]n_1],...,e_k[[AS]n_k]$. Here we eliminate superfluous attributes from answers ($\exists$). We can now form expressions with built-in functions applied to the values of the attributes. This also gives names to attributes in the answer. 

> For every article list the number of pages
>
> ```
> SQL> select distinct pubid, endpage-startpage+1
> 	2 from article
> 	
> RETURNS
> PUBID     ENDPAGE-STARTPAGE+1
> -----     -------------------
> ChTo98                     40
> ChTo98a                    28
> Tom97                      19
> ```