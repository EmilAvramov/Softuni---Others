num_1 = float(input())
num_2 = float(input())
operator = str(input())
num_sum = ""
even_odd = ""
error_0 = ""

if operator == "+":
    num_sum = num_1 + num_2
    if num_sum % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
elif operator == "-":
    num_sum = num_1 - num_2
    if num_sum % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
elif operator == "*":
    num_sum = num_1 * num_2
    if num_sum % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
elif operator == "/":
    if num_2 == 0:
        error_0 = "Yes"
    else:
        error_0 = "No"
        num_sum = num_1 / num_2
elif operator == "%":
    if num_2 == 0:
        error_0 = "Yes"
    else:
        error_0 = "No"
        num_sum = num_1 % num_2

if operator == "+" or operator == "-" or operator == "*":
    print(f'{num_1:.0f} {operator} {num_2:.0f} = {num_sum:.0f} - {even_odd}')
elif operator == "/" and error_0 == "No":
    print(f'{num_1:.0f} / {num_2:.0f} = {num_sum:.2f}')
elif operator == "%" and error_0 == "No":
    print(f'{num_1:.0f} % {num_2:.0f} = {num_sum:.0f}')
elif (operator == "/" or operator == "%") and error_0 == "Yes":
    print(f'Cannot divide {num_1:.0f} by zero')