import math

name = str(input())
num_seasons = int(input())
num_episodes = int(input())
ep_without_ads = float(input())

ep_with_ads = ep_without_ads * 1.2
special_episode = ep_with_ads + 10
time_total = num_seasons * num_episodes * ep_with_ads + num_seasons * special_episode - num_seasons * ep_with_ads

print(f'Total time needed to watch the {name} series is {math.floor(time_total)} minutes.')
