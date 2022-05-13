budget = float(input())
num_vc = int(input())
num_processor = int(input())
num_ram = int(input())

vc_price = float(250)
vc_total_price = vc_price * num_vc
processor_price = vc_total_price * 0.35
processor_total_price = processor_price * num_processor
ram_price = vc_total_price * 0.1
ram_total_price = ram_price * num_ram
total = vc_total_price + processor_total_price + ram_total_price

if num_vc > num_processor:
    grand_total = total * 0.85
else:
    grand_total = total

difference_pos = abs(grand_total - budget)
difference_neg = abs(budget - grand_total)

if grand_total <= budget:
    print(f'You have {difference_pos:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference_neg:.2f} leva more!')
