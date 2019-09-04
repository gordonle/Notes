# Lecture 17: Templates, STL, Exceptions

> November 6, 2018

---

Last time, we began learning about C++ templates: a type of **abstracted class**

```c++
template <typename T>
class Stack {
    int size;
    int capacity;
    T *contents;
    public:
    void push(T x) { ... }
    T top() { ... }
    void pop() { ... }
    ~Stack() { ... }
};
```

To create instances of this `Stack`,

```c++
Stack<int> s1;
s1.push(1);
// ------------------------
Stack<string> s2;
s2.push("this is a string");
```

## Template List Class

```c++
template <typename T>
class List {
    struct Node {
        T data;
        Node *next;
    };
    Node *thelist = nullptr;
	public:
    class Iterator {
        Node *curr;
        Iterator() {}
        public:
        T &operator*() {}
        Iterator &operator++() {}
        friend class List<T>;
    };
    T ith(int i) {}
    void addToFront(T &t) {}  
};
```

**<u>Recall</u>**: the `Iterator` constructor is private, to force the user to use `begin` and `end`.

```c++
List <int> l1;
l1.addToFront(1);
for (List<int>::iterator it = l1.begin(); it != l1.end(); ++it) {
    cout << *it << endl;
}
// We can also create a list of lists of integers
List<List<int>> l2;
l2.addToFront(l1);
```

## STL: Standard Template Library

There are hundreds of template classes that are available to us as part of the STL.

### `std::vector` - Dynamically Resizing Array

```c++
#include <vector>
vector<int> v{4, 5};
v.emplace_back(6); 
// v is now [4, 5, 6]
v.pop_back();
// v is now [4, 5]
```

> `emplace_back()` is more efficient than `push_back()`, because it uses the move constructor instead of always defaulting to the copy constructor.

```c++
vector<int> v1(4, 5); // [5, 5, 5, 5]
// If we want to loop through the vector, we can do either of the following
for (int i = 0; i < v.size(); ++i) {
    cout << v[i] << endl;
}
for (vector<int>::iterator it = v.begin(); it != v.end(); ++i) {
	cout << *it << endl;
}
for (auto n: v) {
    cout << n << endl;
}
```

So `vector` has it’s own nested `Iterator` type!

```c++
// If we want to iterator through our vector in reverse order
for (vector<int>::reverse-iterator rit = v.rbegin(); rit != rend.(); ++rit) {}
```

Many STL methods take iterators as parameters. 

```c++
auto it = v.erase(v.begin()); // removes first, returns an iterator to the new first element
v.erase(v.begin + 3); // removes 4th element, and returns iterator to the new 4th element
v.erase(v.end() - 1);
```

### Out of Range Access

`v[i]` attempts to access the `ith` element. This is unchecked access, and if `i` is out of range, behaviour is undefined.

`v.at(i)` checks if `i` is in range, and if it isn’t an **exception** is thrown.

## Exceptions

:file_folder: `c++/exceptions/rangeError.cc`

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;
    v.emplace_back(2);
    v.emplace_back(4);
    v.emplace_back(6);
    
    cout << v.at(3) << endl; // this is out of range
}
```

:file_folder: `c++/exceptions/rangeError.cc`

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;
    v.emplace_back(2);
    v.emplace_back(4);
    v.emplace_back(6);
    
    try {
        cout << v.at(3) << endl; // this is out of range
        cout << "Done with try" << endl;
    } catch (out_of_range r) {
        cerr << "Bad range " << r.what() << endl;
    }
    cout << "Done with main" << endl;
}
```

As soon as an exception is thrown, the code immediately searches for a `catch` block that handles the type of exception thrown. Then, it continues the code, as if there was never an error.

```c++
throw out_of_range(...);
```

This calls the constructor of the exception object, and allows us to purposefully throw an exception.

### Stack Unwinding

When an exception is thrown, we must pop everything off the stack until the code in the `catch` block can be ran. 

Error recovery can be done in stages:

```c++
try {
    ...
} catch (SomeException e) {
    // we can throw another exception to inform people further down the stack
    1. throw SomeUnrelatedException{...};
    2. throw e; // throws whatever was caught in e, possibly sliced version
    3. throw; // throws the original exception
}
```

All C++ library exceptions inherit from the “exception” class, but in C++ you can throw anything (ie. `int`, `string`, etc). Custom designed exception classes need not inherit from that “exception” class.

```c++
try {
    
} catch (...) { // explicitly the "..." means catch everything
    
}
```

Interesting applications of `try` and `catch` is to throw exceptions to get the values that you want. We can implement a factorial calculator, to find the n-th Fibonacci term, etc. They’re extremely slow to process though, so this may not always be the best idea.