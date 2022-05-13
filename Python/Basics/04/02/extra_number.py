start = int(input())
end = int(input())
even_sum = 0

for license_number in range(1000, 10000):
    str_number = str(license_number)
    if start <= int(str_number[0]) <= end and start <= int(str_number[1]) <= end \
            and start <= int(str_number[2]) <= end and start <= int(str_number[3]) <= end:
        if (int(str_number[0]) % 2 == 0 and int(str_number[3]) % 2 != 0) or \
                (int(str_number[0]) % 2 != 0 and int(str_number[3]) % 2 == 0):
            if int(str_number[0]) > int(str_number[3]):
                even_sum = int(str_number[1]) + int(str_number[2])
                if even_sum % 2 == 0:
                    print(license_number, end=' ')

