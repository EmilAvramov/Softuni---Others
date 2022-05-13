import sys

count = int(input())

ball_value = 0
best_ball = -sys.maxsize
stored_weight = 0
stored_time = 0
stored_quality = 0

for i in range(1, count + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    ball_value = (weight / time) ** quality
    if ball_value > best_ball:
        best_ball = ball_value
        stored_weight = weight
        stored_time = time
        stored_quality = quality

print(f'{stored_weight} : {stored_time} = {best_ball:.0f} ({stored_quality})')