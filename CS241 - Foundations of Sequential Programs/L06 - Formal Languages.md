CS241 L06 | January 24, 2019

# Formal Languages

|             Assembly Languages              |                  High-level Languages                   |
| :-----------------------------------------: | :-----------------------------------------------------: |
|              Simple structure               |                      More complex                       |
| Recognition and translation into ML is easy | Harder to translate (1 keyword is many ML instructions) |

**How do we handle complexity?**

We want a formal theory of string recognition, which will be found upon general principles that work in the context of any programming language.

## Definitions

| Term                   | Definition                                                   | Example            |
| ---------------------- | ------------------------------------------------------------ | ------------------ |
| Alphabet               | A finite set of symbols, denoted $\Sigma = \{a, b, c\}$      | {a, b, c}          |
| Strings (or word)      | A finite sequence of symbols from $\Sigma$                   | a, aba, abbabaca   |
| Length of string $|w|$ | The number of characters/symbols in $w$                      | \|aba\| = 3        |
| Empty string           | An empty sequence of symbols, $\epsilon$ (not a symbol in $\Sigma $) | \|$\epsilon$\| = 0 |
| Language               | A set of strings                                             | {$a^{2n}b, n\ge0$} |

> **Note**: before and after any given character, there are an infinite number of $\epsilon$ . For example, if $w$ = $\epsilon$a$\epsilon$b$\epsilon$a$\epsilon$$\epsilon$, $|w|=3$.
>
> **Note 2:** $\epsilon$ is the empty string, and $\empty$ or $\{\}$ is the empty set. The language $\{\epsilon\}$ only contains the empty string. 

Symbols can be anything we want. **ie:** $\Sigma =$ {dot, dash}, L = { valid English words in Morse code }

**How do we recognize “automatically” if a given string belongs to a given language?**

Well it depends on the *complexity* of the language. Generally, the more cases or different values there are in a language, the more complex it is. For example, **math** or **MIPS** is relatively easy compared to modern languages such as C, C++, Java. Certain languages are so complex it’s impossible to tell.

## Language Classes

Languages are characterized according to how hard the recognition process is.

### Finite

There are only a finite number of possible strings. So given a string, is it in this language?

<u>Brute-force</u>: Store each string then compare with the stored strings. But we can be way more efficient.

The idea is to build a **tree** that holds every word. Check character by character until we hit either the end of the word, or an error. The run-time of this would be the length of the word!

> **Ex**: L = {cat, car, cow, catfish}, $\Sigma $ = {a, ..., z}

In the tree, our nodes will need the values `character`, and `isEnd` to see if it’s the end of a word. Scan from left to right as you traverse your language tree.

#### “scanner”

Used to tokenize an input. Most programming languages don’t have a finite number of programs.

### Regular

Languages in this class are built from finite languages. We are now allowed to use **unions**, **concatenations** and **repetitions**. 

| Building Block | Example                                           |
| -------------- | ------------------------------------------------- |
| Union          | $L_1 \cup L_2 = \{x | x\in L_1 \or x \in L_2\}$   |
| Concatentation | $L_1 \cdot L_2 = \{xy|x \in L_1 \and y\in L_2\}$  |
| Repetition     | $L^* = \{\epsilon\} \cup \{xy|x\in L^*, y\in L\}$ |

> **Ex:** Show that L = {$a^{2n}b, n\ge0$} is regular.
>
> $\implies (a \cdot a)^* \cdot b$ (this is in the world of *expressions*, not *sets*)
>
> $\implies \{\{a\}\cdot\{a\}\}^* \cdot \{b\}$

|      Regular Expression      |         Set Notation         | Description                               |
| :--------------------------: | :--------------------------: | ----------------------------------------- |
|           $\empty$           |             { }              | Empty language                            |
|          $\epsilon$          |        { $\epsilon$ }        | Language containing only the empty string |
|  $E_1 | E_2$ or $E_1 + E_2​$  |        $L_1 \cup L_2$        | Unions                                    |
| $E_1 \cdot E_2$ or ​$E_1 E_2​$ | $L_1 \cdot L_2$ or $L_1 L_2$ | Concatenations                            |
|            $E^*$             |            $L^*$             | Repetitions (Kleene stars)                |

#### Precedence

|       Rule        |          Example           |
| :---------------: | :------------------------: |
| * before $\cdot$  |     aa* $\equiv$ a(a)*     |
| $\cdot$ before \| | aa \| b $\equiv$ (aa) \| b |

> **Is C Regular?**
>
> A C program is ultimately a sequence of tokens, each of which comes from a regular language. There are a *finite number of tokens*. $\text{C}\subseteq \{\text{valid C tokens}\}^*$, but is C regular? Who knows :eyes:

How can we verify if a string is in {$a^{2n}b, n\ge0$}? 

```text
Tree structure:
        a
       <---
[start]--->[]
        b
       --->[end]
```

There are Deterministic Finite Automata (DFAs)

#### Deterministic Finite Automata

Formally, a DFA is a 5-tuple $M = (\Sigma , Q, q_0, A, \delta)$

| Symbol                                     | Definition                                                   |
| ------------------------------------------ | ------------------------------------------------------------ |
| $\Sigma$                                   | a finite, non-empty set                                      |
| $Q$                                        | A finite, non-empty set of states                            |
| $q_0 \in Q$                                | Start state                                                  |
| $A \subseteq Q$                            | Set of accepting states                                      |
| $\delta : (Q \times \Sigma) \rightarrow Q$ | Transition function. From a given state, on a given input symbol (one symbol), next state |



- Context-Free
- Context-Sensitive
- Recursive
- Recursively enumerable
- etc. (impossible)

