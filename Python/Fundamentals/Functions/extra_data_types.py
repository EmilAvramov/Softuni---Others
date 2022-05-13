operation = str(input())
data_input = input()


def transform_data(first, second):
    if first == "int":
        argument = int(second)
        output = f'{argument * 2}'
    elif first == "real":
        argument = float(second)
        output = f'{argument * 1.5:.2f}'
    else:
        output = f'${second}$'
    return output


print(transform_data(operation, data_input))
