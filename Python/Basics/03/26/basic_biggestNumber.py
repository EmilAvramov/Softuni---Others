import sys

str_number = input()
biggest = -sys.maxsize

while str_number != "Stop":
    int_number = int(str_number)
    if int_number > biggest:
        biggest = int_number
    str_number = input()

print(biggest)