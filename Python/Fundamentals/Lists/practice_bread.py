event_list = str(input()).replace('-', '|').split('|')

event_list = [event_list[i:i+2] for i in range(0, len(event_list), 2)]
event_list = [[int(value) if value.isdigit() else value for value in element] for element in event_list]
energy = 100
coins = 100
break_flag = False

for event in event_list:
    if event[0] == "rest":
        if energy + event[1] > 100:
            energy = 100
            print(f'You gained 0 energy.')
            print(f'Current energy: {energy}.')
        else:
            energy += event[1]
            print(f'You gained {event[1]} energy.')
            print(f'Current energy: {energy}.')
    elif event[0] == "order":
        if energy >= 30:
            coins += event[1]
            energy -= 30
            print(f'You earned {event[1]} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins >= event[1]:
            coins -= event[1]
            print(f'You bought {event[0]}.')
        else:
            print(f'Closed! Cannot afford {event[0]}.')
            break_flag = True
            break

if break_flag is False:
    print(f'Day completed!', end='\n')
    print(f'Coins: {coins}', end='\n')
    print(f'Energy: {energy}')


