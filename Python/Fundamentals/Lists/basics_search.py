rows = int(input())
word = str(input())

string_list = []

for i in range(1, rows + 1):
    string = str(input())
    string_list.append(string)
print(string_list)

for i in range(len(string_list) - 1, -1, -1):
    if word not in string_list[i]:
        string_list.remove(string_list[i])
print(string_list)
