ratings = [int(i) for i in input().split(", ")]
index = int(input())
cmd = input()

left_damage = 0
right_damage = 0
left = ratings[:index]
right = ratings[index + 1 :]

for i in range(len(left)):
    if cmd == "cheap":
        if left[i] < ratings[index]:
            left_damage += left[i]
    else:
        if left[i] >= ratings[index]:
            left_damage += left[i]

for i in range(len(right)):
    if cmd == "cheap":
        if right[i] < ratings[index]:
            right_damage += right[i]
    else:
        if right[i] >= ratings[index]:
            right_damage += right[i]

if left_damage >= right_damage:
    print(f"Left - {left_damage}")
else:
    print(f"Right - {right_damage}")
