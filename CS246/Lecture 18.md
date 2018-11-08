# Lecture 18

> November 8th, 2018

---

### Last Time:

In C++, you can throw anything. It is good practice to use existing exception classes, or to create your own:

```c++
class BadInput{...};
```

Then,

```c++
int n;
try {
    if (!(cin >> n)) throw BadInput{};
    ...
} catch (BadInput &) { // here
	n = 0;
}
```

**<u>Note:</u>** In the above code, since we don’t use the result from our exception, we don’t have to instantiate it with a name

Passing our exception by reference is more efficient, and it <u>prevents object slicing</u> from occurring. 

## Destructors & Exceptions

By default, a program will terminate immediately if a destructor throws an exception - the function `std::terminate` is called. We can change this default behaviour in the destructor definition.

```c++
~MyClass noexcept(false) {
    ...
}
```

However, doing this can cause issues with stack unwinding. Suppose there is an exception while the stack is unwinding. As the stack unwinds, memory on the stack is being reclaimed, so destructors of objects will be called. **What if an exception occurs while a destructor is being run?**

This produces 2 simultaneous exceptions. `std::terminate` is called if both of these are unhandled. 

> **<u>Advice</u>**: Destructors should ***not*** throw exceptions.

## Design Patterns

The general idea is to program an **interface**, not an implementation.

1. Create abstract base classes to provide an interface
2. Use base class pointers, and call the interface methods (polymorphism)

Note that subclasses can be swapped in or out to change the behaviour of our program.

### Iterator Pattern - Revisited

We needed to implement the methods `operator*`, `operator++`, and `operator!=` for our `Iterator`. We will abstract this:

```c++
class AbsIter {
    public:
    virtual int &operator*() const = 0;
    virtual AbsIter &operator++() = 0;
    virtual bool operator!=(const AbsIter &) = 0;
    virtual ~AbsIter() {}
}
```

We could even make this a template that can take in any type and create the appropriate iterator. 

```c++
class List {
    struct Node;
    Node *theList = nullptr;
    public:
    class Iterator : public AbsIter {
        Node *curr;
        Iterator( ... ): "MIL STUFF" { };
        public:
        int &operator*() const override { ... }
        Iterator &operator++() override { ... }
        bool operator!=(const AbsIter &o) override { ... }
    };
};
```

Suppose now we have a set, instead of a list.

```c++
class Set {
    ...
    public:
    class Iterator : public AbsIter {
        // the three operator member functions
    };
};
```

Use pointers of the base class type forces you to only use operators that the base class supports. This way, we can write code that is no longer tied to any specific data structure. 

```c++
template <typename Fn>
void forEach(AbsIter &start, const AbsIter &end, Fn f) {
    while (start != end) {
        f(*start);
        ++start;
    }
}
```

We implement a function `addFive()` and we loop through any data structure. For example, we iterate through a list

```c++
void addFive(int &x) { x += 5; }
List l;
List::Iterator b = l.begin();
forEach(b, l.end(), addFive);
```

### Observer Pattern

Typically used in a `publish-subscribe` system. In these systems,

| Type     | Role                         |
| -------- | ---------------------------- |
| Subject  | Publishes and generates data |
| Observer | Subscribes to data updates   |

> If you want to create an abstracted subject class but there is no obvious pure virtual method, we make the destructor pure virtual, but still implement it.

Pure virtual methods can actually be implemented in the parent class! Here’s an updated definition from before:

A **pure virtual** method must be implemented by all subclasses for it to be concrete. 

Check out :file_folder: `lectures/se/observer` to see some implementations of this.

### Decorator Pattern

We are trying to update/add functionality to an existing object. Check out :file_folder: `lectures/se/decorator` to learn how to make pizza. UML diagrams are in my notes. 