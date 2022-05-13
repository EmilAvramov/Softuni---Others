fuel_type = str(input())
fuel_amt = float(input())

if fuel_type == "Diesel":
    set_fuel = "diesel"
elif fuel_type == "Gasoline":
    set_fuel = "gasoline"
elif fuel_type == "Gas":
    set_fuel = "gas"
else:
    set_fuel = "Invalid fuel!"

if fuel_amt >= 25 and set_fuel != "Invalid fuel!":
    print(f'You have enough {set_fuel}.')
elif fuel_amt < 25 and set_fuel != "Invalid fuel!":
    print(f'Fill your tank with {set_fuel}!')
else:
    print(f'Invalid fuel!')
