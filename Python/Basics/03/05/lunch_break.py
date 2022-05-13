import math
movie_name = str(input())
ep_duration = float(input())
break_duration = float(input())

lunch_duration = break_duration * 0.125
relax_duration = break_duration * 0.25
remaining_break = break_duration - lunch_duration - relax_duration
leftover_time_pos = abs(math.ceil(remaining_break - ep_duration))
leftover_time_neg = abs(math.ceil(ep_duration - remaining_break))

if remaining_break >= ep_duration:
    print(f"You have enough time to watch {movie_name} and left with {leftover_time_pos:.0f} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {leftover_time_neg:.0f} more minutes.")
