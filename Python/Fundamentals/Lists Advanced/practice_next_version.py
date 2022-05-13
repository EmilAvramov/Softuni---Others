version = [int(i) for i in str(input()).split('.')]

if version[2] == 9:
    if version[1] == 9:
        version[0] += 1
        version[1] = 0
        version[2] = 0
    else:
        version[1] += 1
        version[2] = 0
elif version[1] == 9 and version[0] == 9:
    version[0] += 1
    version[1] = 0
    version[2] = 0
else:
    version[2] += 1

print(*version, sep='.')
