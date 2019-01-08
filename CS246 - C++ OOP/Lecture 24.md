# Lecture 24: Casting, Template functions, Virtual

> November 29th, 2018

---

## Casting

Last time, we covered the first three types of casts:

- `static_cast`
- `reinterpret_cast`
- `const_cast`

Let's now discuss the most useful type: `dynamic_cast`.

### dynamic_cast

```c++
vector<Book *> myBooks;
...;
Book *bp = myBooks[i];
Comic *cp = dynamic_cast<Comic *>(bp);
if (cp) cout << cp->getHero();
else cout << "Not a Comic";
```

So, what we're doing is tentatively trying the cast. If successful, `cp` is a valid Comic pointer! Otherwise, `cp` becomes `nullptr`.

#### dynamic_cast for references

```c++
Comic c{ ... };
Book &b{c};
...;
// Will this work?
Comic &c2 = dynamic_cast<Comic &>(b);
```

If successful, `c2` is a valid reference to the `Comic`. If unsuccessful, a `bad_cast` exception is thrown.

### Casting with Shared Pointers

| Regular Syntax     | Shared Pointer Syntax  |
| ------------------ | ---------------------- |
| `static_cast`      | `static_pointer_cast`  |
| `reinterpret_cast` | **DNE**                |
| `const_cast`       | `const_pointer_cast`   |
| `dynamic_cast`     | `dynamic_pointer_cast` |

The shared pointer syntax is used to cast a `shared_ptr` to another `shared_ptr` object.

### Resolving Partial Assignment

```c++
Text t1{ ... }, t2{ ... };
Book *bp1{&t1};
Book *bp2{&t2};
*pb1 = *pb2;
```

We fix the previously mentioned problem of partial assignment by making `operator=` virtual.

```c++
class Book {
    ...
    public:
    virtual Book &operator=(const Book &);
};

class Text : public Book {
    ...
    Text &operator=(const Book &other) override {
        const Text &temp = dynamic_cast<const Text &>(other);
        Book::operator=(other);
        topic = temp.topic;
        return *this;
    }
}
```

This does not prevent this code from being executed

```c++
Comic c{ ... };
Book *pb3{&c};
*pb1 = *pb3; 	// this will throw an exception
```

## Runtime-Type Information (RTTI)

```c++
void whatIsIt(shared_ptr<Book> b) {
    if (dynamic_pointer_cast<Comic>(b)) cout << "Comic";
    else if (dynamic_pointer_cast<Text>(b)) cout << "Text";
    else cout << "Book";
}
```

The code above is **tightly coupled** with the class hierarchy, so if you change the hierarchy in any way, we'll also have to do the appropriate changes. The fix? Use a **virtual method** to print out the type.

## Template Functions

```c++
template<typename T>
T min(T x, T y) {
	return (x < y) ? x : y;
}
int x = 5, y = 7;
int result = min(x, y);		// min<int>(x, y);
```

How do we decide which `operator<` to call on `x` and `y`? The type of `T` is automatically inferred from its parameters.

```c++
template <typename Func>;
void foreach(AbsIter &start, const AbsIter &finish, Func f)  // pass name of fn
	while (start != finish) {
		f(*start);
        ++start;
	}
}
```

Here, `start` and `finish` has an IS-A relationship with Abstract Iterators. Instead,

```c++
template<typename Iter, typename Func>;
void foreach (Iter start, Iter finish, Func f) {}
void foo (int n) {
    cout << n << endl;
}
int a[] = {1, 2, 3, 4};
foreach(a, a+4, foo);
```

## std::algorithm

1. `for_each`

2. `find`

    ```c++
    template <typename Iter, typename T>;
    Iter find (Iter first, Iter last, const T &val) {
        // search from [first, last) for the value val
        // return Iter val to the first occurrence
        // return last if not found
    }
    ```

3. `find_if` / `find_if_not`

    > Implement this as an exercise!

4. `copy`

    ```c++
    template <typename InIter, typename OutIter>;
    OutIter copy(InIter first, InIter last, OutIter result) {
    	// copy one container's range [first, last) to another starting at result
        // result must have enough space
    }
    
    vector<int> v{1, 2, 3, 4, 5, 6, 7};
    vector<int> w(4); // reserve space for 4 ints
    copy(v.begin() + 1, v.begin() + 5, w.begin()); // make sure it's only 4 elements
    ```

    Note that we have the ability to specify the range of which we want to copy!

5. `transform`

    ```c++
    template <typename InIter, typename OutIter, typeName Func>;
    OutIter transform(InIther first, InIter last, OutIter result, Func f) {
        while (first != last) {
            *result = f(*first);
            ++first;
            ++result;
        }
        return result;
    }
    ```

    An example of using this,

    ```c++
    int add(int n) {
        return n + 1;
    }
    vector<int> v2(v.size());
    transform(v.begin(), v.end(), v2.begin(), add1);
    ```

## How Virtual Works

If you're interested in this, take cs344!

```c++
class C {
    int x;
    public: 
    virtual void foo();
    void bar();
    ~C();
};
```

What do we get when we call the following?

```c++
C c;
sizeof(c);
```

This will return <u>at least 12</u>. Every time a class has a virtual method, objects of that class contain a pointer "**virtual pointer**" `vptr`. 

```c++
c.bar();
```

For every class that has a virtual method, a **single** virtual table s created. `vptrs` point to virtual tables!

## Potential Exam Questions

1. Use `transform` on a particular vector