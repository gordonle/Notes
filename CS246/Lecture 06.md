# 	Lecture 6: More I/O, Streams

>  September 25, 2018

## Strings in C++

- C used null terminated char arrays
  - This required manual memory management
- C++ provides a `<string>` header
  - This automatically resizes as needed

#### Defining a String

```c++
string str = "hello";
```

- C++ magic is converting the C-style string `“hello”` into the C++ string `string s`

#### String Functionality

In C++, we aren’t comparing pointers as we were in C, so a lot of comparisons become much more efficient

| C++                                | C                                                 | Usage                                |
| ---------------------------------- | ------------------------------------------------- | ------------------------------------ |
| `==`, `!=`, `<`, `>`, `<=`, `>=`   | `strcmp`                                          | Comparing the contents of the string |
| `str.length()`                     | `strlen`                                          | Gets the length of the string        |
| `str[0]`, `str[1]`                 | `str[0]`, `str[1]`                                | Accessing characters                 |
| `s3 = s1 + s2` or <br />`s1 += s2` | `strcat(s1, s2)`<br />s1 had to have enough space | Concatenation of strings             |
| `cin`                              | `scanf`, `%d`, `%s`                               | Reads input                          |
| `cout`                             | `printf`, `%x`                                    | Prints to stdout                     |

==Note==: `scanf` and `printf` are also valid C++ code, but we don’t use them in CS246

> #### Recommended way to initialize variables
>
> ```c++
> string s{"Hello"};
> int x{5};
> ```
>
> - This is recommended because there are certain situations, such when defining classes, the ==old way== of initialization won’t work
> - The recommended way works ==always==

#### Reading Strings

:open_file_folder: `io/readStrings.cc`

```c++
int main() {
    string s;
    cin >> s; 	// since it's defined as a string, it will only accept string input
    cout << s << endl;
}
```

- `cin` reads from first non-whitespace char to first whitespace
- to read an entire line, use `getline(cin, s)`
  - this reads everything on `stdin` until a newline

```c++
int x = 95;
cout << x; // prints in decimal
```

### I/O Manipulators (`iostream`, `iomanip`)

| Manipulator       | Purpose                                                    |
| ----------------- | ---------------------------------------------------------- |
| `hex`             | Prints in hexadecimal                                      |
| `dec`             | The ==decimal== manipulator                                |
| `showpoint`       | Shows decimal                                              |
| `setprecision(x)` | Specifies the decimal points                               |
| `boolalpha`       | Takes “true” or “false” and turns them into boolean values |

- I/O Headers
  - change the way `cout` works
  - are sticky
    - That means that after using `hex`, all subsequent `cout` will apply `hex` 

```c++
// Examples
cout << hex << x;
cout << dec;
cout << showpoint << setprecision(3); // specifies decimal points
```

## Reading/Writing Files

The ==“stream abstraction”== can work on other sources of data.

- In the header, we `#include <fstream>` to read and write files
  - `ifstream` to read from files
  - `ofstream` to write to files

:file_folder: `fileInput.cc`

```c++
#include <iostream>
#include <fstream> using namespace std;
int main() {
   // type  varname  initialization
	ifstream myfile{"file.txt"}; 	// this opens the file to read
    string s;
    while (myfile >> s) { 			// myfile is the equivalent to cin
        cout << s << endl;
    }
}
```

- Anything we can do with `cin` (type ==istream==), we can do with `myfile` (type ==ifstream==)
  - Same applies with `cout` and a variable of type ==ofstream==

==Note==: When you open a file, you must also close it. How is it closed:

- `myfile` is stack allocated, so it’s destroyed when it goes out of scope
  - when it is destroyed, it closes the file!

### Reading/Writing to Strings

To do this, we include the header `<sstream>` (string stream)

- `istringstream` to read from strings
- `ostringstream` to write to strings

:file_folder: `buildString.cc`

```c++
#include <sstream>
int lo = ~;
int hi = ~;
ostringstream oss;
oss << "Enter a num between " << lo << "and " << hi;
string s = oss.str(); // retrieves the string created previously and stores it into the var
```

:file_folder: `getNum.cc/` 

```c++
// this will insist the user inputs a number
#include <sstream>
int n;
while (true) {
    cout << "Enter a number" << endl;
    string s;
    cin >> s; 			// this will succeed for any given input
    // Make sure to check for an EOF here, and break out of the loop
    if (cin.eof()) break;
    
    istringstream iss{s};
    if (iss >> n) { 	// this tries to store s into n
        break;
    } else {
        cout << "Not a Number. Try again" << endl;
    }
}
```

we can also refactor the above code to

```c++
string s;
while (true) {
    cout << "Enter a number" << endl;
    int n;
    if (cin >> s) {
        istringstream iss{s};
        if (iss >> n) {
            break;
        } else {
            cout << "Not a Number. Try again" << endl;
        }
    }
}
```

## Functions

In C++ we are able to define default arguments, as well as create functions that have the same name! Let’s take a look.

### Default Arguments

```c++
// Defining the Function
void printFile(string file = "myfile.txt") {
    ifstream f{file};
}
// Calling the Function
printFile(); 				// uses default argument "myfile.txt"
printFile("hello.txt") 		// uses new arg "hello.txt" instead
```

==Note==: Parameters with default arguments **<u>must appear last</u>**

```c++
// Defining
void test(int num = 5, string str){}				// ILLEGAL
void test2(int num = 5, string str = "hello"){} 	// LEGAL
// Calling
test2(10, "foo"); 		// LEGAL
test2(10);				// LEGAL
test2();				// LEGAL
test("foo");			// ILLEGAL
test(, "foo");			// ILLEGAL
```

### Function Overloading

```c++
int negate(int i) {return -i}
int negate(bool b) {return !b}
```

- C++ allows functions with the same name ==as long as the # of parameters and/or types differ==
  - Differing on return types is **<u>not enough</u>** 

