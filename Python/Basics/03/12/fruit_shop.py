fruit = str(input())
weekday = str(input())
qty = float(input())
price = 0

if weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday" or \
        weekday == "Friday":
    valid_day = "True"
    if fruit == "banana":
        price = 2.5
    elif fruit == "apple":
        price = 1.2
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.7
    elif fruit == "pineapple":
        price = 5.5
    elif fruit == "grapes":
        price = 3.85
    else:
        price = "invalid"
elif weekday == "Saturday" or weekday == "Sunday":
    valid_day = "True"
    if fruit == "banana":
        price = 2.7
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.6
    elif fruit == "kiwi":
        price = 3
    elif fruit == "pineapple":
        price = 5.6
    elif fruit == "grapes":
        price = 4.2
    else:
        price = "invalid"
else:
    valid_day = "False"

if price != "invalid" and valid_day == "True":
    print(f'{round(price * qty, 3):.2f}')
else:
    print("error")
