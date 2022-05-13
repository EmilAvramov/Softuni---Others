initial = [i.split() for i in input().split("|")]
initial = initial[::-1]
initial = [i for elem in initial for i in elem]

print(*initial, sep=' ')