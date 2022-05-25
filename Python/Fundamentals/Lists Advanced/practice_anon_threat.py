from textwrap import wrap

data = input()
save_data = data.split()
data = input()

while data != "3:1":
    command = data.split()[0]
    if command == "merge":
        start = int(data.split()[1])
        end = int(data.split()[2])
        if start < 0:
            start = 0
        if end >= len(save_data):
            end = len(save_data) - 1
        new_data = ["".join(save_data[start : end + 1])]
        save_data = save_data[0:start] + new_data + save_data[end + 1 :]
    elif command == "divide":
        index = int(data.split()[1])
        partitions = int(data.split()[2])
        target = save_data.pop(index)
        parts = 0
        parts = len(target) // partitions
        new_data = wrap(target, int(parts))
        if len(target) % partitions != 0:
            last_element = new_data.pop(-1)
            new_data[-1] += last_element
        for idx, elem in enumerate(new_data):
            save_data.insert(index + idx, elem)
    data = input()

print(*save_data, sep=" ")
