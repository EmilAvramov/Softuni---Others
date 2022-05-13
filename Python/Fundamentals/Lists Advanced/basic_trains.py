index_number = int(input())
train_list = [0] * index_number
command = str(input()).split()

while command[0] != "End":
    if command[0] == "add":
        train_list[index_number - 1] += int(command[1])
    elif command[0] == "insert":
        train_list[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        train_list[int(command[1])] -= int(command[2])
    command = str(input()).split()

print(train_list)