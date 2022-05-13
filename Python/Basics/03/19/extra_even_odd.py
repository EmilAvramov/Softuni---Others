import sys

num_count = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, num_count + 1):
    num_ind = float(input())
    if i % 2 != 0:
        odd_sum += num_ind
        if num_ind < odd_min:
            odd_min = num_ind
        if num_ind > odd_max:
            odd_max = num_ind
    else:
        even_sum += num_ind
        if num_ind < even_min:
            even_min = num_ind
        if num_ind > even_max:
            even_max = num_ind

print(f'OddSum={odd_sum:.2f},', end='\n')
if odd_min == sys.maxsize:
    print(f'OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},', end='\n')
if odd_max == -sys.maxsize:
    print(f'OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},', end='\n')
print(f'EvenSum={even_sum:.2f},', end='\n')
if even_min == sys.maxsize:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},', end='\n')
if even_max == -sys.maxsize:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')
