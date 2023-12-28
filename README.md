**Want to do some replacing which includes processing, but cannot be bothered learning awk?**

With awk3 you can write advanced text processing code using python.

## Installation

`pip install git+https://github.com/ridulfo/awk3.git`

## Examples:

### Increment all numbers in the text files

A command to run `int(m[0]) + 1` on every match of `(\d+)` in all `.txt` files:

`find *.txt | xargs cat | awk3 "(\d+)" "int(m[0]) + 1"`

### Capitalize all week days

`cat weekdays.txt | awk3 "([a-zA-Z]+day)" "m[0].capitalize()"`

or

`awk3 -f weekdays.txt "([a-zA-Z]+day)" "m[0].capitalize()"`

## Help `awk3 --help`

```
usage: awk3 [-h] [-f F] pattern code

A simple awk implementation

Takes a file or stdin, a pattern and some python code.
Outputs the processed text to stdout.

The "pattern" is a regex pattern that will be matched against the file.
The "code" is python code that will be evaluated for every match. The python
code has access to a local variable `m` which is a tuple of the matched groups.

Example:
$ cat file.txt
Adam, 23
Bob, 24
Charlie, 25
$ awk3 file.txt "(\d+)" "int(m[0]) + 1"
Adam, 24
Bob, 25
Charlie, 26

positional arguments:
  pattern     pattern to match
  code        python code to calculate replacement

options:
  -h, --help  show this help message and exit
  -f F        path to file
```
