string = input().lower().split()
dict_string = {}

for i in string:
    if string.count(i) % 2 == 1:
        dict_string[i] = string.count(i)

print(*dict_string.keys(), sep=', ')
