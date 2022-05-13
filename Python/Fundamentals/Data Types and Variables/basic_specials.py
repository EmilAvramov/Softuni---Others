number = int(input())

sum_digits = 0

for num in range(1, number + 1):
    for index, value in enumerate(str(num)):
        sum_digits += int(value)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
    sum_digits = 0
