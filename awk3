#!env/bin/python
import re
import fire
import os


def repl_func(match, repl) -> str:
    """
    Takes the matched and returns a string returned by the python code in repl
    """
    m = match.groups()
    return str(eval(str(repl)))


def main(path=".", pattern="", code=""):
    """
    Takes a path to a file, a pattern to match and a replacer (python code).
    Prints the file with the replacement to stdout,

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

    """
    assert path != "", "path is empty"
    assert pattern != "", "pattern is empty"
    assert code != "", "replacement python code is empty"

    if not os.path.isfile(path):
        print(f"path {path} is not a file")
        exit(1)

    with open(path, "r") as f:
        print(re.sub(pattern, lambda match: repl_func(match, code), f.read()))

if __name__ == "__main__":
    fire.Fire(main)
