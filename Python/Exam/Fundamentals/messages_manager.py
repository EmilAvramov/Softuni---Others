capacity = int(input())

data = input()
user_dict = {}

while data != "Statistics":
    if "Add" in data:
        username = data.split("=")[1]
        sent = int(data.split("=")[2])
        received = int(data.split("=")[3])
        if username not in user_dict.keys():
            user_dict[username] = [sent, received]
    elif "Message" in data:
        sender = data.split("=")[1]
        receiver = data.split("=")[2]
        if sender in user_dict.keys() and receiver in user_dict.keys():
            user_dict[sender][0] += 1
            user_dict[receiver][1] += 1
            if user_dict[sender][0] + user_dict[sender][1] >= capacity:
                print(f"{sender} reached the capacity!")
                del user_dict[sender]
            if user_dict[receiver][0] + user_dict[receiver][1] >= capacity:
                print(f"{receiver} reached the capacity!")
                del user_dict[receiver]
    elif "Empty" in data:
        username = data.split("=")[1]
        if username in user_dict.keys():
            del user_dict[username]
        elif username == "All":
            user_dict = {}
    data = input()

print(f"Users count: {len(user_dict)}")
for [user, stats] in user_dict.items():
    print(f"{user} - {stats[0] + stats[1]}")
