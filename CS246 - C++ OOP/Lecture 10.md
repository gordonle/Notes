# Lecture 10: Initializing Objects

> October 11, 2018

---

Last time:

```c++
struct Student {
    int assns, mt, finals;
    // declaring the constructor
    Student(int assns, int mt, int finals);
};
// implementing the constructor
Student::Student(int assns, int mt, int finals){
    this->assns = assns;
    this->mt = mt;
    this->finals = finals;
}

// These are all equivalent - if an appropriate constructor is present, it is called
Student billy{80, 50, 70};
Student billy = Student(80, 50, 70);
```

## Uniform Initialization Syntax

```c++
// Integers
int x = 5;
int x(5);
int x{5};

// Strings
string s = "hello";
string s("hello");
string s{"hello"};
```

**NOTE**: We do not use the keyword `new`, as that will place it on the **heap** and not the **stack**.

As mentioned before, the recommended initialization syntax is to use `{  }`.

```c++
// Heap Allocation
Student *pBilly = new Student{80, 50, 70};
...
delete pBilly;
```

This will create a pointer to a 	`Student` struct.

## Advantages of Writing Constructors

- Executes arbitrary code
- Default arguments
- Overloading constructors
- Sanity Checks

```c++
struct Student {
    ...
    // default values in declaration
   	Student(int assns = 0, int mt = 0, int finals = 0); 
};

Student::Student(int assns, int mt, int finals){
    this->assns = assns < 0 ? 0 : assns;
    this->mt = mt < 0 ? 0 : mt;
    this->finals = finals < 0 ? 0 : finals;
}

// Calling the constructor
Student s1{50, 60, 70};
Student s2{50, 60};
Student s3{50};
Student s4; // no curly braces here - this will call the default constructor
```

### Default Constructor

Every class comes with a default (0 parameter) constructor, which initializes **fields that are objects** by calling its default constructor.

```c++
struct A{
    int x;
    Student y;
    Vec *z;
};
A myA; // calls the default constructor
```

`x` and `z` will remain uninitialized. `y`, on the other hand, is an object, so it will be initialized.

As soon as you implement **<u>ANY</u>** constructor, you lose the default constructor and C-style initialization.

```c++
struct Vec {
    int x, y;
    // this is bad style, the implementation of the constructor should be in a .cc file
    Vec(int x, int y) { 
        this->x = x;
        this->y = y;
    }
    // this will make the code below work
    Vec () {
        x = 0;
        y = 0;
    }
}

// Since we defined the constructor,
Vec v; 			// won't compile
Vec v{0,0}; 	// compiles
```

### Initializing Constant/Reference Fields

#### Option 1

```c++
int z;
struct MyStruct {
    const int myConst = 10;
    int &myRef = z;
};
```

A problem arises when we want a unique constant for each instance of the object.

> **<u>Example</u>**: Student IDs
>
> ```c++
> struct Student {
>     ...
>     const int id = 20719222;
>     ...
> };
> ```
>
> This won’t work for us, since each student has their own unique ID.

#### Option 2

Do not use in-class initialization

**RULE**: `const`/`refs` must be initialized before the constructor body function runs.

##### Steps for Object Construction

1. Allocate space (`stack`, `heap`)
2. Field initialization (call default constructors for fields that are objects)
3. Constructor body runs

Let’s hijack **Step 2**! We use a construct called a `Member Initialization List` (MIL). 

```c++
Student::Student(const int id, int assns, int mt, int finals) :
id{id}, assns{assns}, mt{mt}, finals{finals} {
    // this is where the sanity checks would go. Otherwise, leave it empty.
}
```

`MIL` can be used for ALL fields, and is recommended that you do this. Also, there is no need to use keyword `this` to disambiguate fields/parameters with the same name.

- Outside the braces, the identifier is a field
- Inside the braces, normal scope rules apply.

### Initializing Objects as Copies of Others

```c++
Student billy{80, 50, 70};
Student bobby{billy}; // calls the copy constructor
```

### What do we get for free?

When we create a class, it automatically comes with:

| Feature                  | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| Default constructor      | 0 parameter constructor                                      |
| Copy constructor         | Creates an object that is a copy of another                  |
| Copy assignment operator | Copies the contents of one object into another               |
| Move constructor         | Creates an object and moves the contents of another to it, deleting the other |
| Move assignment operator | Moves the contents of one object to another                  |
| Destructor               | Runs the destructor body, deletes each field, then frees memory allocated |

The last 5 in the above list are known as “**The Big 5**”.

#### Copy Constructor

```c++
Student::Student(const Student &other): assns{other.assns}, mt{other.mt}, finals{other.finals}{
}
```

Sometimes this `copy constructor` does not work exactly as intended. 

> <u>**Example**</u>: Nodes and Linked Lists:
>
> ```c++
> struct Node{
>     Node *next;
>     Node(int data, Node *next);
>     Node(const Node &other);
> }
> Node::Node(int data, Node *next) : data{data}, next{next} {} 			// ctor
> Node::Node(const Node &other) : data{other.data}, next{other.next} {} 	// copy ctor
> 
> Node *np = new Node{1, new Node{2, new Node{3, nullptr}}};
> // Calling the copy constructor
> Node m{*np};					// Dereference np
> Node *n1 = new Node{*np};		// First node will be on the heap
> ```
>
> ![nodes&ll](C:\Users\gordo\Documents\2A\CS246\nodes&ll.png)
>
> This creates a **shallow copy**, as the tails are shared in each case. Modifying the last node will change all three!

Often, we will want a **<u>deep copy</u>**. To do this, we will use recursion.

```c++
Node::Node(const Node &other) : 
data{other.data}, next{other.next ? new Node{*other.next} : nullptr} {}
```

A copy constructor is called when

- an object is constructed as a copy of another
- passing by value
- returning by value

The parameter of a copy constructor **<u>must</u>** be a reference, otherwise we end up in an infinite loop.

