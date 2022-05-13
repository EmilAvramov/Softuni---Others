days = int(input())
hours = int(input())

mid_sum = 0
sum_total = 0

for index_day in range(1, days + 1):
    for index_hour in range(1, hours + 1):
        if index_day % 2 == 0 and index_hour % 2 != 0:
            sum_total += 2.5
            mid_sum += 2.5
        elif index_day % 2 != 0 and index_hour % 2 == 0:
            sum_total += 1.25
            mid_sum += 1.25
        else:
            sum_total += 1
            mid_sum += 1
    print(f'Day: {index_day} - {mid_sum:.2f} leva')
    mid_sum = 0

print(f'Total: {sum_total:.2f} leva')
