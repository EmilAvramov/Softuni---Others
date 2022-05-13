import sys

stop_flag = False
best_player = ["placeholder", -sys.maxsize]

while stop_flag is False:
    name = input()
    if name == "END":
        stop_flag = True
        break
    goals = int(input())
    if goals > best_player[1]:
        best_player.clear()
        best_player.append(name)
        best_player.append(goals)
    if best_player[1] >= 10:
        stop_flag = True
        break

print(f'{best_player[0]} is the best player!')
if best_player[1] >= 3:
    print(f'He has scored {best_player[1]} goals and made a hat-trick !!!')
elif best_player[1] < 3:
    print(f'He has scored {best_player[1]} goals.')


