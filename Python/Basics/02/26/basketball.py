annual_fee = int(input())
shoes_fee = float(annual_fee * 0.6)
clothes_fee = float(shoes_fee * 0.8)
ball_fee = float(clothes_fee * 0.25)
accessories_fee = float(ball_fee * 0.2)
total_fee = annual_fee + shoes_fee + clothes_fee + ball_fee + accessories_fee
print(total_fee)