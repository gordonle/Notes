# Final Exam Review

> December 14th, 2018

## Partial Assignment VS Mixed Assignment

**<u>Partial Assignment</u>**: Say you have a `Base` class with two children classes, `Child1` and `Child2`. The signature for the = operator for the Base class is `virtual Base &Base::operator=(const Base &other)`. If I want to override this, we do

```c++
class Base {
    public:
    virtual Base &operator=(const Base &);
};

class Child1 : public Base {
    public:
    Child1 &operator=(const Base &); // overrides it
};

// if we call Child1's =operator with a Child2, then we have mixed assignment
```

Basically partial is when you cant get everything, mixed is when you mix the assignment of two different sub-classes.

## vTables

look over this lmao

## Compiler Variables

```c++
int main() {
    #ifdef DEBUG
    cout << "debugging" << endl;
    #endif
}
```

To define `DEBUG`, you run the bash command

```bash
$> g++14 -DEBUG
```

