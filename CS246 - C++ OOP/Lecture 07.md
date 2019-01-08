# Lecture 7: Short Topics

> September 27, 2018

## Function Overloading

```c++
int negate(int x) {return -x;}
int negate(bool x) {return !x;}
```

The compiler looks at the function name, number, and type of the parameters to validate function overloading. It cannot just differ on the return type.

## Operator Overloading

Operator Overloading is an example of functional overloading. For example: the operator `>>`

```c++
cin >> x;
operator>>(cin, x); // implemented as a function
```

This is why `cin >> x` can take either a `string`, `int`, `bool`, etc. There are multiple functions defined to take in each of these argument types.

## `structs`

Here’s some C code (remember, most C code is still valid C++ code).

```c
struct Node {
    int data;
    struct Node*next; 			// in C++, the "struct" in this line is optional
};
struct Node n = {3, NULL};		// same here, and use "nullptr" instead of "NULL"
```

The keyword `nullptr` is the recommended way to have a pointer pointing to null (C++11 onwards)

## Constants

```c++
const int MAX = 100;
const Node n1{5, nullptr}; 		// we cannot change the fields of this node

int x = 10;
const int *p = &x;				// p is a pointer to an int that is constant
{ // Example Calls
    *p = 10; 	// INVALID
    p = &y;		// VALID
}
int * const p1 = *x;			// p is a constant pointer to an int
{ // Example Calls
    *p = 10;	// VALID
    p = &y;		// INVALID
}
```

`const int *p = &x` : `p` is not a constant pointer; rather it is pointing to a constant, and so we cannot change the value of what p is pointing at. `*p = 10` is **<u>invalid</u>**, but `p = &y` is **<u>valid</u>**.

## Parameter Passing

By default, we **<u>pass by value</u>**.

```c++
void inc(int n) {
    n = n+1;
}
...
int x = 5;
inc(x);
cout << x; 		// prints out 5, since a copy of x is set in "inc", and doesn't change x
```

What if we want to <u>**pass by pointer**</u>?

```c++
void inc(int *n){
    *n = *n + 1;
}
...
int x = 5;
inc(&x);
cout << x; 		// prints out 6
```

How does this work with `cin`? When we call `cin >> x`, we are actually calling `operator>>(cin, x)`. This seems to be passing `x` in by value. This is **NOT** the case; we are actually passing by reference.

### Pass by Reference

C++ has a pointer-like type called a **<u>reference</u>**. There are two types of these in C++.

#### Lvalue References

An `lvalue` can or may appear on the **<u>Left Hand Side</u>** of an assignment. It must represent a memory address - a place where we can store value. All variables in general are `lvalue`s.

```c++
int y = 10;
int &z = y;		// z is an lvalue reference to y. It's type is "int &"
```

An `lvalue` reference is a constant pointer with **automatic dereferencing**.

> **<u>Note</u>**: `z` will continue to “point” to y forever. And so,
>
> ```c++
> z = 15; 	// note this is NOT "*z = 15"
> ```
>
> Because `z` is an lvalue of `y`, this changes the value of `y`. So `z` acts like `y`

If we take the address of `z`, we will get the address of `y`. It has no identity of it’s own; it simply mimics `y`.

```c++
int *p = &z; 	// "p" now points to "y"
sizeof(z);		// will return the size of "y"
```

The compiler **doesn’t even store `z`**, as it will just call `y`. So why do we use `lvalue` types?

#### Things you cannot do with references

1. You cannot leave them uninitialized

   ```c++
   int &z;			// INVALID
   ```

2. Must initialize a reference with an `lvalue`

   ```c++
   int &x = 5; 	// INVALID
   int &x = y + 5;	// INVALID
   ```

3. Cannot create a pointer to a reference

4. Cannot create a reference to a reference

   ```c++
   int &&x = 5; 	// this MIGHT compile, as "int &&" is an rvalue
   int &*y = 5;	// INVALID
   int *&z = 5;	// VALID
   ```

5. Cannot create an array of references

#### Function Arguments by Reference

We can pass by reference!

```c++
void inc(int &n){ // the "&" indicates that we are passing by reference
    n = n + 1;
}
int x = 5;
inc(x);
cout << x; // prints 6
```

`inc(x)` creates a reference `int &n = x` , and so now `n` is referring to `x`. No need to dereference `x`;

> We can overload functions with argument types `int &n` and `int n`, but our program will crash when we call the function, as it doesn’t know which function to use.

So why does `cin >> x` work? `x` is being passed by reference. When we call `cin>>x`, we are actually calling:

```c++
// full signature
std::istream &operator>>(std::istream &in, int &data){}
```

Both parameters are passed by reference. This is because:

- we aren’t allowed to make copies of streams ( `int &data` )
- we want changes to stream to be visible when the function is done ( `std::istream &in` )

```c++
struct ReallyBig{...};
void f(ReallyBig rb){...};
```

`f` passes by value, but creating a copy of a large data type is very expensive.

In C, we would pass a pointer to avoid the copy. In C++, we can also pass by reference:

```c++
void g(ReallyBig &rb){...};
```

`g` avoids the copy but allows changes to the original value. To avoid this, we can pass it as a **<u>constant</u>**:

```c++
void h(const ReallyBig &rb){...};
```

`h` avoids having to copy and it disallows changes to the argument.

> **<u>Advice</u>**: Always prefer passing by reference to `const`
>
> ```c++
> void g(int &x){...};
> g(5); 		// INVALID
> g(y+y);		// INVALID
> ```
>
> Instead, if we do
>
> ```c++
> void f(const int &x){...};
> f(5);		// VALID
> f(y+y);		// VALID
> ```
>
> Behind the scenes, `f(y+y)` actually calls 
>
> ```c++
> int z = y + y;
> int &x = z;
> ```

## Dynamic Memory

```c++
// Legal in C++, illegal in CS246
int *p = malloc(size);
...
free(p);
```

```c++
struct Node {
    int data;
    Node *next;
}
Node *np = new Node;
// this automatically allocates the right size of memory in the heap
// after usage, we must delete the pointer to free the memory
delete np;
```

### Arrays

```c++
int *arr = new int[10]; // returns the pointer to an array of integers of size 10
...
// to deallocate arrays:
delete[] arr;
```

