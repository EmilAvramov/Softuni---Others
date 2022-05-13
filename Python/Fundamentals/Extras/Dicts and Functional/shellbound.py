from math import ceil

command = input().split(" ")

shell_dict = {}

while command[0] != "Aggregate":
    location = command[0]
    size = int(command[1])
    if location not in shell_dict.keys():
        shell_dict[location] = [size]
    else:
        if size not in shell_dict[location]:
            shell_dict[location].append(size)
    command = input().split(" ")

for key, value in shell_dict.items():
    print(f"{key} -> ", end='')
    for i in range(len(value)):
        if i == len(value) - 1:
            print(f"{value[i]} ", end='')
            print(f"({ceil(sum(value) - (sum(value)/len(value)))})")
        else:
            print(f"{value[i]}, ", end='')
