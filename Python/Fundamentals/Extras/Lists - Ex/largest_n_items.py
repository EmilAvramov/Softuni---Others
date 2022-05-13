numbers = [int(i) for i in input().split()]
count = int(input())

largest_list = []
largest = 0

for i in range(count):
    largest = max(numbers)
    largest_list.append(numbers.pop(numbers.index(largest)))

print(*largest_list, sep=' ')

