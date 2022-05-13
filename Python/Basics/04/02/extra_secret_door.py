first_digit = int(input())
second_digit = int(input())
third_digit = int(input())

for match_first in range(1, first_digit + 1):
    if match_first % 2 == 0:
        for match_second in range(1, second_digit + 1):
            if match_second / 2 == 1 or match_second / 3 == 1 or match_second / 5 == 1 or match_second / 7 == 1:
                for match_third in range(1, third_digit + 1):
                    if match_third % 2 == 0:
                        print(f'{match_first} {match_second} {match_third}')

