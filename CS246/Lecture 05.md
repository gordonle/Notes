# Lecture 5: Testing, C++ Intro :desktop_computer:

> September 20, 2018

### Misconceptions:

- Testing is not the same as debugging
- Testing does not guarantee correctness
  - can only prove presence of defects

### Writing Tests

- Write small tests that focus on one thing at a time
- Check various classes of input
  - ie. numeric ranges, positive, negative, zero
  - boundaries between ranges (edge cases)
  - simultaneous boundaries (corner cases)
- Always make sure to read assignments carefully, pay attention to details

## C++

- Developed by Bjarne Stroustrup
  - Simula 67 was the first Object-Oriented (OO) language
  - Added OOP concepts to C and called it “C with classes”
    - Now renamed to **C++**
      - Standards are C++99, C++03, C++14, C++17 (all stable)
      - We use C++14
- Most C programs are valid C++ programs, to this day

> ### **Hello World in C++**
>
> ```c++
> #include <iostream> using namespace std;
> 
> int main() {
> 	cout << "Hello World" << endl;
>     return 0;
> }
> ```
>
> Notice that `stdio.h` is not included, and we didn’t use `printf`
>
> - that would have been legal in C++
> - but is **<u>forbidden</u>** in CS246
>
> Instead, do this:
>
> ```c++
> // Include iostream
> #include <iostream> using namespace std;
> 
> // Producing Output
> std::cout<<data1<<data2;std::endl;
> ```
>
> Adding `using namespace std` allows us to refer to `std::cout` or `std::endl` by just `cout` or `endl`

### Compiling C++ Programs

- We use the compiler `g++`

```bash
$> g++ -std=c++14 myfile.cc -o myprog # compiled into a file named "myprog"
$> g++14 myfile.cc # this is an alias, without -o default executable is named "a.out"
```

- if “a.out” already exists, it will be overwritten

### C++ I/O

- Including `iostream` gives us access to 3 I/O variables

| Variable    | Purpose                                 | Operator | Ex                     |
| ----------- | --------------------------------------- | -------- | ---------------------- |
| `std::cin`  | To read from stdin (similar to `scanf`) | `>>`     | `std::cin >> x`        |
| `std::cout` | To write to stdout                      | `<<`     | `std::cout << x`       |
| `std::cerr` | To write to stderr                      | `<<`     | `std::cerr << “ERROR”` |

> Adding two numbers
>
> :file_folder: `/c++/intro/plus.cc`
>
> ```c++
> #include <iostream> using namespace std;
> 
> int main() {
>     int x, y;
>     cin >> x >> y;
>     cout << x+y << endl;
> }
> ```

**<u>Note:</u>** 

- `cin` will read the first non-whitespace character until it hits whitespace. Other than separating inputs, **whitespace is being ignored**.
- If a read fails because
  - of bad input type, the variable will be set to **0**
  - there is no more input (EOF `Ctrl+d`) the variable is also set to **0**
- If a read fails, the expression `cin.fail()` is **true**
- If a read fails due to EOF, both `cin.fail()` and `cin.eof()` are **true**

> ### Read all ints from stdin and echo them to stdout. Stop if a read fails.
>
> :file_folder: `io/readInts/cc`
>
> ```c++
> #include <iostream> using namespace std;
> int main() {
>     int i;
>     while(true) { // Infinite loop
>         cin >> i;
>         if (cin.fail()) break;
>         cout << i << endl;        
>     }
> }
> ```

Let’s look at refactoring this code.

- C++ defines on automatic conversion from a `istream` (input stream) type to `boolean`

  - `cin` has type `istream`
  - `cout` has type `ostream`

- This means that you can use `cin`, `cout`, `cerr` wherever a `boolean` is defined

- So, instead of using `cin.fail()`, we can use `!cin`:

  ```c++
  // Old
  if (cin.fail()) break;
  // New
  if (!cin) break;
  ```

- In C++, `>>` can act as both the input operator and the ==bit shift operator==.

  - This is called **operator overloading**

    ```c++
    cin >> i // input
    int x = _;
    x >> 3; // right bit shift
    ```

  - `cin >> i` will produce `cin`

    - `cin >> x >> y` reduces to `cin >> y` reduces to `cin`

  - Refactored code:

    ```c++
    // Old
    while(true){
        cin >> i;
        if (!cin) break;
        cout << i << endl;
    }
    // New
    while(true){
        if (!(cin >>i)) break;
        cout << i << endl;
    }
    ```

- Then, moving this into the `while` condition, we have finally

  ```c++
  int main() {
  	int i;
      while(cin >> i) {
          cout << i << endl;
      }
  }
  ```

> ### Read all ints & echo them to stdout until EOF. Skip non-integer input
>
> :file_folder:	`readInts5.cc`
>
> ```c++
> int main() {
>     int i;
>     while(true) {
>         if (cin >> i) {
>             cout << i << endl;
>         } else {
>             if (cin.eof()) {
>                 break;
>             } else {
>                 // this is where we have to acknowledge the read fail
>                 cin.clear();
>                 // this is where we throw away the offending character
>                 cin.ignore();
>             }
>         }
>     }
> }
> ```
>
> - When a read fails, all subsequent reads also fail unless the fail is acknowledged with `cin.clear()`
> - We need to throw away the offending character and move on. Do this with `cin.ignore()`

