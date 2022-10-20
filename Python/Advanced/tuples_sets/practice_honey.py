from collections import deque


def run_calculation(bee, nectar, symbol):
    if symbol == "+":
        return bee + nectar
    elif symbol == "-":
        return abs(bee - nectar)
    elif symbol == "*":
        return bee * nectar
    else:
        return bee / nectar


bees = deque([int(i) for i in input().split(" ")])
nectars = deque([int(i) for i in input().split(" ")])
symbols = deque([i for i in input().split(" ")])

total_honey = 0

while True:
    bee = bees[0]
    nectar = nectars[-1]
    symbol = symbols[0]
    if nectar >= bee:
        total_honey += run_calculation(bee, nectar, symbol)
        bees.popleft()
        nectars.pop()
        symbols.popleft()
    else:
        nectars.pop()
    if len(nectars) == 0 or len(bees) == 0:
        break

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")
