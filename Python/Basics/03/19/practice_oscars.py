actor_name = str(input())
academy_points = float(input())
num_people_points = int(input())

total_points = academy_points

for i in range(1, num_people_points + 1):
    name = str(input())
    points_ind = float(input())
    total_points += (len(name) * points_ind) / 2
    if total_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break
if total_points <= 1250.5:
    print(f'Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!')

