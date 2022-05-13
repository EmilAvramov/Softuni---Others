string = str(input()).split()

temp = ""
count = 0
new_list = []

for element in string:
    for index, value in enumerate(element):
        if value.isdigit():
            temp += value
            count += 1
        if index == len(element) - 1:
            temp = chr(int(temp))
            element = temp + element[count:]
            new_list.append(element)
            temp = ""
            count = 0

new_list = [element[0] + element[-1] + element[2:-1] + element[1]
            if len(element) > 2
            else element
            for element in new_list]

print(*new_list, sep=' ')




