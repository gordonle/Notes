# Lecture 8: The C++ Preprocessor

> October 2, 2018

## Common Mistakes

```c++
Node getANode(){
    Node n;
    return n; 		// a copy is returned - expensive operation
}
Node *getANode(){
    Node n;
    return &n; 		// Dangling Pointers - pointing to memory that is not accessible
}
```

Never return a pointer/reference to data the function allocated on the stack. Instead,

```c++
Node *getANode(){
    Node *np = new Node {};  // pointing to heap space - perfectly safe and efficient
    return np;
}
```

## Operator Overloading

> Idea: we can give meaning to C++ operators for user-defined types.

```c++
struct Vec {
    int x;
    int y;
};
// We want to be able to add vectors, so write overload for a (+) operator
Vec operator+(const Vec &v1, const Vec &v2) {
    Vec v{v1.x + v2.x, v1.y + v2.y};
    return v;
}
// Returned a copy since "Vec" is small, and because + usually doesn't need a type pointer

// We also want to multiply it by an int, so write overload for a (*) operator
Vec operator*(const int k, const Vec &v1) {
    return {k * v1.x, k * v1.y}; // C++11 can figure out that this return type is a Vec
}

// Multiply a Vec by another Vec
Vec operator*(const Vec &v1, const Vec &v2) {
    return {v1.x * v2.x, v1.y * v2.y};
}
```

For usability, we also want to overload commutivity:

```c++
Vec operator*(const Vec &v1, const int k) {
    return {k * v1.x, k * v1.y};
}
```

> **<u>Example</u>**: Input/Output Operators
>
> ```c++
> struct Grade {
>     int theGrade;
> }
> 
> // we want to be able to `cout << g << endl`. So:
> ostream &operator<<(ostream &out, const Grade &g) { // returns ostream reference
>     out << g.theGrade << "%";
>     return out;
> }
> 
> // we want to create a Grade from stdin
> istream &operator>>(istream &in, Grade &g) { // not const so you can modify it
>     in >> g.theGrade;
>     if (g.theGrade < 0) g.theGrade = 0;	  // these conditions only need to be written once!
>     if (g.theGrade > 100) g.theGrade = 100;
>     return in;
> }
> ```

## C/C++ Preprocessor

This is a program that runs <u>**before**</u> the compiler gets the code. This <u>**can**</u> change code.

`#` is a preprocessor directive. For example:

```c++
#include <header.h> // copy + paste this file from STANDARD LIBRARY
#include "header.h" // copy & paste this file from CURRENT DIRECTORY
```

To only run the preprocessor:

```bash
$> g++14 -E -P my_file.cc
```

To <u>search and replace</u>, the following code will replace every occurrence of `VAR` with `VALUE`.

```c++
#define VAR VALUE // this defines a proprocessor variable with a value
```

> `#define`s are used for conditional compilation. For example, suppose we want security levels 1 & 2.
>
> Level 1: short int
>
> Level 2: long long int
>
> ```c++
> #define SECLEVEL 1 // could be 2
> // ...
> int main() {
>     //...
>     #if SECLEVEL == 1
> 	short int 			// suppressed if SECLEVEL != 1
> 	#elif SECLEVEL == 2
> 	long long int 		// suppressed if SECLEVEL !=2
> 	#endif
>     publicKey;
>     //...
> }
> ```
>
> The problem with this is that we have to change our `#define SECLEVEL` manually. 

### Setting Preprocessor Variables

We can define preprocessor variables from the command line.

1. Remove the `SECLEVEL` define from our code.

2. Then we call it from the command line like so:

   ```bash
   $> g++ -E -P -DVAR=VALUE my_file.cc
   ```

To “comment out code” from the preprocessor, we can do

```c++
#if 0
	// stuff you want to comment out
#endif
```

```c++
#define VAR		// VAR defaults to an empty string when uninitialized with a VALUE

#ifdef VAR		// true, if VAR is defined
#ifndef VAR		// true, if VAR is NOT defined
```

==NOTE==: `#define` is **<u>literally</u>** searching and replacing, so if you `#define a`, all instances of `a` (not like “apple” but just “a”) will be replaced with the `VALUE`.

#### Printing out Debugging Messages

What if we want to control when we show debug messages?

> :file_folder: `c++/preprocess/debug.cc`
>
> ```c++
> int main(){
>     //...
>     #ifdef DEBUG
>     	cout << stuff << endl;
>     #endif
>     //...
> }
> ```
>
> Call it with
>
> ```bash
> $> g++ -DDEBUG debug.cc
> ```

### Summary Table

| Code                     | Purpose                                              | Example               |
| ------------------------ | ---------------------------------------------------- | --------------------- |
| `#include`               | copy & pastes a file to use                          | `#include <header.h>` |
| `#define`                | search and replace, conditional compilation          | `#define VAR VALUE`   |
| `#if`, `#elif`, `#endif` | will only compile code that satisfies the conditions |                       |

## Separate Compilation

We want to break down our code into different modules: interfaces and implementations.

| Module               | Contents                                 |
| -------------------- | ---------------------------------------- |
| Interface `.h`       | Type definitions + Function declarations |
| Implementation `.cc` | Function Implementation                  |

> <u>**Example:**</u>
>
> `vec.h`
>
> ```c++
> struct Vec { 
> 	int x;
>     int y;
> };
> ```
>
> `vec.cc`
>
> ```c++
> #include "vec.h"
> 
> Vec operator+(const Vec &v1, const Vec &v2) {
>     return {v1.x + v2.x, v1.y + v2.y};
> }
> ```

### How to compile

```bash
$> g++ *.cc
# or
$> g++ main.cc vec.cc
```

**NOTE**: Header files are <u>never</u> compiled. Separate compilation is the process of merging the separately compiled files.

We cannot compile these programs separately.

