budget = float(input())
season = str(input())
num_people = int(input())
boat_price = ""
discount_num_boat = ""
final_boat_price = ""

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if num_people <= 6:
    discount_num_boat = boat_price * 0.9
elif 7 <= num_people <= 11:
    discount_num_boat = boat_price * 0.85
elif num_people >= 12:
    discount_num_boat = boat_price * 0.75

if num_people % 2 == 0 and season != "Autumn":
    final_boat_price = discount_num_boat * 0.95
else:
    final_boat_price = discount_num_boat

difference = abs(final_boat_price - budget)

if budget >= final_boat_price:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')