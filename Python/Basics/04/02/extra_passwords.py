a = int(input())
b = int(input())
max_passwords = int(input())

password_count = 0
break_point = False

for index_1_6 in range(35, 56):
    for index_2_5 in range(64, 96):
        for index_3 in range(1, a + 1):
            for index_4 in range(1, b + 1):
                if password_count == max_passwords:
                    break_point = True
                    break
                password_count += 1
                print(f'{chr(index_1_6)}{chr(index_2_5)}{index_3}{index_4}{chr(index_2_5)}{chr(index_1_6)}', end='|')
                if index_3 == a and index_4 == b:
                    break_point = True
                    break
                index_1_6 += 1
                index_2_5 += 1
                if index_1_6 > 55:
                    index_1_6 = 35
                if index_2_5 > 96:
                    index_2_5 = 64
            if break_point:
                break
        if break_point:
            break
    if break_point:
        break