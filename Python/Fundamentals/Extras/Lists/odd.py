numbers = [int(i) for i in input().split()]

count = 0

for i in numbers:
    if i % 2 == 1:
        count += 1

print(count)