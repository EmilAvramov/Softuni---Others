number = int(input())
symbol = "*"

for upper in range(1, number + 1):
    print(upper * symbol)
for lower in range(number - 1, 0, -1):
    print(lower * symbol)