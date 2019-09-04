# Lecture 20: Template Method Pattern, Visitor Design Pattern

> November 15th, 2018

---

## Last Time: Template Design Pattern

```c++
class Turtle {
    public:
    void draw(){
        drawHead();
        drawShell();
        drawFeet();
    }
    private:
    void drawHead(){}
    void drawFeet(){}
    virtual void drawShell() = 0;
};
```

```c++
class RedTurtle : public Turtle {
    void drawShell () override {
        // draw the Red Turtle
    }
};
```

The idea here is that the base class wants to provide a flexible template for subclasses to use, so that certain methods are customizable (`pure virtual`). Notice that the `drawShell()` is the only **virtual** method, so `drawHead()` and `drawFeet()` are always defined the same way.

### Non-Virtual Interface (NVI) Idiom

Consider any `public virtual` method:

- `public`: part of the interface
- `virtual`: invitation to subclasses to change the behaviour

If we want to design a class that follows the **NVI Idiom**,

1. All public methods are non-virtual

2. All virtual methods should be private/protected

   **<u>Exception</u>**: The destructor, which is public/virtual

```c++
class DigitalMedia {
    public:
    virtual void play() = 0; // pure virtual
    virtual ~DigitalMedia();
};
```

This class, as written, does not follow the NVI Idiom. We can redesign this so that the public interface is non-virtual.

```c++
class DigitalMedia {
    public: 
    void play() {
        doPlay();
    }
    virtual ~DigitalMedia();
    private:
    virtual void doPlay() = 0;
};
```

## Standard Library: `map`

`std::map` is available to us through the `<map>` header

A `map` is a generalization of an array. It’s a template class parameterized on two types: the **key** and the **value**.

```c++
#include <map>
using namespace std;
...
map<string, int> m;
m["abc"] = 1; 				// the operator[] is overloaded
m["def"] = 2;
cout << m["abc"] << endl;	// prints "1"
m.erase("abc"); 			// erases the key value pair associated with said key
```

What if we want to check if a key exists?

```c++
cout << m["xyz"] << endl;	// prints 0
```

 Since key “xyz” is not in the map, a default value will be inserted, and then will return it. For integers, the default value is 0. The proper way to search for a key is to use the `count` method.

```c++
return (m.count("pqr")); // 0 if not found, 1 if found
```

Let’s iterate through our map.

```c++
for (auto &p : m) {
    // p is of type std::pair<string, int>
    cout << p.first << " " << p.second << endl; // prints out "[key] [value]"
}
```

## Visitor Design Pattern

Used to do what is called a “**double dispatch**”. When we have `virtual` methods, methods are chosen based on the runtime type of the object.

What if the choice of the method to run depends on 2 objects?

```c++
virtual void Enemy::strike(Stick &) = 0;
virtual void Enemy::strike(Rock &) = 0;
```

```c++
Weapon *w = ...;
while (player->noDead()) {
    e = l->createEnemy();
    w = player->chooseWeapon();
    e->strike(*w); // will not compile, since no Enemy::strike(Weapon &) exists
}
```

The Visitor Design Pattern (VDP) uses a combination of overriding and overloading.

```c++
class Enemy {
    public:
    virtual void strike(Weapon &) = 0;
};
class Turtle : public Enemy {
    public:
    void strike(Weapon &w) override {
        w.useOn(*this);
    }
};
class Bullet : public Enemy {
    public:
    void strike(Weapon &w) override {
        w.useOn(*this);
    }
};
```

We have to have the same code in both subclasses, because by dereferencing `this` in the `Turtle` class, we **know** it is a `Turtle` object. If instead we had placed the `strike()` method in our abstract `Enemy` class, we would have an Enemy reference, and we wouldn’t know if it’s a Turtle or a Bullet.

```c++
class Weapon {
    public:
    // function overloading
    virtual void useOn(Turtle &) = 0;
    virtual void useOn(Bullet &) = 0;
};
class Stick : public Weapon {
    public:
    void useOn(Turtle &t) override {}
    void useOn(Bullet &b) override {}
};
class Rock : public Weapon {
    public:
    void useOn(Turtle &t) override {}
    void useOn(Bullet &b) override {}
};
```

Now,

```c++
e->strike(*w);
```

... will compile!

Other uses of the VDP:

- separation of concerns
- adding functionality without cluttering classes with new virtual methods

This requires class hierarchy to be setup to accept **<u>visitors</u>**.

```c++
class Book {
    public:
    virtual void accept(BookVisitor &v) {
        v.visit(*this);
    }
};
class Text : public Book {
    public:
    void accept(BookVisitor &v) override {
        v.visit(*this);
    }
};
class Comic : public Book {
    public:
    void accept(BookVisitor &v) override {
        v.visit(*this);
    }
};
```

where

| Abstracted | Example    |
| ---------- | ---------- |
| `Book`     | `Enemy`    |
| `Text`     | `Turtle`   |
| `Comic`    | `Bullet`   |
| `accept()` | `strike()` |
| `visit()`  | `useOn()`  |

Here’s our `BookVisitor` class:

```c++
class BookVisitor {
    public:
    virtual void visit(Book &) = 0;
    virtual void visit(Text &) = 0;
    virtual void visit(Comic &) = 0;
}
```

What if we want to count our Books based on authors, Texts based on topic, Comics based on heroes?

```c++
class Catalog : public BookVisitor {
    map<string, int> cat;
    public:
    void visit(Book &b) {
        ++cat[b.getAuthor()];
    }
    void visit(Text &t) {
        ++cat[b.getTopic()];
    }
    void visit(Comic &c) {
        ++cat[b.getHero()];
    }
};
```

The concern of cataloging is nicely encapsulated in this `Catalog` class.

Under :file_folder: `lectures/se/visitor`, nothing compiles. Try figuring out why it doesn’t compile! To see the valid code, check :file_folder: `lectures/se/visitor2`. 