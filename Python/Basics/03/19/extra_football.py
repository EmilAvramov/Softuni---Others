st_capacity = float(input())
fans = int(input())

team_A = 0
team_B = 0
sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0

for i in range(1, fans+1):
    sector = str(input())
    if sector == "A":
        team_A += 1
        sector_A += 1
    elif sector == "B":
        team_A += 1
        sector_B += 1
    elif sector == "V":
        team_B += 1
        sector_V += 1
    else:
        team_B += 1
        sector_G += 1

print(f'{(sector_A / fans) * 100:.2f}%', end='\n')
print(f'{(sector_B / fans) * 100:.2f}%', end='\n')
print(f'{(sector_V / fans) * 100:.2f}%', end='\n')
print(f'{(sector_G / fans) * 100:.2f}%', end='\n')
print(f'{((team_A + team_B) / st_capacity) * 100:.2f}%')