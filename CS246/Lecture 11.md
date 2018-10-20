# Lecture 11: The Big 5 (cont.)

> October 16, 2018

---

Note on single parameter constructors. Suppose we have

```c++
Node::Node(int data):data{data}, next{nullptr}{}
```

Then, if you want to initialize a node, we can call

```c++
Node n{4};
Node n = 4;
```

One parameter constructors create ==implicit/automatic conversions==. Now, we can do things like

```c++
void foo(Node n){...}
foo(4);
string s = "hello";
string s{"hello"};
```

If we wish to disable implicit conversions, we use the `explicit` keyword

```c++
struct Node {
    explicit Node(int data);
};
```

## Destructors

A method called the `destructor` runs whenever objects are destroyed. 

| Memory Allocation | Destructor runs                                    |
| ----------------- | -------------------------------------------------- |
| Stack             | when the object goes out of scope                  |
| Heap              | when `delete` is called on a pointer to the object |

### Steps for Object Destruction

1. The destructor body runs
2. Fields that are objects are destroyed in reverse declaration order
3. Deallocates space 

> Notice that this is the exact opposite of the constructor, where memory is allocated then each field is initialized in declaration order. 

The body of the “free” destructor is empty. This may not be sufficient.

> For example:
>
> ![destructor](C:\Users\gordo\Documents\2A\CS246\destructor.png)
>
> What if we called this:
>
> ```c++
> delete np;
> ```
>
> This will call the destructor for Node 1, deallocate it, but then leak memory on Nodes 2 and 3. So we need to implement our own destructor:
>
> ```c++
> struct Node {
>     ...
>     ~Node(); // no parameters, cannot be overloaded
> }
> Node::~Node() {
>     delete next; // recursively deletes the next node
> }
> ```

## Copy Assignment Operator

```c++
Student billy{80, 50, 75};
Student bobby = billy;		// copy constructor
Student jane;
jane = billy;				// copy assignment operator
```

In fact, the CAO is defined as a method that takes a single parameter, meaning we can call it like

```c++
jane.operator=(billy);
```

The copy constructor is called when we initialize an object immediately with another, as with `bobby`. They are born as copies. The `copy assignment operator` (CAO) is called when you update an **existing** object as a copy of another. As per usual, the “free” CAO is often not sufficient.

> Implementing a Node copy assignment operator:
>
> ```c++
> Node & Node::operator=(const Node &other) { // Cannot use MIL, not a constructor
>     // Check if "this" and "other" are the same node to avoid dangling pointers
>     if (this == &other) return *this;
> 	data = other.data;
>     // We must deallocate object "next" to avoid memory leaks, as it may be heap allocated
>     delete next;
>     // next = new Node(*other.next); will break when you reach nullptr
>     next = other.next ? new Node(*other.next) : nullptr;
>     return *this;
> }
> ```
>
> **<u>Remember</u>**: Whenever `operator=` deletes memory, check for self-assignment.
>
> If the call to `new Node (..)` fails (runs out of memory, etc), `next` is not assigned. But we deleted old `next` already. This results in `next` being a dangling pointer. How do we avoid this?
>
> ```c++
> Node & Node::operator=(const Node &other) { // Cannot use MIL, not a constructor
>     // Check if "this" and "other" are the same node to avoid dangling pointers
>     if (this == &other) return *this;
>     Node *tmp = next;
>     next = other.next ? new Node(*other.next) : nullptr;
>     data = other.data; 
>     delete tmp;
>     return *this;
> }
> ```
>
> What this does is prevent the last three lines of code from running, due to C++ throwing an exception. The method will stop executing, and we avoid the dangling pointer.

### Copy & Swap Idiom

```c++
struct Node {
    void swap(Node &other);
}
```

:file_folder: `node.cc`

```c++
#include <utility>
void Node::swap(Node, &other){
    using std::swap;			// defined in the <utility> header
    swap(data, other.data);
    swap(next, other.next);
}
Node & Node::operator=(const Node &other){
    Node tmp{other}; 			// deep copy
    swap(tmp);					// same as this->swap(tmp)
    return *this;
}
```

Since `tmp` is on the stack, it will be automatically deallocated. This let’s us define the copy assignment operator very easily.

:file_folder: `classes/rvalue/node.cc`

```c++
Node plusOne(Node n) {
    for (Node *p = &n; p; p = p->next){
       ++p->data; 
    }
    return n;
}

Node n{1, new Node{2, nullptr}};
Node n2{plusOne(n)}; // this gives 6 calls to the copy constructor
```

The 6 calls are from:

- passing by value (2 nodes)
- returning (2 nodes)
- creating n2 (2 nodes)



