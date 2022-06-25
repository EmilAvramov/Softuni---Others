data = [int(i) for i in input().split(" ")]
cmd = input()
start = False
end = False

# Need to redo third command

while cmd != "End":
    action = cmd.split(" ")[0]
    index = int(cmd.split(" ")[1])
    power = int(cmd.split(" ")[2])
    if action == "Shoot":
        if index >= 0 and index < len(data):
            data[index] -= power
            if data[index] <= 0:
                data.remove(data[index])
    elif action == "Add":
        if index >= 0 and index < len(data):
            data.insert(index, power)
        else:
            print("Invalid placement!")
    else:
        if index >= 0 and index < len(data):
            if len(data[:index]) < power:
                start = True
            if len(data[index:]) < power:
                end = True
            if start and end:
                data = data[:index]
        else:
            print("Strike missed!")
    cmd = input()

print(*data, sep="|")
