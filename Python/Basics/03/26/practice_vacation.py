money_needed = float(input())
money_available = float(input())

spend_count = 0
day_count = 0

while spend_count < 5 or money_available != money_needed:
    day_count += 1
    trans_type = str(input())
    if trans_type == "spend":
        spend_count += 1
        if spend_count == 5:
            print(f"You can't save the money.", end='\n')
            print(f"{day_count}")
            break
    else:
        spend_count = 0
    trans_amount = float(input())
    if trans_type == "spend":
        money_available -= trans_amount
        if money_available < 0:
            money_available = 0
    else:
        money_available += trans_amount
        if money_available >= money_needed:
            print(f'You saved the money for {day_count} days.')
            break
