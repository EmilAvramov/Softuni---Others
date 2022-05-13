budget = float(input())
ticket_type = str(input())
num_people = int(input())

ticket_price = ""
transport_cost = ""

if ticket_type == "VIP":
    ticket_price = 499.99
elif ticket_type == "Normal":
    ticket_price = 249.99

if 1 <= num_people <= 4:
    transport_cost = budget * 0.75
elif 5 <= num_people <= 9:
    transport_cost = budget * 0.6
elif 10 <= num_people <= 24:
    transport_cost = budget * 0.5
elif 25 <= num_people <= 49:
    transport_cost = budget * 0.4
else:
    transport_cost = budget * 0.25

difference = abs(budget - transport_cost - (num_people * ticket_price))

if budget >= transport_cost + (num_people * ticket_price):
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')
