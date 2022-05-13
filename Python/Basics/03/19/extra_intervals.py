turns = int(input())

result = 0
i_1 = 0
i_2 = 0
i_3 = 0
i_4 = 0
i_5 = 0
i_6 = 0

for i in range(1, turns+1):
    number = float(input())
    if 0 <= number <= 9:
        i_1 += 1
        result += number * 0.2
    elif 10 <= number <= 19:
        i_2 += 1
        result += number * 0.3
    elif 20 <= number <= 29:
        i_3 += 1
        result += number * 0.4
    elif 30 <= number <= 39:
        i_4 += 1
        result += 50
    elif 40 <= number <= 50:
        i_5 += 1
        result += 100
    else:
        i_6 += 1
        result = result / 2

print(f'{result:.2f}', end='\n')
print(f'From 0 to 9: {(i_1 / turns) * 100:.2f}%', end='\n')
print(f'From 10 to 19: {(i_2 / turns) * 100:.2f}%', end='\n')
print(f'From 20 to 29: {(i_3 / turns) * 100:.2f}%', end='\n')
print(f'From 30 to 39: {(i_4 / turns) * 100:.2f}%', end='\n')
print(f'From 40 to 50: {(i_5 / turns) * 100:.2f}%', end='\n')
print(f'Invalid numbers: {(i_6 / turns) * 100:.2f}%')
