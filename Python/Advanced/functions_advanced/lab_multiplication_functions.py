def multiply(*args):
    result = 1
    all_numbers = [int(i) for i in args]
    for number in all_numbers:
        result *= number
    return result
