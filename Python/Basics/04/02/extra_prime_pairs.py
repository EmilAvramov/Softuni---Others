start_1 = int(input())
start_2 = int(input())
difference_1 = int(input())
difference_2 = int(input())

is_prime = bool

for a in range(start_1, start_1 + difference_1 + 1):
    for b in range(start_2, start_2 + difference_2 + 1):
        if a % 2 != 0 and b % 2 != 0:
            for a_prime in range(3, int(a**0.5) + 1, 2):
                if a % a_prime != 0:
                    is_prime = True
                else:
                    is_prime = False
                    break
            if is_prime:
                for b_prime in range(3, int(b**0.5) + 1, 2):
                    if b % b_prime != 0:
                        is_prime = True
                    else:
                        is_prime = False
                        break
                if is_prime:
                    print(str(a) + str(b))
                    is_prime = False
            else:
                break
