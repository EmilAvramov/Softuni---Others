name = str(input())

score_total = 0
year = 1
fail = 0

while year <= 12 and fail != 2:
    score = float(input())
    if score >= 4:
        year += 1
        score_total += score
    else:
        fail += 1

if fail == 2:
    print(f'{name} has been excluded at {year} grade')
else:
    print(f'{name} graduated. Average grade: {(score_total / 12):.2f}')
