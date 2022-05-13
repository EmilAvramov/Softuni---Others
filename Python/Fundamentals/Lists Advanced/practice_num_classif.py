string = [int(i) for i in str(input()).split(', ')]

# Method 1, list comprehension
# print(f'Positive: ', end='')
# print(*[i for i in string if i >= 0], sep=', ', end='\n')
# print(f'Negative: ', end='')
# print(*[i for i in string if i < 0], sep=', ', end='\n')
# print(f'Even: ', end='')
# print(*[i for i in string if i % 2 == 0], sep=', ', end='\n')
# print(f'Odd: ', end='')
# print(*[i for i in string if i % 2 != 0], sep=', ')

# Method 2, using filter and lambda
print(f'Positive: ', end='')
print(*list(filter(lambda x: x >= 0, string)), sep=', ', end='\n')
print(f'Negative: ', end='')
print(*list(filter(lambda x: x < 0, string)), sep=', ', end='\n')
print(f'Even: ', end='')
print(*list(filter(lambda x: x % 2 == 0, string)), sep=', ', end='\n')
print(f'Odd: ', end='')
print(*list(filter(lambda x: x % 2 != 0, string)), sep=', ')
