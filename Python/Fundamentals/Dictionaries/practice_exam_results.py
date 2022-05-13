cmd = input().split("-")

result_dict = {}  # {user-[language, points]}
count_dict = {}  # {language-count}

while cmd[0] != "exam finished":
    if cmd[1] == "banned":
        result_dict.pop(cmd[0])
    else:
        user = cmd[0]
        language = cmd[1]
        points = int(cmd[2])
        if user not in result_dict:
            result_dict[user] = [language, points]
        else:
            if language in result_dict[user]:
                if result_dict[user][1] < points:
                    result_dict[user] = [language, points]
            else:
                result_dict[user] += [language, points]
        if language in count_dict:
            count_dict[language] += 1
        else:
            count_dict[language] = 1
    cmd = input().split("-")

print("Results:")
for key, value in result_dict.items():
    print(f"{key} | {value[1]}")
print("Submissions:")
for key, value in count_dict.items():
    print(f"{key} - {value}")
