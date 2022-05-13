import math

needed_hours = float(input())
total_days = float(input())
overtime_workers = int(input())

regular_hours = total_days * 8 * 0.9
overtime_hours = total_days * 2 * overtime_workers
total_hours = math.floor(regular_hours + overtime_hours)
difference = abs(total_hours - needed_hours)

if needed_hours <= total_hours:
    print(f'Yes!{difference:.0f} hours left.')
else:
    print(f'Not enough time!{difference:.0f} hours needed.')