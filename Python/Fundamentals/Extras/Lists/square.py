numbers = [int(i) for i in input().split() if (abs(int(i)) ** 0.5).is_integer() and int(i) > 0]

print(*sorted(numbers, reverse=True), sep=' ')