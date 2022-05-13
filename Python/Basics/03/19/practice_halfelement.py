import sys

sequence = int(input())

sum_num = 0
highest = -sys.maxsize

for i in range(1, sequence + 1):
    num = float(input())
    sum_num += num
    if num > highest:
        highest = num

if sum_num - highest == highest:
    print(f'Yes', end='\n')
    print(f'Sum = {highest:.0f}')
else:
    print(f'No', end='\n')
    print(f'Diff = {abs(highest - (sum_num - highest)):.0f}')