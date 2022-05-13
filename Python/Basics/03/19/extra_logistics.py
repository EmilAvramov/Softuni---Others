num_shipments = int(input())

minibus_price = 200
truck_price = 175
train_price = 120
minibus_total_weight = 0
truck_total_weight = 0
train_total_weight = 0
total_price = 0
total_weight = 0

for i in range(1, num_shipments+1):
    weight = int(input())
    total_weight += weight
    if weight <= 3:
        total_price += weight * minibus_price
        minibus_total_weight += weight
    elif 4 <= weight <= 11:
        total_price += weight * truck_price
        truck_total_weight += weight
    else:
        total_price += weight * train_price
        train_total_weight += weight

print(f'{(total_price / total_weight):.2f}', end='\n')
print(f'{((minibus_total_weight / total_weight) * 100):.2f}%', end='\n')
print(f'{((truck_total_weight / total_weight) * 100):.2f}%', end='\n')
print(f'{((train_total_weight / total_weight) * 100):.2f}%')