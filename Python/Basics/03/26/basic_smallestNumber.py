import sys

str_number = input()
smallest = sys.maxsize

while str_number != "Stop":
    int_number = int(str_number)
    if int_number < smallest:
        smallest = int_number
    str_number = input()

print(smallest)