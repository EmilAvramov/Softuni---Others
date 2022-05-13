century = int(input())

year = int(century * 100)
days = int(year * 365.2422)
hours = int(days * 24)
minutes = int(hours * 60)

print(f'{century} centuries = {year} years = {days} days = {hours} hours = {minutes} minutes')