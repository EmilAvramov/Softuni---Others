password = str(input())


def validity_checker(argument):
    symbol_counter = 0
    length_counter = 0
    digit_counter = 0
    error_msg = ""
    for element in argument:
        if element.isdigit():
            digit_counter += 1
        if element.isalnum():
            symbol_counter += 1
        length_counter += 1
    if symbol_counter == len(argument) and digit_counter >= 2 and 6 <= length_counter <= 10:
        return "Password is valid"
    else:
        if length_counter < 6 or length_counter > 10:
            error_msg = "Password must be between 6 and 10 characters\n"
        if symbol_counter != len(argument):
            error_msg = error_msg + "Password must consist only of letters and digits\n"
        if digit_counter < 2:
            error_msg = error_msg + "Password must have at least 2 digits\n"
        return error_msg


print(validity_checker(password))
