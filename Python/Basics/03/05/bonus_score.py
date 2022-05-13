score = float(input())
if score <= 100:
    bonus_points_sub = 5
elif 100 < score < 1000:
    bonus_points_sub = score * 0.2
elif score > 1000:
    bonus_points_sub = score * 0.1
if score % 2 == 0:
    bonus_points_total = bonus_points_sub + 1
elif score % 5 == 0:
    bonus_points_total = bonus_points_sub + 2
else:
    bonus_points_total = bonus_points_sub
total_points = score + bonus_points_total
print(bonus_points_total, end='\n')
print(total_points)