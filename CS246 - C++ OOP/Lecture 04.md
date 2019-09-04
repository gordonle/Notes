# Lecture 4: Shell Scripting (cont.) 💻

> September 18, 2018

- A text file containing a sequence of linux commands executed as a program

### Script File

`shell/scripts/basic`

```bash
#!/bin/bash
date
whoami
pwd
```

When executing scripts, the shell searches all directories listed in `${PATH}`. If you try to run a script not in one of these path directories it will not work. However, you can **<u>run a script</u>** in any directory using

```bash
./script
```

where your working directory contains the `script` file.

### Passing Arguments to Scripts

```bash
./script arg1 arg2 arg3 ...
```

#### Accessing The Arguments

```bash
$1 #contains arg1
$2 #contains arg2
```

> **<u>Ex 1:</u>** Is a word in the dictionary?
>
> ```bash
> #!/bin/bash
> egrep "^$1$" /usr/share/dict/words
> ```
>
> - We don’t need to escape the characters - the shell is smart enough to tell
> - This script just prints out the word if it finds it in the dictionary

> **<u>Ex 2:</u>** “Good Password” lets you know if the given argument is a good password
>
> ```bash
> #!/bin/bash
> egrep "^$1$" /usr/share/dict/words > /dev/null
> ```
>
> - `/dev/null` is where output goes to die (it will vanish)

#### Exit Status Code

Every process exits with a **status code**:

| Status Code | Result  |
| ----------- | ------- |
| 0           | Success |
| Non-zero    | Failure |

`$?` contains the status code for the last process.

### If Statement Syntax

```bash
if [ $? -eq 0 ];then
	echo "Not a good password"
else
	echo "Maybe a good password"
fi
```

> **<u>Note</u>**: The spaces in the test command `[ $? -eq 0 ]` are essential. Arguments must be separated by spaces.

Append this to the bottom of **Ex. 2** for the complete script.

#### Else If Syntax

```bash
if [ condition ]; then
	codeblock
elif [ condition ]; then
	codeblock
else
	codeblock
fi
```

#### Comparisons

| Integer | Purpose                  |
| ------- | ------------------------ |
| `-eq`   | Equal                    |
| `-ne`   | Not Equal                |
| `-lt`   | Less than                |
| `-le`   | Less than or equal to    |
| `-gt`   | Greater than             |
| `-ge`   | Greater than or equal to |

| String | Purpose    |
| ------ | ---------- |
| `=`    | Equals     |
| `!=`   | Not Equals |

| General | Purpose |
| ------- | ------- |
| `-a`    | and     |
| `-o`    | or      |
| `!`     | not     |
| `-e`    |         |

#### Adding Checks for Proper Arguments

The file we just wrote is called `goodPassword`. `goodPasswordCheck` checks to ensure that the user is using the script correctly.

```bash
if [ ${#} -ne 1 ]; then
	echo "Usage: $0 password" >$2
	exit 1
fi
```

`${#}` is the number of arguments to the script.

`$0` is the name of the program being executed.

`exit` terminates the script.

### Sub-routines

```bash
mysubroutine () {
	echo nice
	exit 1
}

if [ #is this true# ];then
	mysubroutine
fi
```

Subroutines are only executed when they are called. When calling subroutine with arguments, add them to the call and separate them with spaces.

```bash
mysubroutine arg1 arg2 arg3
```

### While Loop

Remember, all variables are of type **string**

```bash
# Print #s from 1 to $1
#!/bin/bash
x=1
while [ ${x} -le $1 ]; do
	echo ${x}
	x=$((x+1)) # syntax for arithmetic
done
```

### For Loop

```bash
for x in a b c d; do echo ${x}; done
```

> **<u>Ex 1:</u>** Let’s try to rename all `.cpp` files to `.cc`
>
> To do this, we will have to hold the name of the file in a variable
>
> ```bash
> file = Hello.cpp
> mv ${file} ${file%pp}c # if the end of the string ends in pp, remove it
> ```
>
> We simply concatenate the “c” onto the end by placing it after.
>
> File: `renameC`
>
> ```bash
> #!bin/bash
> # Renames all .C files in the current directory to .cc
> 
> for name in *.C; do
> 	mv ${name} ${name%C}cc
> done
> ```
>
> Note the use of the **<u>globbing pattern</u>** in the for loop

> **<u>Ex 2:</u>** How many times does `$1` appear in the file `$2`?
>
> ```bash
> #!/bin/bash
> # Prints the number of times word ${1} occurs in file ${2}
> count = 0
> for word in $(cat $2); do			 # make sure to wrap command in $()
> 	if [ ${word} = ${1} ]; then
> 		count = $((count + 1))
> 	fi
> done
> echo ${count}
> ```
>
> What if we want to check for phrases instead of words? We can try
>
> ```bash
> ./countWords "A phrase" ../sample.txt # THIS DOESN'T WORK
> ```
>
> but this errors because of the string comparison in the `if [ ${word} = ${1} ]`. To try to fix this, we put it in quotes
>
> ```bash
> if [ ${word} = "${1}" ];
> ```
>
> but `echo ${count}` will always output `0` when we input phrases. To do this properly we need to do a LOT more work.

#### Find the last Friday of the Month

```bash
# cal displays the current month, in grid form
cal | awk ' { print $6 } ' | egrep [0-9] | tail -1
```

Check `cat payday` to see an example.

```bash
echo -n "test" # the -n prevents a newline from being printed
```

