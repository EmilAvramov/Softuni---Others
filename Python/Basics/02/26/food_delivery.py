chicken_qty = int(input())
fish_qty = int(input())
veg_menu_qty = int(input())
chicken_price = float(10.35)
fish_price = float(12.4)
veg_menu_price = float(8.15)
delivery_fee = float(2.5)
mid_bill = chicken_qty * chicken_price + fish_qty * fish_price + veg_menu_price * veg_menu_qty
desert_fee = mid_bill * 0.2
total_bill = mid_bill + desert_fee + delivery_fee
print(total_bill)