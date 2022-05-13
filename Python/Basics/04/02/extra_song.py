number = int(input())

counter = 0
password = 0
pwd_flag = False

for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            for c in range(1, 10):
                for d in range(1, 10):
                    if c > d:
                        if number == (a * b) + (c * d):
                            counter += 1
                            print(f'{a}{b}{c}{d}', end=' ')
                            if counter == 4:
                                password = str(a) + str(b) + str(c) + str(d)
                                if counter == 4:
                                    pwd_flag = True
                                    counter += 1
if pwd_flag:
    print()
    print(f'Password: {password}')
else:
    if counter != 0:
        print()
        print("No!")
    else:
        print("No!")