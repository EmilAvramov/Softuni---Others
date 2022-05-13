numbers = [int(i) for i in str(input()).split()]


def filter_function(number):
    return True if number % 2 == 0 else False


even_numbers = list(filter(filter_function, numbers))
print(even_numbers)
