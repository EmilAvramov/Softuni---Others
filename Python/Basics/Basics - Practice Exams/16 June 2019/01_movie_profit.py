name = str(input())
num_days = int(input())
num_tickets = int(input())
ticket_price = float(input())
profit_take = int(input())

profit = num_days * num_tickets * ticket_price - (num_days * num_tickets * ticket_price) * (profit_take * 0.01)
print(f'The profit from the movie {name} is {profit:.2f} lv.')