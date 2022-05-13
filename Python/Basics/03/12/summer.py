degrees = float(input())
time_day = str(input())
clothes = ""
shoes = ""

if time_day == "Morning":
    if 10 <= degrees <= 18:
        clothes = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif degrees >= 25:
        clothes = "T-Shirt"
        shoes = "Sandals"
elif time_day == "Afternoon":
    if 10 <= degrees <= 18:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        clothes = "T-Shirt"
        shoes = "Sandals"
    elif degrees >= 25:
        clothes = "Swim Suit"
        shoes = "Barefoot"
elif time_day == "Evening":
    if 10 <= degrees <= 18:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif degrees >= 25:
        clothes = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees:.0f} degrees, get your {clothes} and {shoes}.")
