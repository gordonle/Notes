# Lecture 13: Invariants & Encapsulation

> October 23, 2018

---

```c++
struct Node {
    ~Node() {
        delete next;
    }
};

Node n1{1, new Node{2, nullptr}};
Node n2{2, &n1};
```

When these two nodes go out of scope, the destructor will call `delete` on the stack allocated nodes. This is not allowed.

Node assumed that `next` is either `nullptr` or points to the heap. **Invariants** are statements or assumptions that must continue to be true for the class/function to continue to behave as desired.

By creating `n2`, we violated this invariant. To reason about program correctness, we must guarantee that invariants are not violated. To do this, we use the concept of **encapsulation**. 

## Encapsulation

We treat objects as black boxes (or capsules), thus hiding the implementation. However, we provide an **interface** (a select number of methods) that allow others to interact with this class. How does C++ support encapsulation?

```c++
struct Vec {
    Vec(int x, int y) : x{x}, y{y} {}
    private:
    	int x, y; 	// hidden from outside the class
    public :
    	Vec operator+(const Vec &other) {
     		return { x + other.x, y + other.y };
    	}
};

Vec v{1,2};
// the following is valid
Vec v1 = v + v;
// the following is invalid - cannot access the private variables outside of the class
cout << v.x << v.y;	
```

By default, `struct` visibility is <u>public</u> and `class` visibility is <u>private</u>.

> **<u>Advice</u>**: at a minimum, keep all fields private. This is the preferred syntax:
>
> ```c++
> class Vec {
>     int x, y;
>     public:
>     	Vec(int x, int y);
>     	Vec operator+(const Vec &);
> }
> ```

## Node Invariant

We wish to prevent client code from creating Nodes and accessing the `next` pointer. 

- We create a wrapper List class with sole access to Nodes

```c++
// list.h

class List {
    struct Node; // private nested class
    Node *theList = nullptr;
    public:
    	void addToFront(int); // this is the only way the user can create Nodes
    	int ith(int);
    	~List();
};
```

We can freely define our functions in our `.cc` implementation file, since the user only has access to the `.h` interface.

```c++
// list.cc

struct List::Node {
    int data;
    Node *next;
    ~Node() {delete next;}
};

void List::addToFront(int n) {
    theList = new Node{n, theList};
}

int List::ith(int i) {
    // preconditions: the ith node must exist
    Node *curr = theList;
    for (int j = 0; j < i && cur; ++j, curr = curr->next); // pretty neat ngl
    return curr->data;
}

List::~List() {
    delete theList;
}
```

Now suppose we want to print the list. What is the cost? Since the only way to access each element is to call `ith`, which has an average cost of $O(n)$. But we need to call this $n$ times, so the cost of traversal is: $O(n^2)$. But we would like $O(n)$ traversal!

### Design Patterns - Iterator Design Pattern

This is a way to traverse our Linked List in $O(n)$ time. We will need to keep track of where we are inside the List. 

**<u>CHALLENGE</u>**: do this *without* using a public Node pointer.

**<u>SOLUTION</u>**: create another class that keeps track of where we are, but does so privately. This iterator class will act as an abstraction of a pointer inside the list.

> Iterating through an array with pointers:
>
> ```c++
> //arr is an array
> for (int *p = arr; p != arr + arraysize; ++p) {
>     // *p //
> }
> ```

**<u>TODO</u>**: `operator!=`, `operator++`, `operator*`, begin and end methods

```c++
class List {
	struct Node;
    Node *theList;
    public:
    class Iterator { // things in here are private to class Iterator
        Node *curr;
        public:
        Iterator(Node *curr) : curr{curr} {}
        int &operator*() const { return curr->data; }
        Iterator &operator++() { // unary prefix ++
            curr = curr->next;
            return *this;
        }
        bool operator!=(const Iterator &other) {
            return curr != other.curr;
        }
    }; // end of Iterator
    Iterator begin() { return Iterator {theList}; }
    Iterator end() { return Iterator {nullptr}; }
    // addToFront, ith, destructor for List
};

List lst;
lst.addToFront(1);
lst.addToFront(2);
lst.addToFront(3);
// List is currently 3 -> 2 -> 1 -> nullptr
for (List::Iterator it = lst.begin(); it != lst.end(); ++it) {
    cout << *it << endl;
}
```

We can use the `auto` keyword in this case.

```c++
auto x = y; // x is defined to be the same type as y
for (auto it = lst.begin(); it != lst.end(); ++it) {}
```

> Above, we wrote the unary **prefix** ++. If we want to write a function for the **postfix**, we must include an int parameter that remains unused. This is a hack.

C++ has a built in Iterator Design Pattern, like so:

```c++
// By Value
for (auto x: lst) {
    cout << x << endl;
}
// By Reference
for (auto &x: lst) {
    x = x + 1;
}
```

