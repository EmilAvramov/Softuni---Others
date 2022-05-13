exclusions = (
    ",",
    ";",
    ":",
    ".",
    "!",
    "(",
    ")",
    '"',
    "'",
    "\\",
    "/",
    "[",
    "]",
    " ",
)

words = input()
for x in exclusions:
    words = words.replace(x, " ")

lower = [i for i in words.split() if i.islower() and i.isalpha()]
upper = [i for i in words.split() if i.isupper() and i.isalpha()]
mixed = [i for i in words.split() if i not in lower and i not in upper]

print(f"Lower-case: " + ", ".join(lower))
print(f"Mixed-case: " + ", ".join(mixed))
print(f"Upper-case: " + ", ".join(upper))
