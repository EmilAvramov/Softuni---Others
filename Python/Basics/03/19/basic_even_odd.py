numbers = int(input())

sum_even = 0
sum_odd = 0

for i in range(0, numbers):
    uniques = int(input())
    if i % 2 == 0:
        sum_even += uniques
    else:
        sum_odd += uniques

difference = abs(sum_even - sum_odd)

if sum_even == sum_odd:
    print(f'Yes', end='\n')
    print(f'Sum = {sum_even}')
else:
    print(f'No', end='\n')
    print(f'Diff = {difference}')