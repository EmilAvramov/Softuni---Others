number = int(input())


def perfect_number():
    aliquot_sum = 0
    for check in range(1, number):
        if (number/check).is_integer():
            aliquot_sum += check
    return "We have a perfect number!" if aliquot_sum == number else "It's not so perfect."


print(perfect_number())
