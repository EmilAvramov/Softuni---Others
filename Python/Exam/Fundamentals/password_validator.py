import re


def validate_password(password: str, pattern):
    upper_flag = False
    lower_flag = False
    digit_flag = False
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
        return
    match = re.findall(pattern, password)
    if match is False:
        print("Password must consist only of letters, digits and _!")
    for letter in password:
        if letter.isupper():
            upper_flag = True
        if letter.islower():
            lower_flag = True
        if letter.isdigit():
            digit_flag = True
    if upper_flag is False:
        print("Password must consist at least one uppercase letter!")
    if lower_flag is False:
        print("Password must consist at least one lowercase letter!")
    if digit_flag is False:
        print("Password must consist at least one digit!")


re_pattern = r"([A-Za-z_]{8,})"

password = input()

command = input()

while command != "Complete":
    if "Make Upper" in command:
        index = int(command.split(" ")[2])
        password = (
            password[:index] + password[index].upper() + password[index + 1 :]
        )
        print(password)
    elif "Make Lower" in command:
        index = int(command.split(" ")[2])
        password = (
            password[:index] + password[index].lower() + password[index + 1 :]
        )
        print(password)
    elif "Insert" in command:
        index = int(command.split(" ")[1])
        char = command.split(" ")[2]
        if index > 0 and index <= len(password) - 1:
            password = password[:index] + char + password[index:]
            print(password)
    elif "Replace" in command:
        char = command.split(" ")[1]
        value = int(command.split(" ")[2])
        new_symbol = chr(ord(char) + value)
        if char in password:
            while char in password:
                password = password.replace(char, new_symbol)
            print(password)
    elif command == "Validation":
        validate_password(password, re_pattern)

    command = input()
