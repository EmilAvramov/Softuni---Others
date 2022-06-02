data = input()
break_flag = False

while data != "Welcome!":
    if data == "Voldemort":
        print("You must not speak of that name!")
        break_flag = True
        break
    if len(data) < 5:
        print(f"{data} goes to Gryffindor.")
    elif len(data) == 5:
        print(f"{data} goes to Slytherin.")
    elif len(data) == 6:
        print(f"{data} goes to Ravenclaw.")
    else:
        print(f"{data} goes to Hufflepuff.")

    data = input()

if break_flag is False:
    print("Welcome to Hogwarts.")
