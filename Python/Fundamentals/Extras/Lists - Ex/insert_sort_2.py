numbers = [int(i) for i in input().split()]

for i in range(1, len(numbers)):
    current = numbers[i]
    previous = i-1
    while previous >= 0 and current < numbers[previous]:
        numbers[previous+1] = numbers[previous]
        previous -= 1
    numbers[previous+1] = current

print(*numbers, sep=' ')
