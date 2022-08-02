import re


def filtered(x):
    if len(x) > 0:
        destinations.append(x)


pattern = r"=([A-Z][A-Za-z]{2,})=|/([A-Z][A-Za-z]{2,})/"

string = input()
travel_points = 0
destinations = []

matches = re.findall(pattern, string)

for match in matches:
    for item in match:
        filtered(item)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {sum([len(x) for x in destinations])}")
