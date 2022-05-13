word = str(input())
insensitive = word.casefold()

string_list = ["Water", "Sun", "Fish", "Sand"]
string_chars = [i.casefold() for i in string_list]

counter = 0
match = ""

for i in range(len(string_chars)):
    match = string_chars[i]
    counter += insensitive.count(match)

print(counter)
