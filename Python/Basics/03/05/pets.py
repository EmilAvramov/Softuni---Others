import math

days = float(input())
food_total = float(input())
dog_per_day = float(input())
cat_per_day = float(input())
turtle_per_day = float(input()) / 1000

food_eaten = (dog_per_day + cat_per_day + turtle_per_day) * days
difference = abs(food_total - food_eaten)

if food_total >= food_eaten:
    print(f'{math.floor(difference):.0f} kilos of food left.')
else:
    print(f'{math.ceil(difference):.0f} more kilos of food are needed.')


