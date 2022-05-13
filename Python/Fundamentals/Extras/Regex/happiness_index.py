import re

re_happy = r"\:\)|\:D|;\)|\:\*|\:\]|;\]|\:\}|;\}|\(\:|\*\:|c\:|\[\:|\[;"
re_sad = r"\:\(|D\:|;\(|\:\[|;\[|\:\{|;\{|\)\:|\:c|\]\:|\];"

string = input()

happy = re.findall(re_happy, string)
sad = re.findall(re_sad, string)

h_index = len(happy)/len(sad)

if h_index >= 2:
    print(f"Happiness index: {h_index:.2f} :D")
    print(f"[Happy count: {len(happy)}, Sad count: {len(sad)}]")
elif 1 < h_index < 2:
    print(f"Happiness index: {h_index:.2f} :)")
    print(f"[Happy count: {len(happy)}, Sad count: {len(sad)}]")
elif h_index == 1:
    print(f"Happiness index: {h_index:.2f} :|")
    print(f"[Happy count: {len(happy)}, Sad count: {len(sad)}]")
else:
    print(f"Happiness index: {h_index:.2f} :(")
    print(f"[Happy count: {len(happy)}, Sad count: {len(sad)}]")