data = [int(i) for i in input().split(" ")]
cmd = input()
count = 0

while cmd != "End":
    index = int(cmd)
    if index < len(data) and index >= 0:
        count += 1
        shot = data[index]
        data[index] = -1
        for i in range(len(data)):
            if data[i] != -1:
                if data[i] > shot:
                    data[i] -= shot
                else:
                    data[i] += shot
    cmd = input()

print(f"Shot targets: {count} -> {' '.join([str(i) for i in data])}")
