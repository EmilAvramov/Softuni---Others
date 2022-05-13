import math

total_sq_m = float(input())
grape_sq_m = float(input())
needed_wine = float(input())
workers = int(input())

wine_yard = total_sq_m * 0.4
grape_yield = wine_yard * grape_sq_m
wine_yield = grape_yield / 2.5
difference_wine = abs(needed_wine - wine_yield)
worker_wine = difference_wine / workers

if wine_yield < needed_wine:
    print(f'It will be a tough winter! More {math.floor(difference_wine):.0f} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(wine_yield):.0f} liters.', end='\n')
    print(f'{math.ceil(difference_wine):.0f} liters left -> {math.ceil(worker_wine):.0f} liters per person.')
