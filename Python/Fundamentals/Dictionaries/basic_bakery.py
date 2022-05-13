string = input().split()
bakery = {}

for i in range(0, len(string), 2):
    key = string[i]
    value = string[i + 1]
    bakery[key] = int(value)

print(bakery)