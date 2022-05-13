factor = int(input())
length = int(input())

num_list = []

for i in range(1, length + 1):
    num_list.append(factor * i)

print(num_list)
