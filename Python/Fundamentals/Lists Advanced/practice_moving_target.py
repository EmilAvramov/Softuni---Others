targets = [int(i) for i in str(input()).split()]
cmd = str(input()).split()

while cmd[0] != "End":
    if cmd[0] == "Shoot":
        if int(cmd[1]) in range(len(targets)):
            targets[int(cmd[1])] -= int(cmd[2])
            if targets[int(cmd[1])] <= 0:
                targets.pop(int(cmd[1]))
    elif cmd[0] == "Add":
        if int(cmd[1]) in range(len(targets)):
            targets.insert(int(cmd[1]), int(cmd[2]))
        else:
            print(f'Invalid placement!')
    elif cmd[0] == "Strike":
        before = int(cmd[1]) - int(cmd[2])
        after = int(cmd[1]) + int(cmd[2])
        if int(cmd[1]) in range(len(targets)):
            if before in range(len(targets)) and after in range(len(targets)):
                targets = targets[:before] + targets[after + 1:]
            else:
                print(f"Strike missed!")
    cmd = str(input()).split()

print(*targets, sep='|')
