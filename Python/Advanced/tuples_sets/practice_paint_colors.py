from collections import deque

string = deque([i for i in input().split(" ")])

main = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]
found = []
final = []

while len(string) > 0:
    if len(string) == 1:
        first = string.pop()
        last = ""
    else:
        first = string.popleft()
        last = string.pop()

    if first + last in main or first + last in secondary:
        found.append(first + last)
    elif last + first in main or last + first in secondary:
        found.append(last + first)
    else:
        first = first[0:-1]
        last = last[0:-1]
        if first:
            string.insert(len(string) // 2, first)
        if last:
            string.insert(len(string) // 2, last)

for i in range(len(found)):
    if found[i] in main:
        final.append(found[i])
    else:
        if found[i] == "orange":
            if "red" in found and "yellow" in found:
                final.append(found[i])
        if found[i] == "purple":
            if "red" in found and "blue" in found:
                final.append(found[i])
        if found[i] == "green":
            if "yellow" in found and "blue" in found:
                final.append(found[i])

print(final)
