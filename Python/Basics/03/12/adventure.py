budget = float(input())
season = str(input())
vacation_type = ""
destination = ""
spent_cash = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        vacation_type = "Camp"
        spent_cash = budget * 0.3
    elif season == "winter":
        vacation_type = "Hotel"
        spent_cash = budget * 0.7
elif 101 <= budget <= 1000:
    if season == "summer":
        vacation_type = "Camp"
        spent_cash = budget * 0.4
    elif season == "winter":
        vacation_type = "Hotel"
        spent_cash = budget * 0.8
    destination = "Balkans"
elif budget > 1000:
    destination = "Europe"
    vacation_type = "Hotel"
    spent_cash = budget * 0.9

print(f'Somewhere in {destination}', end='\n')
print(f'{vacation_type} - {spent_cash:.2f}')