numbers = str(input()).split()
skip = int(input())

index = skip - 1
result = []

while len(numbers) != 0:
    if skip >= len(numbers) and len(result) == 0:
        index = (index + skip - 1 * (skip // len(numbers))) % len(numbers)
    result.append(numbers.pop(index))
    if len(numbers) == 0:
        break
    else:
        index = (index + skip - 1) % len(numbers)

print(str(result).replace(' ', '').replace('\'', ''))
