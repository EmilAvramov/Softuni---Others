stops = input()
initial = stops

cmd = input()

while cmd != "Travel":
    if "Add" in cmd or "Remove" in cmd:
        command = cmd.split(":")[0]
        if "Add" in command:
            index = int(cmd.split(":")[1])
            string = cmd.split(":")[2]
            if index >= 0 and index <= len(stops) - 1:
                stops = stops[:index] + string + stops[index:]
        elif "Remove" in command:
            start = int(cmd.split(":")[1])
            end = int(cmd.split(":")[2])
            if (
                (start >= 0 and start <= len(stops) - 1)
                and (end >= 0 and end <= len(stops) - 1)
                and (start <= end)
            ):
                stops = stops[:start] + stops[end + 1 :]
    else:
        [command, old, new] = cmd.split(":")
        if old in initial:
            stops = stops.replace(old, new)
    print(stops)
    cmd = input()

print(f"Ready for world tour! Planned stops: {stops}")
