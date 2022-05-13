numbers = [int(i) for i in str(input()).split(', ')]
min_wealth = int(input())

temp_diff = 0
equality_check = 0

for number in numbers:
    if number < min_wealth:
        temp_diff = min_wealth - number
        numbers[numbers.index(number)] += temp_diff
        numbers[numbers.index(max(numbers))] -= temp_diff

for number in numbers:
    if number >= min_wealth:
        equality_check += 1

if equality_check == len(numbers):
    print(numbers)
else:
    print(f'No equal distribution possible')

