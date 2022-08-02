import re

string = input()
pattern = r"(#|\|)([a-zA-Z\s]+)(#|\|)(\d{2}\/\d{2}\/\d{2})(#|\|)(\d+)(#|\|)"
calories = 0
cal_per_day = 2000

matches = re.findall(pattern, string)
for match in matches:
    calories += int(match[5])

print(f"You have food to last you for: {int(calories/cal_per_day)} days!")
for match in matches:
    print(f"Item: {match[1]}, Best before: {match[3]}, Nutrition: {match[5]}")
