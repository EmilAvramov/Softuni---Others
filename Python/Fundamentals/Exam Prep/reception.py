emp_1 = int(input())
emp_2 = int(input())
emp_3 = int(input())
students = int(input())

eff = emp_1 + emp_2 + emp_3
hours = 0

while students > 0:
    students -= eff
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")
