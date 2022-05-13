lengths = [int(i) for i in input().split()]
set_a = set()
set_b = set()

for i in range(lengths[0]):
    set_a.add(input())

for i in range(lengths[1]):
    set_b.add(input())

set_intersection = set_a.intersection(set_b)

print(*set_intersection, sep="\n")
