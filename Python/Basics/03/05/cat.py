holidays = float(input())
working_days = 365 - holidays
sum_playtime = working_days * 63 + holidays * 127
quota = 30000
difference = abs(quota - sum_playtime)
difference_hours = difference // 60
difference_minutes = difference % 60

if sum_playtime > quota:
    print("Tom will run away", end='\n')
    print(f'{difference_hours:.0f} hours and {difference_minutes:.0f} minutes more for play')
else:
    print("Tom sleeps well", end='\n')
    print(f'{difference_hours:.0f} hours and {difference_minutes:.0f} minutes less for play')
