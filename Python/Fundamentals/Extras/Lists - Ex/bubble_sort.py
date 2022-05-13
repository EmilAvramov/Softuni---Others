numbers = [int(i) for i in input().split()]

temp_n = 0

for number in numbers:
    for i in range(len(numbers)):
        if i + 1 > len(numbers) - 1:
            break
        if numbers[i+1] < numbers[i]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            temp = 0

print(*numbers, sep=' ')
