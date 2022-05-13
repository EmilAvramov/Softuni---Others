rows = int(input())

opened = 0
closed = 0
no_nested = True

for i in range(1, rows + 1):
    symbol = str(input())
    if symbol == "(":
        opened += 1
        if opened > closed + 1:
            no_nested = False
            break
    elif symbol == ")":
        closed += 1

if opened == closed and no_nested is True:
    print(f'BALANCED')
else:
    print(f'UNBALANCED')
