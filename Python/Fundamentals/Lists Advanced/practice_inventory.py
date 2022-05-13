items = str(input()).split(', ')
cmd = str(input()).split(' - ')

while cmd[0] != "Craft!":
    if cmd[0] == "Collect":
        if cmd[1] not in items:
            items.append(cmd[1])
    elif cmd[0] == "Drop":
        if cmd[1] in items:
            items.pop(items.index(cmd[1]))
    elif cmd[0] == "Combine Items":
        split = cmd[1].split(":")
        if split[0] in items:
            index = items.index(split[0])
            items.insert(index + 1, split[1])
        split.clear()
    elif cmd[0] == "Renew":
        if cmd[1] in items:
            items.append(items.pop(items.index(cmd[1])))
    cmd = str(input()).split(' - ')

print(*items, sep=', ')
