import math

time_shoots = int(input())
num_scenes = int(input())
num_per_scene = int(input())

time_needed = num_scenes * num_per_scene + time_shoots * 0.15

if time_shoots >= time_needed:
    print(f'You managed to finish the movie on time! You have {abs(time_needed - time_shoots):.0f} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {abs(time_needed - time_shoots):.0f} minutes.')