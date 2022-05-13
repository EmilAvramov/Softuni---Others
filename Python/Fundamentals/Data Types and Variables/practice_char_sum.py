rows = int(input())

total_sum = 0

for i in range(1, rows + 1):
    char = str(input())
    total_sum += ord(char)
print(f'The sum equals: {total_sum}')