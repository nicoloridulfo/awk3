#!env/bin/python
import re
import os
import sys
import argparse

# https://docs.python.org/3/library/argparse.html


def repl_func(match, repl) -> str:
    """
    Takes the matched and returns a string returned by the python code in repl
    """
    m = match.groups()
    return str(eval(str(repl)))


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""A simple awk implementation

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

""")

    parser.add_argument("-f", help="path to file")
    parser.add_argument("pattern", help="pattern to match")
    parser.add_argument("code", help="python code to calculate replacement")
    args = parser.parse_args()

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        if args.f:
            with open(args.f) as f:
                text = f.read()
        else:
            print("No file or stdin")
            sys.exit(1)

    pattern = args.pattern
    code = args.code
    print(re.sub(pattern, lambda match: repl_func(match, code), text), end="")