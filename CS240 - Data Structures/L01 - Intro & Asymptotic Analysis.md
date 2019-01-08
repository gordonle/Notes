# Lecture 1: Introduction

> January 8th, 2019

---

## Grade Breakdown

| Evaluation  | Weight        |
| ----------- | ------------- |
| Assignments | 25% (5% each) |
| Midterm     | 25%           |
| Final       | 50%           |

## Terminology

| Term             | Definition                                                   |
| ---------------- | ------------------------------------------------------------ |
| Problem          | Given input, carry out a computational task                  |
| Problem Instance | Input                                                        |
| Problem Solution | Intended Output                                              |
| Problem Size     | Size($l$) is a positive integer $l$ that measures size of instance $l$ |
| Algorithm        | Step-by-step process for carrying out computation            |
| Program          | Implementation                                               |
| Pseudocode       | Most convenient way to communicate algs to another person    |

Each **problem** $N$ can have several **algorithms**, and each **algorithm** $A$ that solves $N$ can have several **programs**.

> Given a problem $N$,
>
> 1. **Algorithm Design**: design algorithm $A$ that solves $N$
> 2. **Algorithm Efficiency**: Assess *correctness* and *efficiency* of $A$

## Algorithm Analysis

To asses the efficiency of an algorithm, we can use

- Experimental Studies
  - Strengths:
    - 
  - Shortcomings:
    - implementation could be costly/complicated
    - timings affected by hardware, software environment, human factors, etc.
    - cannot test all inputs

We develop these in structure, high-level pseudocode, so it is language independent. The analysis of algorithms is based on an idealized computer model, and the **time efficiency** of algorithms is measured in terms of its **growth rate**.

To overcome the dependency on hardware/software, we

- express algorithms using **pseudocode**
- instead of time, we count the number of **primitive operations**
- assume primitive operations have approximately equal running time

Always access worst case scenarios.

### Random Access Machine (RAM) Model

RAM has a set of memory cells, each of which stores one item of data.