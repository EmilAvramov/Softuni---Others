num_list = input().split()
num_dict = {}

for i in num_list:
    num_dict[i] = num_list.count(i)

for key, value in sorted(num_dict.items()):
    print(f'{key} -> {value} times')
