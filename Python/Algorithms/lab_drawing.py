def drawing(number):
    if number == 0:
        return

    print(number * "*")
    drawing(number - 1)
    print(number * "#")


number = int(input())

drawing(number)
