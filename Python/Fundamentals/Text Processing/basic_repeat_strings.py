string = str(input()).split()
result = [i * len(i) for i in string]

print(*result, sep='')
