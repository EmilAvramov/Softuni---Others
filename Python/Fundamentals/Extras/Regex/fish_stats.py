import re

data = input()

fish = r">*<\(+[\'\-x]>"
counter = 1

match = re.findall(fish, data)
if len(match) != 0:
    for fish in match:
        print(f"Fish {counter}: {fish}")
        tail = fish.count(">")
        body = fish.count("(")
        if tail == 1:
            print(f"  Tail type: None ")
        elif tail == 2:
            print(f"  Tail type: Short ({tail} cm)")
        elif 2 < tail <= 6:
            print(f"  Tail type: Medium ({tail * 2 - 2} cm)")
        else:
            print(f"  Tail type: Long ({tail * 2 - 2} cm)")
        if body > 10:
            print(f"  Body type: Long ({body * 2} cm)")
        elif 5 < body <= 10:
            print(f"  Body type: Medium ({body * 2} cm)")
        else:
            print(f"  Body type: Short ({body * 2} cm)")
        if "'" in fish:
            print(f"  Status: Awake")
        elif "-" in fish:
            print(f"  Status: Asleep")
        elif "x" in fish:
            print(f"  Status: Dead")
        counter += 1
else:
    print(f"No fish found.")
