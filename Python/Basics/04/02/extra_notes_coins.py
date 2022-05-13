num_1 = int(input())
num_2 = int(input())
num_5 = int(input())
total_sum = int(input())

match_one = 0
match_two = 0
match_five = 0
checksum = 0

for ones in range(0, num_1 + 1):
    checksum = total_sum
    match_one = ones
    checksum -= match_one
    if checksum == 0:
        print(f'{match_one} * 1 lv. + {match_two} * 2 lv. + {match_five} * 5 lv. = {total_sum} lv.')
        match_one = 0
        break
    elif checksum != 0 and checksum > 0:
        for twos in range(0, num_2 + 1):
            checksum = total_sum
            match_two = twos
            checksum -= match_two * 2 + match_one
            if checksum == 0:
                print(f'{match_one} * 1 lv. + {match_two} * 2 lv. + {match_five} * 5 lv. = {total_sum} lv.')
                match_two = 0
                break
            elif checksum != 0 and checksum > 0:
                for fives in range(0, num_5 + 1):
                    checksum = total_sum
                    match_five = fives
                    checksum -= match_five * 5 + match_two * 2 + match_one
                    if checksum == 0:
                        print(f'{match_one} * 1 lv. + {match_two} * 2 lv. + {match_five} * 5 lv. = {total_sum} lv.')
                        match_five = 0
                        break
                    match_five = 0


