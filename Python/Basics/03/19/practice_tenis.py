import math

num_tour = int(input())
points_init = float(input())

won_points = 0
times_winner = 0

for i in range(1, num_tour + 1):
    rank = str(input())
    if rank == "W":
        won_points += 2000
        times_winner += 1
    elif rank == "F":
        won_points += 1200
    else:
        won_points += 720

print(f'Final points: {math.floor(won_points + points_init):.0f}', end='\n')
print(f'Average points: {math.floor(won_points / num_tour):.0f}', end='\n')
print(f'{(times_winner / num_tour) * 100:.2f}%')