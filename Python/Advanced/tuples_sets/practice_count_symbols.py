string = input()
string_dict = {}

for letter in string:
    if letter not in string_dict:
        string_dict[letter] = 1
    else:
        string_dict[letter] += 1

for key, value in sorted(string_dict.items()):
    print(f"{key}: {value} time/s")
