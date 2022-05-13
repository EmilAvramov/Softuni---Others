name = str(input())

ticket_type = ""
student_ticket = 0
standard_ticket = 0
kid_ticket = 0
all_tickets = 0
free_seats = 0
taken_seats = 0

while name != "Finish":
    free_seats = int(input())
    while free_seats > taken_seats:
        ticket_type = str(input())
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1
        taken_seats += 1
        all_tickets += 1
    print(f'{name} - {(taken_seats / free_seats) * 100:.2f}% full.')
    taken_seats = 0
    name = str(input())

print(f'Total tickets: {all_tickets}', end='\n')
print(f'{(student_ticket / all_tickets) * 100:.2f}% student tickets.', end='\n')
print(f'{(standard_ticket / all_tickets) * 100:.2f}% standard tickets.', end='\n')
print(f'{(kid_ticket / all_tickets) * 100:.2f}% kids tickets.')
