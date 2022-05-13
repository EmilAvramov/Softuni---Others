numbers = [int(i) for i in input().split()]

for index, value in enumerate(numbers):
    if value % 2 == 1 and index % 2 == 1:
        print(f'Index {index} -> {value}')
