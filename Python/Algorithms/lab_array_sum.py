def array_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]

    return numbers[idx] + array_sum(numbers, idx + 1)


data = [int(i) for i in input().split(" ")]

print(array_sum(data, 0))
