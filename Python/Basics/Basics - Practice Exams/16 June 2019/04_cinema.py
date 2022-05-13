capacity = int(input())
people = str(input())

people_counter = 0
ticket_price = 5
income = 0

while people != "Movie time!":
    int_people = int(people)
    people_counter += int_people
    if people_counter > capacity:
        people_counter -= int_people
        break
    if int_people % 3 == 0:
        income += int_people * ticket_price - 5
    else:
        income += int_people * ticket_price
    people = str(input())

if people == "Movie time!":
    print(f'There are {abs(capacity - people_counter)} seats left in the cinema.', end='\n')
else:
    print(f'The cinema is full.')
print(f'Cinema income - {income} lv.')
