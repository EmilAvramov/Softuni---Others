letters = input()
letter_dict = {}

for i in letters:
    letter_dict[i] = letters.count(i)

for key, value in letter_dict.items():
    print(f'{key} -> {value}')