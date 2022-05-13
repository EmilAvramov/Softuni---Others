lines = int(input())
chemicals = set()

for element in range(lines):
    data = input().split()
    for element in data:
        chemicals.add(element)

print(*chemicals, sep="\n")
