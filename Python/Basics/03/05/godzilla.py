budget = float(input())
num_people = int(input())
clothing_per_price = float(input())

decor = budget * 0.1
if num_people > 150:
    final_clothing_price = clothing_per_price * num_people * 0.9
    budget_needed = final_clothing_price + decor
else:
    final_clothing_price = clothing_per_price * num_people
    budget_needed = final_clothing_price + decor

missing_funds = abs(budget - budget_needed)
exceed_funds = budget - budget_needed

if budget_needed > budget:
    print(f'Not enough money!', end="\n")
    print(f'Wingard needs {missing_funds:.2f} leva more.')
else:
    print(f'Action!', end='\n')
    print(f'Wingard starts filming with {exceed_funds:.2f} leva left.')
