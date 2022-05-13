def func_executor(*args):
    inbound_func = ""
    inbound_tuple = ()
    result = []
    for item in args:
        inbound_func = item[0]
        inbound_tuple = item[1]
        result.append(inbound_func(*inbound_tuple))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
