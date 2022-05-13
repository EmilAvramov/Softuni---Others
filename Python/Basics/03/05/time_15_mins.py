hours = float(input())
minutes = float(input())
if minutes + 15 >= 60:
    if hours >= 23:
        hours_total = hours - 23
    else:
        hours_total = hours + 1
    minutes_total = minutes - 45
elif minutes + 15 <= 60:
    hours_total = hours
    minutes_total = minutes + 15

if minutes_total < 10:
    print(f'{hours_total:.0f}:0{minutes_total:.0f}')
else:
    print(f'{hours_total:.0f}:{minutes_total:.0f}')
