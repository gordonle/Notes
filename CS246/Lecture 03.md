# Lecture 3: Shell (cont.) 🐚

>  September 13, 2018

#### Using the output of a program as an argument to others

```bash
echo "Today is $(date)" // Double quotes allows embedded commands since it is one argument
echo 'Today is $(date)' // Single quotes will suppress embedded commands
echo Today is `date` // Back ticks also work, but is old formatting, nesting breaks it
echo Today is $(date) // No quotes makes each individual word an argument, so it works here
```

### grep - global regular expression print ### 

Using `egrep` (same as `grep -E` ): “`egrep ` <u>pattern</u> file(s)”

- this pattern is NOT a globbing pattern; it is a regular expression
- outputs line(s) of text that match the pattern
- case sensitive (can just use flag `-i` to make it case insensitive)

| Regex Expressions | Description                                       | Additional / Examples                                        |
| :---------------- | ------------------------------------------------- | ------------------------------------------------------------ |
| `|`               | ==Or== operator                                   | `“abc|def”`                                                  |
| `[ ]`             | Defines a set of characters that will be checked  | Can make a range with dash `a-z`<br/> Add a `^` to say ==NOT== from this set `[^ab]` |
| `?`               | 0 or 1 occurrences of the preceding expr          | `“cs?246”` will match “cs246” and “c246”                     |
| `*`               | 0 or more occurrences of the preceding expr       | `“(cs)*246”` matches “246, cscs246, ..”                      |
| `+`               | 1 or more occurrences                             | `“Ha(ha)+!”` matches “Hahahahahaha!”                         |
| `.`               | Represents <u>any</u> character                   | `.*` means any number of any character                       |
| `{ }`             | Quantifier brackets                               | `(cs){3}` means “cscscs”                                     |
| `^`               | Forces the match to <u>begin</u> with the pattern | `^cs246` does not match “hellocs246”                         |
| `$`               | Forces the match to <u>end</u> with the pattern   | `cs246$` does not match “cs246hello”                         |

**Ex**: Print all words in /usr/share/dict/words that start with an e and consists of 5 characters

- `egrep “^e....$” /usr/share/dict/words` or the expression `“^e.{4}$“` also works

**Ex**: Fetch lines of even length

- `egrep “^(..)*$” /usr/share/dict/words`

**Ex**: Files in the current directory whose name contains ==exactly one== a

- `ls | egrep “^[^a]*a[^a]*$”`

### File Permissions

`ls -l` outputs a “long listing”

\[d or - ]\[type of file]   \[shortcut]   \[owner]   \[group]   \[size in bits]   \[last modified time stamp]   \[filename]

- ie. ==-r-wr--r-x 1 g2le staff 1024 Date abc.txt==

- “d” means directory, “-” means file
- Type of File:
  - Split into 3 sections of 3 characters - ==user== bits, ==group== bits, ==other== bits (all other users)
  - r = read, w = write(modify), x = execute

#### Changing permissions

Only the owner can change permissions

- Command: `chmod` mode file(s)

- | mode | ownership class                                              | operator                                           | permission            |
  | ---- | ------------------------------------------------------------ | -------------------------------------------------- | --------------------- |
  |      | `u` - user bits<br />`g` - group bits<br />`o` - other bits<br />`a` - all | `+` - add<br />`-` - remove<br />`=` - set exactly | `r`<br />`w`<br />`x` |

- Ex: 

  - `o+r` give others read access
  - `g-x` remove execute permission from group
  - `a=r` set all permissions to read

## Shell Variables

- `x=1` (no spaces) creates variables x with <u>string</u> variable “1”
- `echo ${x}` prints out the variable

```bash
echo ${dir} // prints out directory
echo "${dir}" // prints out directory
echo '${dir}' // prints out ${dir}
```

> Single quotes will suppress converting variables to value

- PATH
  - a bunch of paths separated by `:`
  - used by the shell to search for commands/programs

## Shell Scripting

- Sequence of linux commands written in a text file `.txt` and then executed as a program
- Script: <u>basic</u> `#!/bin/bash` - known as the shebang line DONT FORGET IT YOU’LL LOSE A MARK