men = int(input())
women = int(input())
seats = int(input())
sum_dates = 0
men_counter = men

while sum_dates < seats or men_counter == 0:
    for m in range(1, men + 1):
        if men_counter != 0:
            men_counter -= 1
            if sum_dates >= seats:
                break
            for w in range(1, women + 1):
                sum_dates += 1
                print(f'({m} <-> {w})', end=' ')
                if sum_dates >= seats:
                    break
    break



