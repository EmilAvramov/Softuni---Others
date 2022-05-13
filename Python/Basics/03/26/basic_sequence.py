number = float(input())
future_number = 0

while future_number <= number:
    future_number = future_number * 2 + 1
    if future_number > number:
        break
    print(future_number)