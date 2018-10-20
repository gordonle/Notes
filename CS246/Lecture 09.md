# Lecture 9

> October 4, 2018

---

## Last Time: Separate Compilation

We want to be able to separate each file when compiling, and then afterwards combining the executables as needed. This is valuable to use when you have **many** files in your project, so you don’t have to recompile every time you make a small change to one file. It is the job of the **<u>linker</u>** to produce the final executable. 

**<u>Linker</u>**: Produces the final executable. 

By default, `g++` tries to compile, link, and produce an executable. The solution is to change this default:

```bash
# To only compile,
$> g++ -c main.cc
$> g++ -c vec.cc
# This tells the linker to **NOT** link and produce the executable
```

This produces ==object files==  `.o`. These files:

- contain compiled code
- info about what is defined and what is required

`g++` can also be given `.o` files :

```bash
$> g++ main.o vec.o
```

The linker then checks that all “promises” have been kept.  If all of them have been kept, then an executable is made.

## Recompilation Book Keeping

The problem at hand is that we need to keep track of which file(s) need to be recompiled. We will use the tool `make`. `Makefiles` specifies the dependencies, and the instructions on what to do when our project needs to be recompiled.

### Makefiles

> :file_folder: `lectures/tools/make/vec-example1`
>
> ```makefile
> myprogram: main.o vec.o
> 	g++ main.o vec.o -o myprogram
> 	
> vec.o: vec.cc vec.h
> 	g++ -std=c++14 -c vec.cc
> 
> main.o: main.cc vec.h
> 	g++ -std=c++14 -c main.cc
> 
> .PHONY: clean
> 
> clean:
> 	rm *.o myprogram
> ```

Then, once we are ready to compile, we call

```bash
$> make
```

Make will notice that the timestamp of different files, and it can tell which files/dependencies have been modified. If, for example, `vec.o` is newer than `myprogram`, then it will recompile to create a new executable.

==Note==: Simply “touching” or opening a file will change the timestamp.

> :file_folder: `vec-example2`
>
> ```makefile
> CXX = g++
> CXXFLAGS = -std=c++14 -Wall
> OBJECTS = main.o vec.o
> EXEC = myprogram
> 
> ${EXEC}: main.o vec.o
> 	${CXX} ${CXXFLAGS} ${OBJECTS} -o ${EXEC}
> 	
> vec.o: vec.cc vec.h
> main.o: main.cc vec.h
> .PHONY: clean
> 
> clean:
> 	rm ${OBJECTS} ${EXEC}
> ```

This `vec-example2` allows us to use variables to clean up the code a little bit. We still have lots of work to do when we need to customize the `CXXFLAGS` and `OBJECTS` values. To get all the dependencies,

```bash
$> g++ -MMD vec.cc
```

This creates a `.d` file.

> :file_folder: `vec-example3`
>
> ```bash
> CXX = g++
> CXXFLAGS = -std=c++14 -Wall -MMD
> EXEC = myprogram
> OBJECTS = main.o vec.o
> DEPENDS = ${OBJECTS: .o=.d}
> 
> ${EXEC}: ${OBJECTS}
> 	${CXX} ${CXXFLAGS} ${OBJECTS} -o ${EXEC}
> 	
> -include ${DEPENDS}
> 
> .PHONY: clean
> 
> clean:
> 	rm ${OBJECTS} ${EXEC} ${DEPENDS}
> ```
>
> The three examples we’ve covered are all functionally the same, this one is just easily customizable.

Always remember to update the `makefile` whenever you create a new file for your project. 

## Include Guards

:file_folder: `c++/separate/example3`

Try running

```bash
$> g++ -c linalg.cc
```

This will error, since `vec.h` has been included twice, resulting in multiple definitions of the struct `Vec`! 

In general, it’s very hard to keep track of which files are including what, and so to avoid calling `#include`multiple times, we use include guards.

:file_folder: `vec.h`

```c++
#ifndef VEC_H
#define VEC_H

...

#endif
```

The variable name `VEC_H` must be unique to the program. It is common practice to incorporate the file name.

We should always have include guards in ALL `.h` files.

### Final Thoughts

- Never compile `.h` files
- Never include `.cc` files
- In header `.h` files
  - Do not put `using namespace std`
  - Always use the full name (ie `std::istream`, `std::string`, etc)

## C++ Classes

In :o::o:P, a `class` is a `struct` type that can contain functions. Every C++ struct is actually a class! There is nothing that a `class` can do that a `struct` can’t. 

```c++
// student.h
struct Student {
    int assns, midterms, finals;
    float grade(); // forward declaration, no implementation
};
```

```c++
// student.cc
#include "student.h"

float Student::grade() {
	return assns * 0.4 + midterms * 0.2 + finals * 0.4;
}
```

==Note==: `::` is the scope resolution operator. So `Student::____` means “in the scope of the `Student` structure”. If we don’t include this, then the function `____` is made as a standalone function.

```c++
Student billy{80, 50, 70};

cout << billy.grade() << endl;
```

An instance of a `class` is called an `object`. Billy is an object.

A function inside a `class`/`struct` is called a <u>member function</u> or a `method`. These methods can only be called using an `object` from that class.

Within a `method`, the method can access all the fields of the object on which the method was called.

A method contains a hidden parameter named `this`. `this` is a pointer to the object on which the method was called. It references the context of the object where the method is being invoked. For example, 

```c++
this == &billy;
*this == billy;
```

Now to rewrite our `Student::grade` implementation,

```c++
float Student::grade() {
	return this->assns * 0.4 + this->midterms * 0.2 + this->finals * 0.4;
}
```

### Initializing Objects

==C-style initialization==: All the values given as fields must be **constants**

```c++
Student billy{60, 50, 70};
```

In C++, we can write special methods to construct objects. These are called `constructors`.

```c++
// student.h
struct Student {
    Student(int assns, int midterm, int finals){}; // no return type
};
```

```c++
// student.cc
Student::Student(int assns, int midterm, int finals){
    this->assns = assns;
    this->midterm = midterm;
    this->finals = finals;
}
```

Now, writing `Student bily{60, 50, 70}` calls this constructor method.
