budget = float(input())
season = str(input())

location = ""
housing_type = ""
vacation_cost = ""

if budget <= 1000:
    housing_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        vacation_cost = budget * 0.65
    else:
        location = "Morocco"
        vacation_cost = budget * 0.45
elif 1000 < budget <= 3000:
    housing_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        vacation_cost = budget * 0.8
    else:
        location = "Morocco"
        vacation_cost = budget * 0.6
else:
    housing_type = "Hotel"
    vacation_cost = budget * 0.9
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f'{location} - {housing_type} - {vacation_cost:.2f}')