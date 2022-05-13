number = int(input())
edge = "+ "
mid_row = "- "
mid_col = "| "

print(f'{edge}{(mid_row * (number - 2))}{edge}')
for x in range(1, number - 1):
    print(f'{mid_col}{mid_row * (number - 2)}{mid_col}')
print(f'{edge}{mid_row * (number - 2)}{edge}')
