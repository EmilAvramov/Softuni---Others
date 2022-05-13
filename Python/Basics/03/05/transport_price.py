kilometers = float(input())
day_night = str(input())

taxi_initial = 0.7
bus_total = kilometers * 0.09
train_total = kilometers * 0.06

if day_night == "day":
    taxi_km = 0.79
else:
    taxi_km = 0.9

taxi_total = taxi_km * kilometers + taxi_initial

if kilometers < 20:
    print(f'{taxi_total:.2f}')
elif 20 <= kilometers < 100:
    print(f'{bus_total:.2f}')
elif kilometers >= 100:
    print(f'{train_total:.2f}')