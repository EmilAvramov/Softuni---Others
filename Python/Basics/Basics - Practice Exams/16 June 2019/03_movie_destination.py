budget = float(input())
destination = str(input())
season = str(input())
days = int(input())

price = 0
total_cost = 0

if season == "Winter":
    if destination == "Dubai":
        price = 45000 * 0.7
    elif destination == "Sofia":
        price = 17000 * 1.25
    else:
        price = 24000
else:
    if destination == "Dubai":
        price = 40000 * 0.7
    elif destination == "Sofia":
        price = 12500 * 1.25
    else:
        price = 20250

total_cost = days * price

if budget >= total_cost:
    print(f'The budget for the movie is enough! We have {abs(budget - total_cost):.2f} leva left!')
else:
    print(f'The director needs {abs(total_cost - budget):.2f} leva more!')