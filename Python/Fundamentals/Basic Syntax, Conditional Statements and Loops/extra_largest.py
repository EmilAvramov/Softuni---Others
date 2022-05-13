number = int(input())

num_list = []
concat = ""

for char in str(number):
    num_list.append(char)

num_list_sorted = sorted(num_list, reverse=True)

for sort_num in num_list_sorted:
    concat += sort_num

print(concat)

