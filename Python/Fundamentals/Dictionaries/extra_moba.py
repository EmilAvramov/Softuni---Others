def split(_input):
    if "->" in _input:
        operator.append("->")
        return _input.split(" -> ")
    elif "vs" in _input:
        operator.append("vs")
        return _input.split(" vs ")
    else:
        return _input


player_dict = {}
operator = []
removal_flag = False

command = split(input())

while command != "Season end":
    if "->" in operator:
        player = command[0]
        position = command[1]
        skill = int(command[2])
        if player not in player_dict:
            player_dict[player] = {position: skill}
        else:
            if position not in player_dict[player]:
                player_dict[player][position] = skill
            else:
                if skill > player_dict[player][position]:
                    player_dict[player][position] = skill
    else:
        player_1 = command[0]
        player_2 = command[1]
        if player_1 in player_dict and player_2 in player_dict:
            for key, value in player_dict.items():
                for sub_key, sub_value in value.items():
                    if sub_key in player_dict[player_1] and sub_key in player_dict[player_2]:
                        if sum(value for value in player_dict[player_1].values()) > \
                                sum(value for value in player_dict[player_2].values()):
                            player_dict.pop(player_2)
                            removal_flag = True
                            break
                        elif sum(value for value in player_dict[player_1].values()) < \
                                sum(value for value in player_dict[player_2].values()):
                            player_dict.pop(player_1)
                            removal_flag = True
                            break
                        else:
                            pass  # Tie
                if removal_flag:
                    break
    operator.clear()
    removal_flag = False
    command = split(input())

for key, value in (sorted(sorted(player_dict.items(), key=lambda x: x[0]), key=lambda x: -sum(x[1].values()))):
    print(f'{key}: {sum(value.values())} skill')
    for sub_key, sub_value in (sorted(sorted(value.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)):
        print(f'- {sub_key} <::> {sub_value}')
