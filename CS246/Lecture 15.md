# Lecture 15: Composition, Aggregation, Inheritance

> October 30, 2018

**Note**: UML drawings are omitted from this file. They are available in the CS246 directory, or can be found online.

## Composition

Composition creates a **OWNS-A** relationship

> Car OWNS-A carParts
>
> Catalog HAS-A carParts (`carParts` should not be destroyed with `Catalog`)

### HAS-A

A class `A` **HAS-A** class `B`:

- `B` is not copied if `A` is copied (shallow)
- `B` is not destroyed if `A` is

```c++
class catalog {
    Part *parts[10]; // Pointers to objects
};
```

`catalog` doesn’t contain the objects, but rather points to them. 

## Inheritance

In C, to create an array of different types of `Book`s we can use union types. Alternatively, we could also use a `void ptr`

### IS-A

Observe that:

- `Text` IS-A `Book` (with an additional `topic` field)
- `Comic` IS-A `Book` (with an additional `hero` field)

In this case, `Book` is referred to as the

- base class
- superclass
- parent

and `Text` and `Comic` are referred to as the

- derived classes
- subclasses
- child classes

Now, to do this in C++:

:file_folder: `c++/inheritance/example1`

```c++
class Book {
    string title, authors;
    int numPages;
    public:
    Book(string title, string author, int numPages)
        : title{title}, author{author}, numPages{numPages} {}
};

class Text : public Book {
    string topic;
};

class Comic : public Book {
    string hero;
    
};
```

Derived classes inherit members(fields/methods) from the base class. Any method that we can call on `Book` can also be called on `Text` and `Comic`.

This is because of inheritance! `ifstream`/`istringstream` objects act like `istream` objects. 

### Inheriting Private Members

`Text` inherited the private fields from `Book`

```c++
int main() {
    Text t = ~~~;
    t.author = ~~~; // won't compile
}
```

What if we are inside Text?

```c++
Text::Text(string title, string author, int numPages, string topic)
    : title{title}, author{author}, numPages{numPages}, topic{topic} {}
```

This won’t compile for the following reasons:

1. inherited fields were private in `Book`
   1. MIL can only refer to private fields declared in the class
2. Steps of object creation (for inherited classes):
   1. Space is allocated
   2. superclass part is constructed
   3. subclass field initialization / MIL
   4. constructor body runs

Step 2 fails, as `Book` does not have a default constructor. To fix this, we’ll make MIL hijack step 2 as well.

```c++
Text::Text(string title, string author, int numPages, string topic)
    : Book(title, author, numPages), topic{topic} {}
```

**The order matters**. Make sure you begin with the constructor call to your superclass first, then initialize other fields.

If we want subclasses to have access to our `private` members, we can change them to 	`protected`.

### Protected Access

```c++
class Book {
    protected:
    string author;
};

class Text: public Book {
    void addAuthor(string newAuth) {
        author += newAuth;
    }
};
```

Anything defined in `protected` ca be accessed by the class and any subclasses. Note

```c++
int main() {
    Text t = ~~~;
    t.author = ~~~; // STILL invalid, since we are trying to access from outside
}
```

> In **UML**, use `#` for `protected`

**<u>Claim</u>**: `private` > `protected`. A class is responsible for maintaining its invariant. If you give protected access to your children, you are trusting them to maintain your invariant. `protected` breaks encapsulation, much like how `friend` does.

In general, keep fields `private`, provide `protected` methods for subclasses. In doing so, we can maintain invariance in our methods by writing whatever checks we need.

```c++
class Book {
    string author;
    protected:
    void addAuthor(string auth) {
        // add invariant check here
        author += auth
    }
};
```

## Method Overriding

:file_folder: `c++/inheritance/example2`

`isHeavy` is a method we want to implement for `Book` that has unique behaviour depending on the class that it is being called from, say: Book > 200 | Text > 300 | Comic > 30

```c++
class Book {
    int numPages;
    int getNumPages() const {
        return numPages;
    }
    bool isHeavy const;
};
bool Book::isHeavy() const { return numPages > 200; }
bool Text::isHeavy() const { return getNumPages() > 300; }
bool Comic::isHeavy() const { return getNumPages() > 30; }
```

The `isHeavy()` method is overridden three times for the three classes. 

```c++
Book b{~~, ~~, 100};
b.isHeavy(); // returns FALSE
Comic c{~~, ~~, 40, "batman"};
c.isHeavy(); // returns TRUE
```

We have not taken advantage of the **IS-A** relationship between `Book` and `Comic`! So,

```c++
// The following is legal since Comic IS-A Book
Book b = Comic{~~, ~~, 40, "superman"};
b.isHeavy(); 
```

What does `b.isHeavy()` call? It calls `Book::IsHeavy()`, since when we defined `b` we are actually calling the **copy constructor** of `Book`. The parameter “superman” is thrown away. This is known as **object coercion**/**slicing**. To prevent this from occurring, we can use pointers instead.



