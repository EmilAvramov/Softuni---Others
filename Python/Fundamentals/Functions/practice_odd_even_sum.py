number = int(input())


def breakdown_number():
    sum_even = 0
    sum_odd = 0
    for index, value in enumerate(str(number)):
        if int(value) % 2 == 0:
            sum_even += int(value)
        elif int(value) % 2 != 0:
            sum_odd += int(value)
    return sum_odd, sum_even


print(f'Odd sum = {breakdown_number()[0]}, Even sum = {breakdown_number()[1]}')
