str_steps = str(input())

goal = 10000
current_steps = 0

while current_steps < goal:
    if str_steps == "Going home":
        str_steps = int(input())
        if goal > current_steps + str_steps:
            current_steps += str_steps
            break
    int_steps = int(str_steps)
    current_steps += int_steps
    if current_steps >= goal:
        break
    str_steps = str(input())

if current_steps < goal:
    print(f'{abs(goal - current_steps):.0f} more steps to reach goal.')
elif current_steps == goal:
    print(f'Goal reached! Good job')
else:
    print(f'Goal reached! Good job!', end='\n')
    print(f'{abs(goal - current_steps):.0f} steps over the goal!')