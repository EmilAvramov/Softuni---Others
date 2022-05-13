import math

num_magnolia = int(input())
num_hyacinth = int(input())
num_rose = int(input())
num_cactus = int(input())
present = float(input())

price_magnolia = num_magnolia * 3.25
price_hyacinth = num_hyacinth * 4
price_rose = num_rose * 3.5
price_cactus = num_cactus * 8
total_order = (price_magnolia + price_hyacinth + price_rose + price_cactus) * 0.95
difference = abs(total_order - present)

if total_order >= present:
    print(f'She is left with {math.floor(difference):.0f} leva.')
else:
    print(f'She will have to borrow {math.ceil(difference):.0f} leva.')
