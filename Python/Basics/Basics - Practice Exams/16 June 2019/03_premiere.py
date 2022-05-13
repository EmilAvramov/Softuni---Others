name = str(input())
food = str(input())
num_tickets = int(input())

price = 0

if name == "John Wick":
    if food == "Drink":
        price = 12
    elif food == "Popcorn":
        price = 15
    else:
        price = 19
elif name == "Star Wars":
    if num_tickets >= 4:
        if food == "Drink":
            price = 18 * 0.7
        elif food == "Popcorn":
            price = 25 * 0.7
        else:
            price = 30 * 0.7
    else:
        if food == "Drink":
            price = 18
        elif food == "Popcorn":
            price = 25
        else:
            price = 30
else:
    if num_tickets == 2:
        if food == "Drink":
            price = 9 * 0.85
        elif food == "Popcorn":
            price = 11 * 0.85
        else:
            price = 14 * 0.85
    else:
        if food == "Drink":
            price = 9
        elif food == "Popcorn":
            price = 11
        else:
            price = 14

print(f'Your bill is {num_tickets * price:.2f} leva.')