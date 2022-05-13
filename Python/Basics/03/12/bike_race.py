juniors = int(input())
seniors = int(input())
track_type = str(input())

junior_cost = ""
senior_cost = ""

if track_type == "trail":
    junior_cost = 5.5
    senior_cost = 7
elif track_type == "cross-country":
    junior_cost = 8
    senior_cost = 9.5
    if juniors + seniors >= 50:
        junior_cost = junior_cost * 0.75
        senior_cost = senior_cost * 0.75
elif track_type == "downhill":
    junior_cost = 12.25
    senior_cost = 13.75
else:
    junior_cost = 20
    senior_cost = 21.5

total_profit = ((juniors * junior_cost) + (seniors * senior_cost)) * 0.95
print(f'{total_profit:.2f}')
