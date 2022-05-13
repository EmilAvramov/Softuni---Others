rows = int(input())

number_list_pos = []
number_list_neg = []

for i in range(1, rows + 1):
    number = int(input())
    if number >= 0:
        number_list_pos.append(number)
    else:
        number_list_neg.append(number)

print(number_list_pos, end='\n')
print(number_list_neg, end='\n')
print(f'Count of positives: {len(number_list_pos)}', end='\n')
print(f'Sum of negatives: {sum(number_list_neg)}')
