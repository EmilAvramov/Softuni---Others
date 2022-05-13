season = str(input())
km_month = float(input())

tariff_km = ""
mid_earnings = ""
final_earnings = ""

if km_month <= 5000:
    if season == "Spring" or season == "Autumn":
        tariff_km = 0.75
    elif season == "Summer":
        tariff_km = 0.9
    else:
        tariff_km = 1.05
elif 5000 < km_month <= 10000:
    if season == "Spring" or season == "Autumn":
        tariff_km = 0.95
    elif season == "Summer":
        tariff_km = 1.1
    else:
        tariff_km = 1.25
else:
    tariff_km = 1.45

mid_earnings = km_month * tariff_km * 4
final_earnings = mid_earnings * 0.9
print(f'{final_earnings:.2f}')