number = int(input())
sum_left = 0
sum_right = 0
str_number = ""

for int_number in range(1111, 10000):
    str_number = str(int_number)
    sum_left = int(str_number[0]) + int(str_number[1])
    sum_right = int(str_number[2]) + int(str_number[3])
    if int(str_number[0]) != 0 and int(str_number[1]) != 0 and int(str_number[2]) != 0 and int(str_number[3]) != 0:
        if sum_left == sum_right and number % sum_left == 0:
            print(int_number, end=' ')






