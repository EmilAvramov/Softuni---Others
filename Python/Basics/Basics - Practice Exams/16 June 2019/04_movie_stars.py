budget = float(input())
name = str(input())

cost = 0

while name != "ACTION":
    if len(name) > 15:
        salary = (budget - cost) * 0.2
    else:
        salary = float(input())
    cost += salary
    if cost >= budget:
        break
    name = str(input())

if budget >= cost:
    print(f'We are left with {abs(budget - cost):.2f} leva.')
else:
    print(f'We need {abs(cost - budget):.2f} leva for our actors.')