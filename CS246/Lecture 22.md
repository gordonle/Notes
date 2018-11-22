# Lecture 22: Exception Safety

> November 22nd, 2018

---

## Last Time:

```c++
void f() {
    MyClass *p = new MyClass;
    MyClass m;
    g();
    delete p;
}
```

We want our program to recover from exceptions, if and when they’re called. The program should not leak memory, and we want to stay in a consistent state. This means **no dangling pointers** and **no broken invariants**. 

C++ guarantees that during **stack unwinding**, all stack allocated objects are destroyed properly. 

Let’s refactor `f`

```c++
void f() {
    MyClass *p = new MyClass;
    try {
        MyClass m;
        g();
    } catch (...) {
        delete p;
        throw;
    }
    delete p;
}
```

This fix is error prone and tedious - in more complicated functions, we’ll have to have `throw/catch` blocks everywhere.

We want a way to guarantee that some code runs irrespective of whether an exception occurs or not. In C++, we rely on it’s guarantee for stack objects  - let’s maximize the stack usage.

## Resource Acquisition Is Initialization (RAII)

Every resource should be wrapped within a stack allocated object, whose destructor releases the resource.

> Example: `ifstream`
>
> ```c++
> { 
> 	ifstream f{"file"}; // automatically opens the file
> }
> ```
>
> The file resource is released (closed) when the stack object (`f`) goes out of scope.

### RAII for Heap Memory

Wrap the heap object within a stack object whose destructor deallocates the heap object. `STL` provides a template class to do this! 

## Smart Pointers

### Unique Pointers - `std::unique_ptr<T>` 

The **unique pointer** has a constructor that takes a `T *` as an argument, and its destructor deletes the pointer. This class overloads `operator*` and `operator->`.

Refactoring `f` again, this time it’s exception safe and doesn’t leak memory.

```c++
void f() {
    // The following two lines accomplish the same thing. We choose ONE.
    std::unique_ptr<MyClass> p{new MyClass};
    auto p = std::make_unique<MyClass>(); // parameters to the ctor of MyClass go in ()
    MyClass m;
    g();
}
```

#### Copying VS Moving `unique_ptr`

```c++
class c{...};
auto p = std::make_unique<c>();
std::unique_ptr<c> q = p; // this will not compile
```

`unique_ptr` does **NOT** have a copy constructor. It is disabled to avoid occurrences of double `free`, since you would have multiple stack objects pointing to the same heap object. 

A sample implementation of `unique_ptr`s can be found at :file_folder: `lectures/c++/unique_ptr/basicimpl.cc`

> `delete` keyword is used to **disable** the copy constructor.

#### Ownership

Who owns the heap resource that is released? If code does own the heap resource, it can be provided the “raw” pointer. We use the method `get()` to access the raw pointer.

If there are multiple owners, we use a new type of Smart Pointer, the shared pointer.

### Shared Pointers - `std::shared_ptr`

The **shared pointer** uses reference counting. It’s destructor only deletes heap memory once the reference count reaches 0 (once nobody is referring to it).



