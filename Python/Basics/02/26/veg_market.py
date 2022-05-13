fruit_price = float(input())
veg_price = float(input())
fruit_qty = float(input())
veg_qty = float(input())
fruit_price_eur = fruit_price / 1.94
veg_price_eur = veg_price / 1.94
total_profit = fruit_qty * fruit_price_eur + veg_qty * veg_price_eur
print(f'{total_profit:.2f}')