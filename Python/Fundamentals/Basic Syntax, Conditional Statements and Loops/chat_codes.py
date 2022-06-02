count = int(input())

for x in range(count):
    data = int(input())
    if data == 88:
        print("Hello")
    elif data == 86:
        print("How are you?")
    elif data != 86 and data < 88:
        print("GREAT!")
    elif data > 88:
        print("Bye.")
