number = int(input())

sequence = 1
stop_point = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        print(sequence, end=" ")
        sequence += 1
        if sequence == number + 1:
            stop_point = True
            break
    if stop_point:
        break
    print()



