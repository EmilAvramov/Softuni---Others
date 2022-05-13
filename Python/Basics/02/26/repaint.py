safety_mats_qty = int(input())
paint_qty = int(input())
paint_dilute_qty = int(input())
worker_hours = int(input())
safety_mats_price = float(1.5)
paint_price = float(14.5)
paint_dilute_price = float(5)
extra_mats_cost = (paint_qty * 0.1) * paint_price + safety_mats_price * 2 + 0.4
total_cost_no_fee = safety_mats_qty * safety_mats_price + paint_qty * paint_price + paint_dilute_qty * paint_dilute_price + extra_mats_cost
workers_fee = (total_cost_no_fee * 0.3) * worker_hours
total_cost = total_cost_no_fee + workers_fee
print(total_cost)



