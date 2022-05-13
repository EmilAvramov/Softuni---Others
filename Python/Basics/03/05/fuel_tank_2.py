fuel_type = str(input())
fuel_qty = float(input())
club_card = str(input())

if fuel_type == "Gasoline":
    fuel_price = 2.22
elif fuel_type == "Diesel":
    fuel_price = 2.33
elif fuel_type == "Gas":
    fuel_price = 0.93

if club_card == "Yes" and fuel_type == "Gasoline":
    fuel_price = 2.22 - 0.18
elif club_card == "Yes" and fuel_type == "Diesel":
    fuel_price = 2.33 - 0.12
elif club_card == "Yes" and fuel_type == "Gas":
    fuel_price = 0.93 - 0.08

if 20 <= fuel_qty <= 25:
    total_price = fuel_price * fuel_qty * 0.92
elif fuel_qty > 25:
    total_price = fuel_price * fuel_qty * 0.9
else:
    total_price = fuel_price * fuel_qty

print(f'{total_price:.2f} lv.')

