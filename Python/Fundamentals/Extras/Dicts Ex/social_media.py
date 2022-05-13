data = input()

media_dict = {}

while data != "drop the media":
    action = data.split()[0]
    name = data.split()[1]
    if action == "post":
        media_dict[name] = [0, 0, {}]
    elif action == "like":
        media_dict[name][0] += 1
    elif action == "dislike":
        media_dict[name][1] += 1
    elif action == "comment":
        media_dict[name][2].update(
            {data.split()[2]: ' '.join(data.split()[3:])})
    data = input()

for key, value in media_dict.items():
    print(f"Post: {key} | Likes: {value[0]} | Dislikes: {value[1]}")
    print(f"Comments:")
    if len(value[2]) > 0:
        for sub_key, sub_value in value[2].items():
            print(f"*  {sub_key}: {sub_value}")
    else:
        print(f"None")
