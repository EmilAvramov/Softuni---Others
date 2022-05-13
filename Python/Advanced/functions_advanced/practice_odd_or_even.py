command = input()
numbers = [int(i) for i in input().split()]
sum_numbers = 0

if command == "Odd":
    sum_numbers += sum([i for i in numbers if i % 2 != 0]) * len(numbers)
else:
    sum_numbers += sum([i for i in numbers if i % 2 == 0]) * len(numbers)

print(sum_numbers)
