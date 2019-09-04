# Lecture 21: Compilation Dependencies, Exception Safety

> November 20th, 2018

---

## Last Time: Visitor Design Pattern

:file_folder: `se/visitor`

There is a cyclic `include` chain but it doesn’t compile. The cycle stops because we have **include guards**, but then why isn’t it compiling?

It is because the definition of `Text` is above the definition of `Book`, so our compiler cannot understand what `Text` is. The order of `include`s matter!

An `include` creates a compilation dependency. The changes to included files requires the file to recompile. Often, a **forward declaration** of a class is all we need (rather than the include)

```c++
class XYZ; 	// tells the compiler "trust me, I will define this later"
```

Whenever possible, we <u>prefer forward declarations</u> over includes. This:

- reduces compilation dependencies (including circular dependencies)
- reduces compile time
- reduces compilation frequency

> **Example 1:**
>
> :file_folder: `a.h`
>
> ```c++
> class A{ ... };
> ```
>
> :file_folder: `b.h`
>
> ```c++
> #include "a.h"
> class B : public A { ... };
> ```
>
> :file_folder: `c.h`
>
> ```c++
> #include "a.h"
> class C {
>     A a;
> };
> ```
>
> Here, we need to know how much size must be allocated for our field of type `A`.
>
> :file_folder: `d.h`
>
> ```c++
> class A;
> class D {
>     A *myA;
> };
> ```
>
> Since pointers are all the same size, we can forward declare `A` here.
>
> :file_folder: `d.cc`
>
> ```c++
> #include "a.h"
> void D::foo() {
>     myA->someMethod();
> }
> ```
>
> We have to include our `a.h` file here, since we need to access the fields and methods of `A`. This will never cause circular dependencies, since `.h` files never include `.cc` files.
>
> :file_folder: `e.h`
>
> ```c++
> class A;
> class E {
>     A f(A x);
> };
> ```
>
> In this case, the forward declaration work. Notice that the method `f` itself is a forward declaration. It’s saying that `f` will take a type `A` and return a type `A`. But, when we implement `f` in `e.cc`, we’ll need to include it.
>
> :file_folder: `e.cc`
>
> ```c++
> #include "a.h"
> A E::f(A x) { ... }
> ```

## Reducing Compilation Dependencies

Let’s revisit the graphical interface that was used in Assignment 4.

:file_folder: `window.h`

```c++
#include <XLib/X11.h>
class XWindow {
    Display *d;
    Window w;
    ...
    public:
    draw();
}
```

:file_folder: `client.cc`

```c++
#include "window.h"
...
    myXWindow->draw();
```

`client.cc` has to recompile even if private members in `window.h` changes, even if the changes don’t affect the way `client.cc` functions. How do we fix this unnecessary recompilation?

### Pointer to Implementation (“pImpl” Idiom)

We take the private implementation out of `window.h` and place it in another file.

:file_folder: `XWindowInput.h`

```c++
#include <XLib/X11.h>
struct XWindowImpl {
    Display *d;
    Window w;
    ...
};
```

:file_folder: `window.h`

```c++
struct XWindowImpl;
class XWindow {
    XWindowImpl *pImpl;
    public:
    // all public methods remain here
    draw();
}
```

:file_folder: `window.cc`

```c++
#include "XWindowImpl.h"
#include "window.h"
XWindow::XWindow() : pImpl{new XWindowInput} {}
...
    pImpl->d;
```

What this does is now if private implementation details are modified, then only `window.cc` has to recompile, along with `XWindowImpl`. As such, `window.h` and `client.cc` are unaffected. 

> Check out `Bridge_Pattern_UML.png`

## Coupling & Cohesion

### Coupling

The degree to which modules/classes interact with each other. 

| Type          | Definition                                                   |
| ------------- | ------------------------------------------------------------ |
| Low coupling  | Interaction through a public <u>interface</u>.               |
| High coupling | Interaction through a public <u>implementation</u> (friends, public fields) |

**Goal:** Always aim for <u>low coupling</u>. Classes should be functional on their own.

### Cohesion

Measures how related things are within a module.

| Type          | Definition                                 | Example                   |
| ------------- | ------------------------------------------ | ------------------------- |
| Low cohesion  | The module/class can achieve many tasks    | `<utility`, `<algorithm>` |
| High cohesion | The module/class achieves exactly one task |                           |

**Goal:** Always aim for <u>high cohesion</u>. Everything that is needed to understand something is in a single place. Writing `virtual` methods is actually low cohesion, but sometimes cannot be avoided.

### Decoupling the Interface

Without knowing it, most of our code thus far exhibits very high coupling. How can we fix this?

> **Example**: Chess Game
>
> ```c++
> class ChessBoard {
>     std::cout << "Your move" << std::endl;
> };
> ```
>
> In the above code, `ChessBoard` is coupled with `std::out`. 
>
> ```c++
> class ChessBoard {
>     ofstream &out;
>     out << "Your move";
> };
> ```
>
> This is slightly better. By using an `ostream` variable, we are not restricted to only using `std::out`, but to any output stream. If we wanted to now write to a file, we can. `ChessBoard` is still coupled with `std::ostream`.
>
> `ChessBoard` has two responsibilities:
>
> 1. Game State
> 2. Communication
>
> **<u>Single Responsibility Principle</u>** tells us that `ChessBoard` should not be responsible for communication.

#### Single Responsibility Principle

A class should only have one reason to change - one purpose it fulfils. 

> Check out `MVC_Design_Pattern.png`

## Exception Safety

```c++
void f() {
    MyClass *p = new MyClass();
    MyClass c;
    g();
    delete p;
}
```

Can `f( )` leak memory, given `g( )` does not leak? Yes. If `g` throws an exception, `p` leaks.