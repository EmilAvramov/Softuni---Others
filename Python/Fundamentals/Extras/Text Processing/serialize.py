string = input()

uniques = ""
symbol_count = 0

for letter in string:
    if letter not in uniques:
        uniques += letter

for unique in uniques:
    print(f"{unique}:", end='')
    for index in range(len(string)):
        if string[index] == unique:
            symbol_count += 1
            if string.count(unique) != symbol_count:
                print(f"{index}/", end='')
            else:
                print(f"{index}", end='\n')
                symbol_count = 0
