import re

search = input()
sequence = input()

sent_re = r"^[A-Z].*[\.!\?]"
search_re = re.sub(r"(\w)(\d+)", r"\1{\2}|(.*\1.*){\2}", search)
split_re = r"[\.,!;\'\?\s]"
results = []

while sequence != "end":
    if re.findall(sent_re, sequence):
        sequence = re.split(split_re, sequence)
        sequence = [i for i in sequence if len(i) != 0]
        for word in sequence:
            if re.findall(search_re, word):
                results.append(word)
    sequence = input()

print(*results, sep=", ")
