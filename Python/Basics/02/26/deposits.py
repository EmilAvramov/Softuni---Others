deposit_sum = float(input())
deposit_time = int(input())
interest_rate = float(input())
sum = deposit_sum + (deposit_time*((deposit_sum * (interest_rate /100)) / 12))
print(f'{sum:.2f}')

