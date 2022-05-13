num_orders = int(input())

price_capsule = 0
days = 0
count_capsule = 0
total_price = 0

for i in range(1, num_orders + 1):
    price_capsule = float(input())
    days = int(input())
    count_capsule = int(input())
    total_price += price_capsule * days * count_capsule
    print(f'The price for the coffee is: ${price_capsule * days * count_capsule:.2f}')
print(f'Total: ${total_price:.2f}')