# Debugging Tutorial

> October 3, 2018

```bash
$ valgrind val_arg1 ... program prog_arg1
$ valgrind wc -1 < my_file
```

They run our code with valgrind, so if you fail valgrind then you fail the secret/public test.

It’s probably a good idea to add this into `runSuite` just to double check every time.

> :file_folder: `basic1.cc`
>
> ```bash
> $> valgrind ./basic1
> --> Invalid write of size 4 at main Address 0x0 is on stack
> ```

## Valgrind

### Memory leaks

```bash
$> valgrind ./sample1
--> definitely lost: 40 bytes #since when main is cut, we lose the elements array
--> possibly lost: 0
--> indirectly lost: 0
--> still reachable: 72 704 bytes
```

| Type              | Explanation                                                  |
| ----------------- | ------------------------------------------------------------ |
| `definitely lost` | leaked memory                                                |
| `possibly lost`   | might be lost                                                |
| `indirectly lost` | lost first pointer                                           |
| `still reachable` | still have a pointer to the end of the program, can delete if we want to<br />we want to see `72 704` bytes of memory here |

> :file_folder: `sample2.cc`
>
> ```bash
> $> valgrind ./sample2
> --> invalid write of size 4 at (0xff...)
> --> invalid read of size 4 at (0xff...)
> ```

> :file_folder: `sample3.cc`
>
> ```bash
> $> valgrind ./sample3
> --> conditional jump depends on uninitialized value
> ```

> :file_folder: `sample4.cc`
>
> ```bash
> $> valgrind ./sample4
> # this will print like 40 lines of error lmao
> --> deleting address (0x7ff...)
> --> 	allocated on thread #1's stack
> ```
>
> This is because of the mismatched `delete[]`
>
> | Initialize | Delete       |
> | ---------- | ------------ |
> | `new`      | `delete`     |
> | `new [ ] ` | `delete [ ]` |
> | `malloc`   | `free`       |

## GDB

`-g` disables optimization

- it will ship with copy of code
- with valgrind, will tell you line that error occurred on

```bash
gdb ./myprog
```

| Shrtcut | Commands       | Usage                                                        |
| ------- | -------------- | ------------------------------------------------------------ |
|         | `run`          | Runs the program                                             |
| `b`     | `break main`   | sets a breakpoint at `main`                                  |
| `n`     | `next`         | goes to next line of code after the breakpoint               |
| `p`     | `print <var>`  | prints the variable                                          |
|         | `up`/`down`    | goes up/down the all stack                                   |
|         | `watch <var> ` | watchpoints allow us to stop when `var` changes, can only call once it’s been initialized |
| `c`     | `continue`     | resumes running the program                                  |
| `bt`    | `backtrace`    | will print out exactly where you are, the function that called you, the stack trace, etc... |
|         | `list`         | arguments: `<line_number>`, `<file_name>` or `<file_name>:<line_number>` |
| `s`     | `step`         | step into the current line                                   |
| `f`     | `finish`       | run to the end of the function, then gives control back to you |

> :file_folder: `basic2.cc`
>
> ```bash
> $> gdb ./basic2
> (gdb) run
> 	Hello
> (gdb) break main
> (gdb) run
> 	Breakpoint set somewhere
> (gdb) next
> 	int i = 5;
> (gdb) print i
> ```

To get all the breakpoints/watchpoints information,

```bash
(gdb) info breakpoint
--> breakpoint 1 main.cc:50
--> breakpoint 2 main.cc:55
--> watchpoint 3
(gdb) delete 1 # deletes breakpoint 1
(gdb) delete # deletes all breakpoints
# shorthands: del, d
```

