string = [value for index, value in enumerate(str(input()))]

result_string = []

digit_list = [int(i) for i in string if i.isdigit()]
letter_list = [i for i in string if not i.isdigit()]
take_list = [digit_list[i] for i in range(len(digit_list)) if i % 2 == 0]
skip_list = [digit_list[i] for i in range(len(digit_list)) if i % 2 != 0]

for i in range(len(digit_list)):
    if i % 2 == 0:
        result_string.append(letter_list[:take_list[0]])
        letter_list = letter_list[take_list[0]:]
        take_list.pop(0)
    if i % 2 != 0:
        letter_list = letter_list[skip_list[0]:]
        skip_list.pop(0)

result_string = [i for sub in result_string for i in sub]

print(*result_string, sep='')
