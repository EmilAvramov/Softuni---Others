state = input()
fiction = input()

result = []

while state != "collapse":
    while len(fiction) != 0:
        if fiction in state:
            state = state.replace(fiction, "")
            fiction = fiction[1:-1]
        else:
            fiction = fiction[1:-1]
    if len(state) != 0:
        result.append(state)
    else:
        result.append("(void)")
    state = input()
    if state == "collapse":
        break
    fiction = input()

result = [i.strip() for i in result]

for string in result:
    print(string)
