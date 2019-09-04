# Lecture 12: Move Constructor & Assignment Operator

> October 18, 2018

---

**<u>Last Time:</u>** `classes/rvalue/node.cc`

The move constructor can only be called on a temporary value that is about to be destroyed. The temporary value is then taken and stored into an object.

## `rvalue` References

```c++
Node &other;		// lvalue reference
Node &&other;		// rvalue reference
```

An 	`rvalue` reference is a reference to a temporary value (one that is about to be destroyed).

## Move Constructor

The `move constructor` takes one parameter - an `rvalue` reference. 

```c++
Node::Node(Node &&other) : data{other.data}, next{other.next} {
    others.next = nullptr;
}
```

The destructor for `other` will run once this function completes, deleting it. By default, the given move constructor would behave the same as the given copy constructor.

## Move Assignment Operator

```c++
Node m{1, new Node {2, nullptr}};
m = plusOne(m);
```

Once `plusOne(m)` runs, it will create a temporary linked list, then copy it to `m`, then it will delete itself. This constructs new objects that we’re going to delete immediately, so we should instead be using an `rvalue`!

```c++
Node &Node::operator=(Node && Node) {
    swap(other); 	// see Lecture 11 Notes
    return *this;
}
```

If a move constructor/move assignment operator is available, it will be used whenever the RHS is an `rvalue` reference. 

**NOTE**: The default move constructor/move assignment operator go away if you write **any** of the Big 5.

## Rule Of 5

If you need to implement any of:

- copy constructor
- copy assignment operator
- destructor
- move constructor
- move assignment operator

(the Big 5), then you usually will need to implement all 5.

## Compiler Optimization

### Copy/Move Elision

```c++
Vec makeVec() { return {0,0}; }
Vec v = makeVec(); 
```

Intuitively, the `Vec v = makeVec()` should call either the move or the copy constructor. But this is not the case. The complier might directly create the vector `{0, 0}` in the space for variable `v`. 

C++ allows compilers to avoid calling copy/move constructors even if this would change program behaviour.

Some compilers will perform C/M Elision and some wont. To turn this off:

```bash
$> g++14 -fno-elide-constructors
```

### Operators - Functions or Methods?

Recall that `methods` must be called on a class, and functions are standalone.

The following must be implemented as methods: `operator=`, `operator[ ]`, `operator->`, `operator( )`, `operator T( )`, where T is a type.

#### Assignment Operator

`operator=` must be implemented as a method. This is because we are given one for free.

```c++
n1 = n2
n1.operator=(n2);
```

The LHS (`n1`) is represented by the pointer `*this`.

#### Mathematic Operators

```c++
// Interface
// Sidenote: in here (.h), we don't need parameter names
struct Vec {
    int x, y;
    Vec operator+(const Vec &); 
    // The following must also be implemented as a function, if the LHS is not a Vector
    Vec operator*(const int);
}
Vec operator*(const int, const &);
```

```c++
// Implementation
// Here we need our parameter names again
Vec Vec::operator*(const int k) {
    return { x*k, y*k };
}
```

#### Input / Output Operators

Why don’t we define output/input operators as methods? This will prevent us from being able to chain our output together (ie. `cout << v1 << v2`). For example,

```c++
ostream &Vec::operator<<(ostream &out) {
    out << x << " " << y;
    return out;
}
```

With this definition, if we want to call `cout << v1 << v2` , then it will have to be called `v2 << (v1 << cout)`.

This is against programming conventions, so **<u>DO NOT DO THIS</u>**. Always write IO operators as standalone functions.

## Arrays of Objects

```c++
struct Vec {
    Vec (int x, int y);
    // by doing so, we delete the default constructor (no paramters)
    // we will then not be able to initialize an array of Vec!
}
// None of the following will compile:
Vec v;
Vec v[10];
Vec *ptr = new Vec[10];
```

To fix this, we can:

1. implement a 0 parameter constructor

2. for stack arrays, use array initialization

   ```c++
   Vec v = {Vec{0,0}, Vec{0,0}, Vec{0,0}};
   ```

3. use an array of pointers to objects

### Arrays of Pointers to Objects

For allocating memory in the stack,

```c++
Vec *array[3];
```

and in the heap,

```c++
Vec **array = new Vec*[3]; // this is a heap allocated array of pointers to Vec objects
```

When we want to define values in the array, we also need to remember to delete them afterwards.

```c++
Vec **array = new Vec*[3];
...
array[0] = new Vec{0,0};
...
for(int i = 0; i < 3) delete array[i];
delete[] array;
```

## `const` Methods

```c++
struct Student {
    int assns, mt, finals;
    float grade() const {
        return 0.4*assns, + 0.2*mt + 0.4*finals;
    }
}
const Student billy{80, 50, 75};
billy.grade(); 
```

Calling `grade.( )` on `billy` will not compile unless we add the keyword `const`, as we cannot guarantee that `billy`’s grade won’t change. A `const` method promises to not change field values of `*this`.

As such, `const` objects can only call `const` methods!

----------------------------------------------------------------------------

**-- <u>MIDTERM COVERS CONTENT UP UNTIL THIS POINT</u> --**

---

## Invariants & Encapsulation

Previously, we’ve assumed from our `Node` class was that `next` always points to heap memory or is a `nullptr`, but we never restricted this. This will be covered next lecture.