data = input()

data_list = []
length = 0

while data != "end":
    set_char = data.split(":")[0]
    set_indices = [int(i) for i in data.split(":")[1].split("/")]
    data_list.append([set_char, set_indices])
    data = input()

for elem in data_list:
    for symbol in elem[1]:
        if symbol > length:
            length = symbol

full_string = (length + 1) * ["*"]

for elem in data_list:
    for i in range(len(elem[1])):
        full_string[elem[1][i]] = elem[0]

print(*full_string, sep='')
