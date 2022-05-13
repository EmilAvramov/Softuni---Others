string = str(input())

string_list = string.split(' ')
string_list = [int(i) * -1 for i in string_list]

print(string_list)
