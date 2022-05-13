budget = float(input())
num_serials = int(input())

total_price = 0

for n in range(1, num_serials + 1):
    name = str(input())
    if name == "Thrones":
        price = float(input()) * 0.5
    elif name == "Lucifer":
        price = float(input()) * 0.6
    elif name == "Protector":
        price = float(input()) * 0.7
    elif name == "TotalDrama":
        price = float(input()) * 0.8
    elif name == "Area":
        price = float(input()) * 0.9
    else:
        price = float(input())
    total_price += price

if budget >= total_price:
    print(f'You bought all the series and left with {abs(budget - total_price):.2f} lv.')
else:
    print(f'You need {abs(total_price - budget):.2f} lv. more to buy the series!')