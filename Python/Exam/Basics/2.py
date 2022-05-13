shirt_price = float(input())
goal_points = float(input())

shorts = shirt_price * 0.75
socks = shorts * 0.2
socker_shoes = (shirt_price + shorts) * 2

points_total = (shirt_price + shorts + socks + socker_shoes) * 0.85

if points_total >= goal_points:
    print(f'Yes, he will earn the world-cup replica ball!', end='\n')
    print(f'His sum is {points_total:.2f} lv.')
else:
    print(f'No, he will not earn the world-cup replica ball.', end='\n')
    print(f'He needs {goal_points - points_total:.2f} lv. more.')
