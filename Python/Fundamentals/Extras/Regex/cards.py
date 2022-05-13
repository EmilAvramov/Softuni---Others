import re

regex = r"[23456789][SHDC]|" \
        r"[1][0][SHDC]|" \
        r"[JQKA][SHDC]"

cards = input()

matches = re.findall(regex, cards)

print(*matches, sep=" ")
