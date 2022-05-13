command = str(input())

while command != "end":
    original_string = command
    reversed_string = original_string[::-1]
    print(f'{original_string} = {reversed_string}')
    command = str(input())

