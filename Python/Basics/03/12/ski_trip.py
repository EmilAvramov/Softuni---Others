days = int(input())
room_choice = str(input())
grade = str(input())

room_price = ""
mid_cost = ""
total_cost = ""
nights = days - 1

if room_choice == "room for one person":
    room_price = 18
elif room_choice == "apartment":
    room_price = 25
    if days < 10:
        room_price = room_price * 0.7
    elif 10 <= days <= 15:
        room_price = room_price * 0.65
    elif days > 15:
        room_price = room_price * 0.5
elif room_choice == "president apartment":
    room_price = 35
    if days < 10:
        room_price = room_price * 0.9
    elif 10 <= days <= 15:
        room_price = room_price * 0.85
    elif days > 15:
        room_price = room_price * 0.8

mid_cost = room_price * nights

if grade == "positive":
    total_cost = mid_cost * 1.25
elif grade == "negative":
    total_cost = mid_cost * 0.9

print(f'{total_cost:.2f}')
