import math


def factorials():
    number_1 = int(input())
    number_2 = int(input())

    # For Method 1 & 2
    # factorial_1 = number_1
    # factorial_2 = number_2

    # Method 1, standard factorial, naive
    # for i in range(number_1 - 1, 1, -1):
    #     factorial_1 *= i
    # for i in range(number_2 - 1, 1, -1):
    #     factorial_2 *= i

    # Method 2, simple factorial, naive
    # for i in range(1, number_1):
    #     factorial_1 *= i
    # for i in range(1, number_2):
    #     factorial_2 *= i

    # Method 3, math.factorial(), function
    return f'{math.factorial(number_1)/math.factorial(number_2):.2f}'


print(factorials())
