**Want to do some replacing which includes processing, but cannot be bothered learning awk?**

With awk3 you can write advanced text processing code using python.

## Examples:

### Increment all numbers in the text files
A command to run `int(m[0]) + 1` on every match of `(\d+)` in all `.txt` files:

`$ find *.txt | xargs -I{} ./awk3 {} "(\d+)" "int(m[0]) + 1"`

### Capitalize all week days
`$ ./awk3 weekdays.txt "([a-zA-Z]+day)" "m[0].capitalize()"`


## Help `./awk --help`

```
NAME
    awk3 - Takes a path to a file, a pattern to match and a replacer (python code). Prints the file with the replacement to stdout,

SYNOPSIS
    awk3 <flags>

DESCRIPTION
    The "pattern" is a regex pattern that will be matched against the file.
    The "code" is a python code that will be evaluated for every match. The python
    code can use the variable `m` which is a tuple of the matched groups.

    Example:
    $ cat file.txt
    Adam, 23
    Bob, 24
    Charlie, 25
    $ ./awk3 file.txt "(\d+)" "int(m[0]) + 1"
    Adam, 24
    Bob, 25
    Charlie, 26

FLAGS
    --path=PATH
        Default: '.'
    --pattern=PATTERN
        Default: ''
    -c, --code=CODE
        Default: ''
```