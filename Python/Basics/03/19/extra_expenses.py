months = int(input())

total_bill = 0
total_el_bill = 0
total_water_bill = 0
total_inet_bill = 0
total_others_bill = 0

for i in range(1, months+1):
    el_bill = float(input())
    water_bill = 20
    inet_bill = 15
    others = (el_bill + water_bill + inet_bill) * 1.2
    total_el_bill += el_bill
    total_water_bill += water_bill
    total_inet_bill += inet_bill
    total_others_bill += others
    total_bill += el_bill + water_bill + inet_bill + others

print(f'Electricity: {total_el_bill:.2f} lv', end='\n')
print(f'Water: {total_water_bill:.2f} lv', end='\n')
print(f'Internet: {total_inet_bill:.2f} lv', end='\n')
print(f'Other: {total_others_bill:.2f} lv', end='\n')
print(f'Average: {total_bill / months:.2f} lv')
