import re

names = input()
regex = r"\b" \
        r"(?P<day>\d{2})" \
        r"([-.\/])" \
        r"(?P<month>[A-Z][a-z]{2})" \
        r"\2" \
        r"(?P<year>\d{4})" \
        r"\b"
matches = re.findall(regex, names)

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
