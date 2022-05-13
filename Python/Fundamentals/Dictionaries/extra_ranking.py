cmd = input().split(":")

contest_info = {}  # {contest: password}
entries = {}  # {username: [contest, points]}
winner = ""
max_points = 0


while cmd[0] != "end of contests":
    contest = cmd[0]
    password = cmd[1]
    contest_info[contest] = password
    cmd = input().split(":")

cmd.clear()
cmd = input().split("=>")


while cmd[0] != "end of submissions":
    contest = cmd[0]
    password = cmd[1]
    username = cmd[2]
    points = int(cmd[3])
    if contest in contest_info and password == contest_info[contest]:
        if username in entries:
            if contest in entries[username]:
                if points > entries[username][contest]:
                    entries[username][contest] = points
            else:
                entries[username][contest] = points
        else:
            # if user does not exist, create as dict of dicts
            entries[username] = {contest: points}
    cmd = input().split("=>")

# sort main and sub dicts
entries = {k: (entries[k]) for k in sorted(entries)}
for key, value in entries.items():
    entries[key] = {sk: sv for sk, sv in sorted(value.items(), key=lambda x: x[1], reverse=True)}

# check highest points
for key, value in entries.items():
    current_points = 0
    for sub_key, sub_value in value.items():
        current_points += sub_value
    if current_points >= max_points:
        max_points = current_points
        winner = key

# print
print(f'Best candidate is {winner} with total {max_points} points.')
print(f'Ranking:')
for key, value in entries.items():
    print(f'{key}')
    for sub_key, sub_value in value.items():
        print(f'#  {sub_key} -> {sub_value}')
