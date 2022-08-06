string = input()

command = input()

while command != "Done":
    if "TakeOdd" in command:
        string = string[1::2]
        print(string)
    elif "Cut" in command:
        index = int(command.split(" ")[1])
        length = int(command.split(" ")[2])
        string = string[0:index] + string[index + length :]
        print(string)
    else:
        [cmd, substr, substitute] = command.split(" ")
        if substr in string:
            while substr in string:
                string = string.replace(substr, substitute)
            print(string)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {string}")
