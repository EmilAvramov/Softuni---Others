actor_name = str(input())
initial_points = float(input())
num_grades = int(input())

total_points = initial_points

for i in range(1, num_grades + 1):
    grader_name = str(input())
    points = (float(input()) * len(grader_name)) / 2
    total_points += points
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {abs(1250.5 - total_points):.1f} more!')
