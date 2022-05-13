num_people = int(input())
season = input()

below_five = {'spring': 50, 'summer': 48.5, 'autumn': 60, 'winter': 86}
above_five = {'spring': 48, 'summer': 45, 'autumn': 49.5, 'winter': 85}

total_price = 0

if num_people <= 5:
    for key, value in below_five.items():
        if season in key:
            if season == "summer":
                total_price = (value * num_people) * 0.85
            elif season == "winter":
                total_price = (value * num_people) * 1.08
            else:
                total_price = value * num_people
else:
    for key, value in above_five.items():
        if season in key:
            if season == "summer":
                total_price = (value * num_people) * 0.85
            elif season == "winter":
                total_price = (value * num_people) * 1.08
            else:
                total_price = value * num_people

print(f'{total_price:.2f} leva.')