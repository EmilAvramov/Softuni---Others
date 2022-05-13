chrysanthemums_num = int(input())
roses_num = int(input())
tulips_num = int(input())
season = str(input())
holiday = str(input())

chrysanthemums_price = ""
roses_price = ""
tulips_price = ""
wrapping = 2
total_price = ""
final_price = ""

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15

if holiday == "y" or holiday == "Y":
    chrysanthemums_price = chrysanthemums_price * 1.15
    roses_price = roses_price * 1.15
    tulips_price = tulips_price * 1.15

total_price = chrysanthemums_price * chrysanthemums_num + roses_price * roses_num \
    + tulips_price * tulips_num

if season == "Spring" and tulips_num > 7:
    total_price = total_price * 0.95
    if (chrysanthemums_num + roses_num + tulips_num) > 20:
        total_price = total_price * 0.8
elif season == "Winter" and roses_num >= 10:
    total_price = total_price * 0.9
    if (chrysanthemums_num + roses_num + tulips_num) > 20:
        total_price = total_price * 0.8
elif (season != "Spring" or season != "Winter") and (chrysanthemums_num + roses_num + tulips_num) > 20:
    total_price = total_price * 0.8

final_price = total_price + wrapping

print(f'{final_price:.2f}')
