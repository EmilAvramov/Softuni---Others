string = input()
data = input()

while data != "end":
    command = data.split()[0]
    if command == "Left" or command == "Right" or command == "Insert":
        idx = int(data.split()[1])
        if command == "Left":
            idx = idx % len(string)
            string = string[idx:] + string[:idx]
        elif command == "Right":
            idx = idx % len(string)
            string = string[-idx:] + string[:-idx]
        elif command == "Insert":
            symbol = data.split()[2]
            string = string[:idx] + symbol + string[idx:]
    else:  # Delete
        start = int(data.split()[1])
        end = int(data.split()[2])
        string = string[:start] + string[end + 1:]
    data = input()

print(string)
