numbers = int(input())

num_list = []

for number in range(numbers):
    num = int(input())
    num_list.append(num)

print(sum(num_list))