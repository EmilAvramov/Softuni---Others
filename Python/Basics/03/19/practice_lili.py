age = int(input())
washer_price = float(input())
toy_price = float(input())

toy_sum = 0
money_increase = 0
money_sum = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toy_sum += 1
    else:
        money_increase += 1
        money_sum += (10 * money_increase) - 1

total_sum = toy_sum * toy_price + money_sum

if total_sum >= washer_price:
    print(f'Yes! {abs(total_sum - washer_price):.2f}')
else:
    print(f'No! {abs(total_sum - washer_price):.2f}')
