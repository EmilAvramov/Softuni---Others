budget = float(input())
season = str(input())

car_class = ""
car_type = ""
rent_cost = ""

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        rent_cost = budget * 0.35
    else:
        car_type = "Jeep"
        rent_cost = budget * 0.65
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        rent_cost = budget * 0.45
    else:
        car_type = "Jeep"
        rent_cost = budget * 0.8
else:
    car_class = "Luxury class"
    car_type = "Jeep"
    rent_cost = budget * 0.9

print(f'{car_class}', end='\n')
print(f'{car_type} - {rent_cost:.2f}')