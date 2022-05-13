a = int(input())
b = int(input())

print(f'Before:', end='\n')
print(f'a = {a}', end='\n')
print(f'b = {b}')
a, b = b, a
print(f'After:', end='\n')
print(f'a = {a}', end='\n')
print(f'b = {b}')
