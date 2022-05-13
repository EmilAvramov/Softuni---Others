import math
time_first = float(input())
time_second = float(input())
time_third = float(input())
sum_time = time_first + time_second + time_third
minutes = sum_time / 60
minutes = math.floor(minutes)
seconds = sum_time % 60
if seconds < 10:
    print(f'{minutes:.0f}:0{seconds:.0f}')
else:
    print(f"{minutes:.0f}:{seconds:.0f}")
