lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_cost = 0
shield_broken = 0

for defeat_index in range(1, lost_fights + 1):
    if defeat_index % 2 == 0:
        total_cost += helmet_price
    if defeat_index % 3 == 0:
        total_cost += sword_price
    if defeat_index % 2 == 0 and defeat_index % 3 == 0:
        total_cost += shield_price
        shield_broken += 1
    if shield_broken == 2:
        total_cost += armor_price
        shield_broken = 0

print(f'Gladiator expenses: {total_cost:.2f} aureus')
