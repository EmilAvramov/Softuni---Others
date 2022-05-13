operator = str(input())
int_1 = int(input())
int_2 = int(input())


def calculations(operation, number_1, number_2):
    if operation == "multiply":
        output = number_1 * number_2
    elif operation == "divide":
        output = number_1 / number_2
    elif operation == "add":
        output = number_1 + number_2
    else:
        output = number_1 - number_2
    return output


print(f'{calculations(operator, int_1, int_2):.0f}')
