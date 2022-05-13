number = float(input())
sum_numbers = 0

while sum_numbers < number:
    extra_number = float(input())
    sum_numbers += extra_number

print(f'{sum_numbers:.0f}')
