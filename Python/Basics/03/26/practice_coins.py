import math

leftover = float(input())

coin_count = 0
cents = leftover * 100

while cents > 0:
    if cents >= 200:
        cents -= 200
        coin_count += 1
    if 200 > cents >= 100:
        cents -= 100
        coin_count += 1
    if 100 > cents >= 50:
        cents -= 50
        coin_count += 1
    if 50 > cents >= 20:
        cents -= 20
        coin_count += 1
    if 20 > cents >= 10:
        cents -= 10
        coin_count += 1
    if 10 > cents >= 5:
        cents -= 5
        coin_count += 1
    if 5 > cents >= 2:
        cents -= 2
        coin_count += 1
    if 2 > cents >= 1:
        cents -= 1
        coin_count += 1
    cents = math.floor(cents)

print(f'{coin_count:.0f}')

# Other method using list and //
# sequence = [200, 100, 50, 20, 10, 5, 2, 1]
#
# input_value = float(input())
#
# counter = 0
# number = 0
#
# result_value = int(input_value * 100)
#
# for i in range (0, 8):
#     number = result_value // sequence[i]
#     result_value -= number * sequence[i]
#     counter += number
#
# print(counter)