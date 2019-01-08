# Lecture 14

> October 25, 2018

---

## Last Time: Iterator Design Pattern

```c++
List lst;
lst.addToFront(1);
...
for (List::Iterator it = lst.begin(); it != lst.end(); ++it) {
    cout << *it << endl;
}
```

### `auto` Keyword

We can use `auto` to automatically define the type of your variable as what it’s being assigned to.

```c++
for (auto it = lst.begin(); it != lst.end(); ++it) {
    cout << *it << endl;
}
```

### Range-based For Loops

C++ actually has built-in support for this Iterator Design Pattern! 

```c++
for (auto n: lst) {
    cout << n << endl;
} 
// by value; n is a copy of whatever operator* returns
```

```c++
for (auto &n: lst) {
    ++n;
}
// by reference, ++n actually increments whatever data we are looking at
```

To use range-based for loops for a class `MyClass`, the following conditions must be met:

1. `MyClass` must implement `begin()` and `end()`, which must return some “iterator” object
2. That iterator class must implement `operator*`, `operator++`, and `operator!=`

## `friend` Keyword

Constructor for `List::Iterator` are public. This means that `List::begin` and `List::end` call it. We would like to make this `List::Iterator` constructor private, but then `begin()` and `end()` will not be able to access it. 

We can declare `List` to be a `friend ` of `Iterator`:

```c++
class List {
    ...
    public:
    class Iterator {
        Node *curr;
        Iterator (Node *curr);
        public:
        ...
        friend class List;
    };
};
```

**<u>ADVICE</u>**: make as few `friend`s as possible, as it will break encapsulation. If needed, provide accessors/getters and mutators/setters.

```c++
class Vec {
    int x, y;
    public:
    // Getters
    int getX() const {return x;}
    int getY() const {return y;}
    // Setters
    void setX(int x) {this->x = x;}
    void setY(int y) {this->y = y;}
}
```

These are very helpful, especially when writing things like output/input operators. 

```c++
class Vec {
	int x, y;
    public:
    // No accessors implemented
    friend ostream &operator<<(ostream &, const Vec &);
};
ostream &operator<<(ostream &out, const Vec &v) {
    out << v.x << v.y;
    return out;
}
```

In this case, we’ve used `friend`, since accessors can be used by everyone, and here we want to limit it only to the output operator.

**NOTE**: Declarations of friendship have no public or private state.

## `mutable` Keyword

Suppose I want to count the number of times `grade()` is called.

```c++
struct Student {
    int assns, mt, finals;
    mutable int numCalls = 0;
    float grade() const {
        ++numCalls;
        return 0.4*assns + 0.2*mt + 0.4*finals;
    }
};
```

For a constant object, all fields that are not mutable will remain constant.

## `static` Keyword

We can make fields `static`. A static field belongs to the class, **<u>not</u>** each object of the class.

```c++
struct Student {
    static int numObj;
    Student(): ... {++numObj;}
}
```

The field `numObj` will increment anytime the constructor of `Student` is called - the space is only allocated once. When is space allocated for it then?

Static fields must be defined external to the file defining the class. In other words, if that is `student.h`, we cannot define it there. It must be defined externally, in the `student.cc` file. This makes sure that it’s only linked once.

```c++
// student.cc
int Student::numObj = 0;
```

We can also have `static` member functions!

### `static` Member Functions

```c++
struct Student {
    ...
    static int objCreated() {
        return numObj;
    }
};
```

Again, this function is associated with the class, not an individual object. So we don’t need an object to call it. So,

```c++
Student::objCreated();
```

is valid.

**<u>NOTE</u>**: Since they aren’t associated with objects, they do not have the implicit `this` parameter. Static member functions can only access static fields or other static member functions.

> Look up the **Singleton Design Pattern** to see a very clever application of `static` member functions

## System Modelling

A good design requires:

- determining the major **abstractions** (classes)
- **relationships** between objects of these classes

In order to describe these relationships, we use a modelling language. A standard is **<u>UML</u>**: Unified Modelling Language.

### Modelling a Class

Let’s model a single class in UML:

![UML Class](C:\Users\gordo\Documents\Notes\CS246\UML Class.png)

By convention, when we are listing methods, `-` : private, `+`: public.

### Relationship 1: Composition

```c++
class Vec {
    int x, y;
    public:
    Vec(int x, int y);
}
class Basis {
    Vec v1, v2;
}
Basis b; // this won't compile, since there is no default constructor for Vec
```

Instead, we can hijack the default constructor on the `Basis` class using MIL.

```c++
class Basis {
    Vec v1, v2;
    Basis(): v1{0,0}, v2{1,1} {}
}
```

Embedding an object (`Vec`) within another (`Basis`) is called **composition**. We say “Basis OWNS_A Vec”.

If `A` OWNS_A `B`,

- `B` does not exist outside of `A`
- copying `A` copies `B` (deep)
- destroying `A` destroys `B`