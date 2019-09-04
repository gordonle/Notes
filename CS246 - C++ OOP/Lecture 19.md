# Lecture 19: Big 5 Revisited, More Design Patterns

> November 12, 2018

---

## Big 5: Parent vs Child Classes

```c++
class Book {
    // Big 5 implemented
};
class Text : public Book {
    // Big 5 not implemented
};
```

Let’s create instances of `Text`

```c++
Text t1 = {---, ---, ---, ---};
Text t2 = t1;
```

This is the **free copy constructor** that is called:

```c++
Text::Text(const Text &other): Book(other), topic(other.topic) {}
```

As well, this is our **free assignment operator** that is given to us

```c++
Text &Text::operator=(const Text &other) {
    Book::operator=(other);
    topic = other.topic;
    return *this;
}
```

In our move constructor (**incorrectly implemented**),

```c++
Text::Text(Text &&other) : Book(other), topic{other.topic} {}
```

** Review the differences between `rvalue` and `lvalue` **

`other` is an <u>rvalue</u> reference; it is an <u>lvalue</u>. Thus, the copy constructor is being called. We have not gained any efficiency. 

The C++ library has a function `std::move` which allows us to treat an lvalue <u>as if it was an rvalue</u>.

The **correct** implementation of the above is as follows,

```c++
// Move Constructor
Text::Text(Text &&other) : Book{std::move(other)}, topic{std::move(other.topic)} {}

// Move Assignment Operator
Text &Text::operator=(&&other) {
    Book::operator(std::move(other));
    topic = std::move(other.topic);
    return *this;
}
```

Now, which assignment operator will run?

```c++
Text t1{"abc", "Nomair", 400, "CS246"};
Text t2{"xyz", "Dave", 200, "CS136"};
Book *pb1 = &t1;
Book *pb2 = &t2;
*pb1 = *pb2; // object assignment through Base class pointers
// t1 is now equal to {"xyz", "Dave", 200, "CS246"};
```

`Book::operator=` is called! We have done **partial assignment**, and this is a problem.

## Partial Assignment Problem

We noticed that the `topic` field was not copied. We could make `operator=` a virtual method to fix this. 

```c++
class Book {
    public:
    virtual operator=(const Book &);
};
class Text : public Book {
    Text &operator=(const Text &) override;
};
```

> This is **NOT** an actual override! The code will not compile. Why?

The signatures of our assignment operators **do not match** - one is a `Book` reference, the other is a `Text` reference. To fix this, we correct the parameters in our override function.

```c++
class Text : public Book {
    Text &operator=(const Book &) override; // this is now a valid override
}
```

This allows assignment to `Text`s from any type of Book. But now we have a **mixed assignment problem**! We will discuss this at a later time. For now, lets talk about how to **avoid partial assignment**

To prevent this, let’s prevent assignment through base class pointers. Options include:

- Could make `Book::operator=` **private**
  - This is flawed, since subclasses still need access to this. It is too restrictive
- Could make `Book::operator=` **protected**
  - But we still cannot assign a `Book` to another `Book`!
- We should make `Book` an **abstract class** instead, with a pure virtual assignment operator.

> Look at the `Abstract_Book_Class_UML.png` diagram

AbstractBook has a protected `operator=`

```c++
Text t1{---}, t2{---};
AbstractBook *pt1{&t1};
AbstractBook *pt2{&t2};
*pt1 = *pt2; // will not compile, as AbstractBook::operator= is protected
```

## Factory Method Pattern

> View `Factory_Method_UML.png` 

```c++
class Level {
    public:
    virtual Enemy *createEnemy() = 0; // pure virtual
};
class Normal : public Level {
    public:
    Enemy *createEnemy() override {
        // more turtles, less bullets
    }
};
class Castle : public Level {
    public:
    Enemy *createEnemy() override {
        // more bullets, less turtles
    }
};
```

So now, we can create a sort of “game”,

```c++
Player *p =;
Level *l = ;
Enemy *e = ;
while (p->isNotDead()) {
    // generate enemy
    e = l->createEnemy();
    // attack players
}
```

What if we wanted to create a secret/new type of level? What about new types of enemies? We can easily create a new subclass of `Level` or `Enemy`, which is very easy. 

This is also called the Virtual Constructor Pattern, as the factory method acts like a constructor

- ie. Iterator::begin and end functions, addToFront, etc.

## Template Method Pattern

The Template Method Pattern is used when a class wants subclasses to override some but not all methods.

> View `Template_Method_UML.png`

```c++
class Turtle {
    public:
    void draw() {
        drawHead();
        drawShell();
        drawFeet();
    }
    private:
    void drawHead(){...}
    void drawFeet(){...}
    virtual void drawShell = 0;
}

class GreenTurtle : public Turtle {
    // to be completed next class    
};
```

