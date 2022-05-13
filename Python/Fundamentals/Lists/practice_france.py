items = str(input()).replace('->', '|').split('|')
budget = float(input())

nested_items = [items[i:i+2] for i in range(0, len(items), 2)]
for item in nested_items:
    item.append('0')

sold = 0
sold_list = []
leftover = budget

for item in nested_items:
    if leftover >= float(item[1]):
        if (item[0] == "Clothes" and float(item[1]) <= 50.00 and int(item[2]) == 0) or \
                (item[0] == "Shoes" and float(item[1]) <= 35.00 and int(item[2]) == 0) or \
                (item[0] == "Accessories" and float(item[1]) <= 20.50 and int(item[2]) == 0):
            sold += float(item[1]) * 1.4
            leftover -= float(item[1])
            item[2] = '1'
            sold_list.append(float(item[1]) * 1.4)

for i in range(len(sold_list)):
    print(f'{float(sold_list[i]):.2f}', end=' ')
print()
print(f'Profit: {sold - budget + leftover:.2f}')
if sold + leftover >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
