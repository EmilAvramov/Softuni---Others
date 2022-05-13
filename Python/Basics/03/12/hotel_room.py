month = str(input())
num_nights = int(input())

studio = ""
apartment = ""
studio_cost = ""
apartment_cost = ""

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    studio_cost = studio * num_nights
    apartment_cost = apartment * num_nights
    if 7 < num_nights <= 14:
        studio_cost = studio_cost * 0.95
    if num_nights > 14:
        studio_cost = studio_cost * 0.7
        apartment_cost = apartment_cost * 0.9
elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
    studio_cost = studio * num_nights
    apartment_cost = apartment * num_nights
    if num_nights > 14:
        studio_cost = studio_cost * 0.8
        apartment_cost = apartment_cost * 0.9
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    studio_cost = studio * num_nights
    apartment_cost = apartment * num_nights
    if num_nights > 14:
        apartment_cost = apartment_cost * 0.9

print(f'Apartment: {apartment_cost:.2f} lv.', end='\n')
print(f'Studio: {studio_cost:.2f} lv.')
