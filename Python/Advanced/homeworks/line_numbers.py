from curses.ascii import isalpha

from sympy import Line


punct_count = 0
letter_count = 0

with open("demofile.txt", "r") as f:
    l = 0
    for line in f.readlines():
        l += 1
        for letter in line:
            if letter == ".":
                punct_count += 1
            if letter.isalpha():
                letter_count += 1
        with open("writefile.txt", "r") as f:
            f.write(f"Line {l}: {Line} {letter_count}{punct_count}")
