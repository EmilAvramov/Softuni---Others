inheritance = float(input())
year = int(input())

age = 18
sum_spent = 0
year_diff = year - 1800

for i in range(0, year_diff + 1):
    if i % 2 == 0:
        sum_spent += 12000
    else:
        sum_spent += 12000 + (i + 18) * 50

difference = abs(inheritance - sum_spent)

if inheritance >= sum_spent:
    print(f'Yes! He will live a carefree life and will have {difference:.2f} dollars left.')
else:
    print(F'He will need {difference:.2f} dollars to survive.')

