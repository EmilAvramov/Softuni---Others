season = str(input())
group_type = str(input())
num_students = int(input())
num_nights = int(input())

price_night_total = ""
sport_type = ""

if season == "Winter" and group_type == "boys":
    price_night_total = 9.6 * num_nights * num_students
    sport_type = "Judo"
elif season == "Winter" and group_type == "girls":
    price_night_total = 9.6 * num_nights * num_students
    sport_type = "Gymnastics"
elif season == "Winter" and group_type == "mixed":
    price_night_total = 10 * num_nights * num_students
    sport_type = "Ski"
elif season == "Spring" and group_type == "boys":
    price_night_total = 7.2 * num_nights * num_students
    sport_type = "Tennis"
elif season == "Spring" and group_type == "girls":
    price_night_total = 7.2 * num_nights * num_students
    sport_type = "Athletics"
elif season == "Spring" and group_type == "mixed":
    price_night_total = 9.5 * num_nights * num_students
    sport_type = "Cycling"
elif season == "Summer" and group_type == "boys":
    price_night_total = 15 * num_nights * num_students
    sport_type = "Football"
elif season == "Summer" and group_type == "girls":
    price_night_total = 15 * num_nights * num_students
    sport_type = "Volleyball"
elif season == "Summer" and group_type == "mixed":
    price_night_total = 20 * num_nights * num_students
    sport_type = "Swimming"

if num_students >= 50:
    price_night_total = price_night_total * 0.5
elif 20 <= num_students < 50:
    price_night_total = price_night_total * 0.85
elif 10 <= num_students < 20:
    price_night_total = price_night_total * 0.95

print(f'{sport_type} {price_night_total:.2f} lv.')
