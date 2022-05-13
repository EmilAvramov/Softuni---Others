letter_1 = str(input())
letter_2 = str(input())
letter_3 = str(input())
number_1 = ord(letter_1) - 96
number_2 = ord(letter_2) - 96
number_3 = ord(letter_3) - 96
counter = 0

for x in range(number_1, number_2 + 1):
    if x != number_3:
        for y in range(number_1, number_2 + 1):
            if y != number_3:
                for z in range(number_1, number_2 + 1):
                    if z != number_3:
                        print(f'{chr(x + 96)}{chr(y + 96)}{chr(z + 96)}', end=' ')
                        counter += 1
print(counter)

