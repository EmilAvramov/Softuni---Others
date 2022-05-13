command = input().split(" -> ")

user_dict = {}
contest_dict = {}
iteration = 0
total_points = {}

while command[0] != "no more time":
    username = command[0]
    contest = command[1]
    points = int(command[2])
    # handle contest_dict with key contest
    if contest not in contest_dict:
        contest_dict[contest] = {username: points}
    else:
        if username not in contest_dict[contest]:
            contest_dict[contest][username] = points
        else:
            if points > contest_dict[contest][username]:
                contest_dict[contest][username] = points
    # handle user_dict with key user
    if username not in user_dict:
        user_dict[username] = {contest: points}
    else:
        if contest not in user_dict[username]:
            user_dict[username][contest] = points
        else:
            if points > user_dict[username][contest]:
                user_dict[username][contest] = points
    command = input().split(" -> ")

# Handle total_point dict with key user and sum points
for key, value in user_dict.items():
    total_points[key] = sum(value.values())

# Sort contest dict
for key, value in contest_dict.items():
    contest_dict[key] = {sk: sv for sk, sv in sorted(sorted(value.items(), key=lambda x: x[0], reverse=False),
                                                     key=lambda x: x[1], reverse=True)}

for key, value in contest_dict.items():
    print(f'{key}: {len(value)} participants')
    for sk, sv in value.items():
        iteration += 1
        print(f'{iteration}. {sk} <::> {sv}')
    iteration = 0

print(f'Individual standings:')
for key, value in sorted(sorted(total_points.items(), key=lambda x: x[0], reverse=False),
                         key=lambda x: x[1], reverse=True):
    iteration += 1
    print(f'{iteration}. {key} -> {value}')
