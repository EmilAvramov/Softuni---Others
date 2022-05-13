num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def multiplication(_num_1, _num_2, _num_3):
    list_numbers = [_num_1, _num_2, _num_3]
    pos_counter = 0
    neg_counter = 0
    zero_counter = 0
    for element in list_numbers:
        if element == 0:
            zero_counter += 1
        elif element > 0:
            pos_counter += 1
        else:
            neg_counter += 1
    if (pos_counter == 3 or pos_counter == 1) and zero_counter == 0:
        result = "positive"
    elif zero_counter != 0:
        result = "zero"
    else:
        result = "negative"
    return result


print(multiplication(num_1, num_2, num_3))
