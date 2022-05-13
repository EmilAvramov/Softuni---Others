number = float(input())

stop_flag = False

while stop_flag is False:
    if 1 <= number <= 100:
        stop_flag = True
        break
    number = float(input())

print(f'The number {number} is between 1 and 100')