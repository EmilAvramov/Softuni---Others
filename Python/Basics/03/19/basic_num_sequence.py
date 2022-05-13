import sys

num_numbers = int(input())
smallest = sys.maxsize
biggest = -sys.maxsize

for i in range(0, num_numbers):
    num_input = int(input())
    if num_input < smallest:
        smallest = num_input
    if num_input > biggest:
        biggest = num_input

print(f'Max number: {biggest}', end='\n')
print(f'Min number: {smallest}')
