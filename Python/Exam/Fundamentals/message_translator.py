import re

pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

count = int(input())

for i in range(count):
    string = input()
    match = re.findall(pattern, string)
    if match:
        command = match[0][0]
        text = [ord(i) for i in match[0][1]]
        print(f"{command}: {' '.join([str(i) for i in text])}")
    else:
        print("The message is invalid")
