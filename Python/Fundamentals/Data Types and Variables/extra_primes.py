number = int(input())

prime_flag = False

if number > 1:
    for i in range(2, number // 2):
        if number % i == 0:
            prime_flag = False
            break
        else:
            prime_flag = True

if prime_flag:
    print("True")
else:
    print("False")
