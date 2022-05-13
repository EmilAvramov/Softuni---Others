city = str(input())
qty_sold = float(input())
comm = 0
city_check = 0

if city == "Sofia":
    if 0 <= qty_sold <= 500:
        comm = qty_sold * 0.05
    elif 500 < qty_sold <= 1000:
        comm = qty_sold * 0.07
    elif 1000 < qty_sold <= 10000:
        comm = qty_sold * 0.08
    elif qty_sold > 10000:
        comm = qty_sold * 0.12
    else:
        comm = "invalid"
elif city == "Varna":
    if 0 <= qty_sold <= 500:
        comm = qty_sold * 0.045
    elif 500 < qty_sold <= 1000:
        comm = qty_sold * 0.075
    elif 1000 < qty_sold <= 10000:
        comm = qty_sold * 0.1
    elif qty_sold > 10000:
        comm = qty_sold * 0.13
    else:
        comm = "invalid"
elif city == "Plovdiv":
    if 0 <= qty_sold <= 500:
        comm = qty_sold * 0.055
    elif 500 < qty_sold <= 1000:
        comm = qty_sold * 0.08
    elif 1000 < qty_sold <= 10000:
        comm = qty_sold * 0.12
    elif qty_sold > 10000:
        comm = qty_sold * 0.145
    else:
        comm = "invalid"
else:
    city_check = "invalid"

if comm != "invalid" and city_check != "invalid":
    print(f'{comm:.2f}')
else:
    print("error")