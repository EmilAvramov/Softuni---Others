data = input()

topic_dict = {}
search_count = 0

while data != "filter":
    topic = data.split(" -> ")[0]
    tags = [i for i in data.split(" -> ")[1].split(", ")]
    tags = ["#" + i for i in tags]
    if topic not in topic_dict.keys():
        topic_dict[topic] = tags
    else:
        for i in range(len(tags)):
            if tags[i] not in topic_dict[topic]:
                topic_dict[topic].append(tags[i])
    data = input()

search = input().split(", ")
search = ["#" + i for i in search]

for key, value in topic_dict.items():
    for item in search:
        if item in value:
            search_count += 1
    if search_count == len(search):
        print(f"{key} | ", end='')
        print(*value, sep=', ')
    search_count = 0
