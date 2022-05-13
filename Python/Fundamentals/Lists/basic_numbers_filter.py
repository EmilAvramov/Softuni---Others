rows = int(input())

num_list = []

for i in range(1, rows + 1):
    number = int(input())
    num_list.append(number)

command = str(input())
if command == "even":
    for i in range(len(num_list) - 1, - 1, - 1):
        if num_list[i] % 2 != 0:
            num_list.remove(num_list[i])
elif command == "odd":
    for i in range(len(num_list) - 1, - 1, - 1):
        if num_list[i] % 2 == 0:
            num_list.remove(num_list[i])
elif command == "negative":
    for i in range(len(num_list) - 1, - 1, - 1):
        if num_list[i] >= 0:
            num_list.remove(num_list[i])
elif command == "positive":
    for i in range(len(num_list) - 1, - 1, - 1):
        if num_list[i] < 0:
            num_list.remove(num_list[i])

print(num_list)