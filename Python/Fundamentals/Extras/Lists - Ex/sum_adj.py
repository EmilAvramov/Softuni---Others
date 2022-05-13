numbers = [float(i) for i in input().split(" ")]

store_number = 0

for number in numbers:
    for i in range(len(numbers)):
        if i + 1 > len(numbers) - 1:
            break
        if numbers[i] == numbers[i + 1]:
            store_number = numbers[i] + numbers[i + 1]
            numbers.pop(i)
            numbers.pop(i)
            numbers.insert(i, store_number)
            store_number = 0

print(*numbers, sep=" ")
