# Lecture 23: Exception Safety/Casting

> November 27, 2019

---

## 3 Levels of Exception Safety: 

| Level    | Description                                                  |
| -------- | ------------------------------------------------------------ |
| Basic    | Exception occurs, the program is in a valid but unspecified state. No memory leaks, dangling ptrs, etc |
| Strong   | If an exception occurs during `f()`, it is as if `f()` was never called |
| No-throw | `f()` does not throw exceptions and always achieves its goal |

We need to analyze code line by line to determine the exception safety level.

```c++
class A {...};
class B {...};
class C {
 	A a;
    B b;
    void f() {
        a.method1(); 	// strong guarantee
        b.method2(); 	// strong guarantee
    }
};
```

- If `method1()` throws, `f()` has a **strong guarantee**.
- If `method2()` throws, we need to undo what `method1` did
  - Often, undo-s are not possible! If this is the case, then `f()` does **not** have a strong guarantee

Suppose that `method1()`, `method2()` only had local side effects. Are we able to rewrite `f()` to provide a strong guarantee? Let’s call these methods on copies of `a` and `b`. This is only possible because we know changes are local. We do this so that we can easily “revert” back to the state of `a` and `b` before their methods were called.

```c++
void C::f() {
    A atemp{a};
    B btemp{b};
    atemp.method1();
    btemp.method2();
    a = atemp;
    b = btemp;
}
```

**Note**: `f()` only will have a strong guarantee if `B::operator=` does not throw.

> With **pImpl idiom**:
>
> ```c++
> struct CImpl {
>     A a;
>     B b;
> };
> 
> class C {
>     // === Not actually written ===
>     CImpl *pImpl; // this is what the idiom would have us to
>     // === ===
>     // instead, we follow RAII
>     unique_ptr<CImpl> pImpl;
>     void f() {
>         unique_ptr<CImpl> temp(new CImpl(*pImpl));
>         // auto temp = make_unique<CImpl>(*pImpl);
>         temp->a.method1();
>         temp->b.method2();
>         std::swap(pImpl, temp);
>     }
> };
> ```

## Exception Safety in the STL

### std::vector

- Uses RAII
- wraps around a heap array
- destructor deallocates the array

```c++
void f() {
    std::vector<MyClass> v;
    ...
}
```

When `v` is destroyed, the elements (objects) are also destroyed. What happens when `v` contains pointers?

```c++
void g() {
    std::vector<MyClass *> v;
    ...
}
```

When `v` goes out of scope, the elements within the array (ptrs) are not deleted. So, we would have to do

```c++
void g() {
    std::vector<MyClass *> v;
    ...
    for (auto p : v) delete p;
}
```

This is not exception safe! We would then have to implement our previous `try/catch` block. We can avoid this by using RAII and smart pointers:

```c++
void h() {
    std::vector<std::unique_ptr<MyClass>> v;
    ...
}
```

`std::vector::emplace_back` provides a strong guarantee in all cases!

**Case 1**: `size < capacity`

1. Simply add the element to the end.

**Case 2**: `size == capacity`

1. We have to now create an array with larger capacity. So, copy from old to new

   ​	If this throws, our old array is still fine

2. Swap old & new pointers

3. Delete old (deleting pointers does not throw)

4. Add element

Something more efficient would be to `move` elements to the new array, not copy. Would this still have a strong guarantee? What if halfway through the process, an exception is thrown? We have then lost our strong guarantee.

`emplace_back` actually checks if the `move` operations have a no-throw guarantee (“**no-except**”). If they do, then it uses the more efficient `move` operations. Otherwise, it copies.

## Casting

```c++
Node n;
int *p = (int *) &n; // c-style cast
```

In C++, casts are actually <u>**template functions**</u>. There are 4 different ways to cast in C++.

### static_cast

A “sensible” cast where the type conversion is well defined.

```c++
void f(int);
void f(double);

double a = ...;
f(a); // this calls f(double)
f(static_cast<int>(a)); // syntax for the static_cast, and it calls f(int)
```

An example of a more frequent use case...

```c++
Book *bp = new Text { ... };
// To call getTopic(), we need a Text *
Text *tp = static_cast<Text *>(bp);
```

We can do this because:

1. There MUST be an IS-A relationship between the current type and the requested type

   ​	When we go from `Book` to `Text`, we’ve done a `downcast`.

What we’ve done is an **unchecked cast**! If our assumption is not correct, and for example `bp` is not pointing to a `Text` but instead a `Comic`, behaviour is **undefined**. 

### reinterpret_cast

Anything goes! This relies on compiler-dependent decisions on how objects appear in memory.

```c++
Student *s = ...;
Turtle *t = reinterpret_cast<Student *>(s);
t->draw();
```

This will compile, and we can go ahead and start trying to draw this `Turtle`. **Why** would you ever do this? To bypass the private keyword :open_mouth: .

> Check out :file_folder: `lectures/c++/casting/reinterpret.cc`
>
> Here, we create two classes, one with private fields and another with public ones. By using `reinterpret_cast`, we can now change the previously private fields with the public version of the class!

### const_cast

This is used to remove `const`. 

```c++
void g(int *p);
const int *q = ..;
g(q);		// this will not compile
g(const_cast<int *>(q)); // this will compile
```

While the above code might compile, this can be extremely dangerous. It might be the case that `q` is pointing to READ_ONLY  memory. If so, your program will most definitely crash. 

`const_cast` is useful if `g()` was written by someone else who doesn’t believe in `const` keywords. 

### dynamic_cast

This is the most useful type of cast! We’ll get to this next class. 