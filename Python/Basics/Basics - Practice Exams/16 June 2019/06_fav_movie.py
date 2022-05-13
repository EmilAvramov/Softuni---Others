import sys

name = str(input())

num_movies = 0
total_points = 0
max_score = -sys.maxsize
max_score_name = ""

while name != "STOP" and num_movies != 7:
    for index, value in enumerate(name):
        for letter in range(0, index + 1):
            if 65 <= ord(value) <= 90:
                total_points += ord(value) - len(name)
                break
            elif 97 <= ord(value) <= 122:
                total_points += ord(value) - len(name) * 2
                break
            else:
                total_points += ord(value)
                break
    num_movies += 1
    if num_movies == 7:
        break
    if total_points > max_score:
        max_score = total_points
        max_score_name = name
    total_points = 0
    name = str(input())

if num_movies == 7:
    print(f'The limit is reached.')
    print(f'The best movie for you is {max_score_name} with {max_score} ASCII sum.')
else:
    print(f'The best movie for you is {max_score_name} with {max_score} ASCII sum.')