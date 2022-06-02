data = input()


while data != "End":
    doubles = ""
    if data != "SoftUni":
        for letter in data:
            doubles += letter * 2
        print(doubles)
        doubles = ""
    data = input()
