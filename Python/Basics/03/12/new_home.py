type_flower = str(input())
num_flower = int(input())
budget = float(input())

price_flower = ""

if type_flower == "Roses":
    price_flower = 5
    if num_flower > 80:
        price_flower = 5 * 0.9
elif type_flower == "Dahlias":
    price_flower = 3.8
    if num_flower > 90:
        price_flower = 3.8 * 0.85
elif type_flower == "Tulips":
    price_flower = 2.8
    if num_flower > 80:
        price_flower = 2.8 * 0.85
elif type_flower == "Narcissus":
    price_flower = 3
    if num_flower < 120:
        price_flower = 3 * 1.15
elif type_flower == "Gladiolus":
    price_flower = 2.5
    if num_flower < 80:
        price_flower = 2.5 * 1.2

sum_needed = num_flower * price_flower
difference = abs(budget - sum_needed)

if budget >= sum_needed:
    print(f'Hey, you have a great garden with {num_flower:.0f} {type_flower} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')