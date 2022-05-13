names = str(input()).split(', ')

print(sorted(names, key=lambda x: (-len(x), x)))
