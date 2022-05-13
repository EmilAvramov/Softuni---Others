card = str(input())
card_list = card.split(' ')

team_A = []
team_B = []

for i in range(1, 12):
    team_A.append("A-" + str(i))
    team_B.append("B-" + str(i))

for i in range(len(card_list)):
    if len(team_A) < 7 or len(team_B) < 7:
        break
    if card_list[i] in team_A:
        team_A.remove(card_list[i])
    elif card_list[i] in team_B:
        team_B.remove(card_list[i])

if len(team_A) >= 7 and len(team_B) >= 7:
    print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')
else:
    print(f'Team A - {len(team_A)}; Team B - {len(team_B)}', end='\n')
    print(f'Game was terminated')
