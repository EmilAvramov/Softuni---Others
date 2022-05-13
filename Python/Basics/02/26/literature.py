num_pages = int(input())
num_per_hour = int(input())
num_days = int(input())
hours_needed_per_day = (num_pages / num_per_hour) / num_days
print(f'{hours_needed_per_day:.0f}')
