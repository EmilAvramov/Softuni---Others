hour = float(input())
weekday = str(input())

if 10 <= hour <= 18 and weekday != "Sunday":
    print("open")
else:
    print("closed")