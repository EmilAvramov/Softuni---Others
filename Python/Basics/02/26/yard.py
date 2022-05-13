#Very Important to consider what the user will input!!!
sq_m_qty = float(input())
sq_m_price = float(7.61)
final_price = float(sq_m_qty * sq_m_price)
discounted_price = float(final_price * 0.82)
discount_qty = float(final_price - discounted_price)
print(f'The final price is {discounted_price} lv.', end='')
print(f'The discount is {discount_qty} lv.')

