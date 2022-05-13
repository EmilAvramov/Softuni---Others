number = int(input())
end = False

counter = 0

while end is False:
    for number_in_loop in range(1111, 10000):
        for index, digit in enumerate(str(number_in_loop)):
            for each_index in range(0, index + 1):
                if "0" in str(number_in_loop):
                    break
                else:
                    if number % int(digit) == 0:
                        counter += 1
                        break
                    else:
                        counter = 0
                        break
            if counter == 4:
                print(number_in_loop, end=' ')
                counter = 0
                break
    break