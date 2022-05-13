number = int(input())

for first in range(1, number + 1):
    for second in range(1, number + 1):
        for third in range(1, number + 1):
            print(chr(first + 96) + chr(second + 96) + chr(third + 96))
