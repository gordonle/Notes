# Lecture 16

> November 1, 2018

---

## Last Time: Method Overriding

```c++
bool Book::isHeavy() { return numPages > 200; }
bool Text::isHeavy() { return getNumPages() > 300; }
bool Comic::isHeavy() { return getNumPages() > 30; }

Book b = Comic{_, _, 40, _};
b.isHeavy();
```

In the above code, `b.isHeavy()` calls `Book::isHeavy` due to **object slicing**. 

```c++
Comic c{_, _, 40, _};
Comic *cp{&c};
cp->isHeavy();
```

This time, we have a `Comic` object with a `Comic` pointer, so this will call `Comic::isHeavy` as intended. Now we can also use the **IS-A** relationship:

```c++
Book *bp{&c}; // no slicing occurs
bp->isHeavy();
```

The `Book` pointer is pointing to a `Comic` pointer,  but it is still going to call `Book::isHeavy()`. The compiler looks at the declared type of `bp` and accordingly, decides that `Book::isHeavy` should be called (**static dispatch**)

## Dynamic Dispatch (`virtual`)

:file_folder: `c++/inheritance/example3`

```c++
class Book {
    ...
    public:
    virtual bool isHeavy() { ... };
};
bool Text::isHeavy() override { ... };
bool Comic::isHeavy() override { ... };

Comic c{_, _, 40, _};
Comic *cp{&c};
Book *bp{&c};
Book &br{c};

// The following all call Comic::isHeavy()
cp->isHeavy();
bp->isHeavy();
br.isHeavy();
```

The `virtual` method written above is **dispatched dynamically**. The decision on which method to call happens during the **runtime type** of the object, and once you make a field virtual, it remains virtual for all its children.

### `override` Keyword

The `override` keyword is a safeguard to make sure you are in fact overriding a method. Incorrectly done, the compiler will generate an entirely new method.

### Dynamic Dispatch Cost

There is a cost associated with determining types at runtime. This is why `C++` favours static dispatch because the cost is shifted to compile time.

:file_folder: `c++/inheritance/example4`

```c++
Book *collection[20]; // using Book * to prevent object slicing
fot (int i = 0; i < 20; ++i) {
    cout << collection[i]->isHeavy(); // will call the most specific one
}
```

## Polymorphism

The ability to accommodate multiple types within the same abstraction. In our examples, we’ve used `Book` to represent all of `Book`, `Text`, and `Comic`. Above, `collection` is a **polymorphic** array. Recall the output operator:

```c++
ostream &operator<<(ostream &, Student &)
```

Here, the parameter `ostream &` is a polymorphic parameter. It can refer to multiple different types.

## Destructors

When an object of a derived class is destroyed, what happens? There are 4 steps, as before:

1. Subclass destructor body runs
2. Subclass fields are destroyed in reverse declaration order
3. Superclass destructor is called
4. Space is reclaimed/deallocated

Destructors are prone to causing memory leaks when 

:file_folder: `c++/inheritance/example5`

```c++
class X {
    int *x;
    public:
    X(int n): x{new int[n]} {}
    ~X(){ delete[] x; }
};
class Y: public X {
    int *y;
    public:
    Y(int n, int m): X(n), y{new int[m]} {}
    ~Y() { delete[] y; }
};
```

Now, consider the following code:

```c++
X *myX = new Y{10, 20};
delete myX; 
```

**This will leak memory!** We have not called `Y`’s destructor, so it will not run. The parent class is not aware of any child classes it has, since `X`’s destructor is statically dispatched. 

If a class is expected to have subclasses, declare the parent destructor `virtual` (remember it is passed onto children).

```c++
virtual ~X() {}
```

If a class is **NOT** expected to have subclasses, we declare the class as `final`.

### `final` Keyword

```c++
class Y final: public X {
    ...
};
```

This prevents a child class of `Y` from being created.

## `pure virtual` Methods

> **Co-op VS Non Co-op**
>
> ```c++
> class Student {
>     ...
>     public:
>     virtual int fees() = 0;
> };
> 
> class Coop: public Student {
>     public:
>     int fees() override{ ... }
> };
> 
> class Regular: public Student {
>     public:
>     int fees() override{ ... }
> };
> ```
>
> In the code above, we know that a `Student` must be one of either `Coop` or `Regular`, so we want `Student::fees()` to not have an implementation. As such, we make it `pure virtual`. The line
>
> ```c++
> virtual int fees() = 0;
> ```
>
> is a **pure virtual** method. 

The key differences between `virtual` and `pure virtual` are that:

- `virtual` methods **<u>may</u>** be overridden by subclasses
- `pure virtual` methods **<u>must</u>** be overridden by subclasses to be considered **concrete**

A class with even one pure virtual method is abstract and cannot be instantiated. For example,

```c++
Student s;
```

is invalid. As well, abstract classes are used to organize types, and can have shared fields/methods and support polymorphism. 

A **<u>concrete</u>** class declares no new pure virtual methods and overrides all inherited pure virtual methods.

## UML Tips

| Types                  | Style                     |
| ---------------------- | ------------------------- |
| Virtual / Pure Virtual | *italics*                 |
| Abstract               | `class name` in *italics* |
| Static                 | **bold**                  |

## Templates

```c++
class Stack {
    int count;
    int capacity;
    int *contents;
    public;
    int pop();
    void push(int);
    int top();
    ~Stack();
};
```

A C++ Template Class is parameterized on a **type**. We can now write:

```c++
template <typename T>
class Stack {
    int count;
    int capacity;
    T *contents;
    public;
    T pop();
    void push(T);
    T top();
    ~Stack();
};
```

Now, if we want to create a stack of `int` or `string`, we can do

```c++
stack<int> sInts;
stack<string> sStrings;
```

