number_str = str(input())

prime_sum = 0
non_prime_sum = 0
not_prime = False

while number_str != "stop":
    number_int = int(number_str)
    if number_int < 0:
        print("Number is negative.", end='\n')
    elif number_int > 1:
        for i in range(2, number_int):
            if number_int % i == 0:
                not_prime = True
                break
        if not_prime is True:
            non_prime_sum += number_int
            not_prime = False
        else:
            prime_sum += number_int
    number_str = str(input())

print(f'Sum of all prime numbers is: {prime_sum}', end='\n')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
