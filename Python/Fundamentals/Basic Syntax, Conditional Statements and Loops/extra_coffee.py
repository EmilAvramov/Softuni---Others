event = str(input())

counter = 0
event_list_lower = ["coding", "cat", "dog", "movie"]
event_list_upper = [i.upper() for i in event_list_lower]

while event != "END":
    if event in event_list_lower:
        counter += 1
    elif event in event_list_upper:
        counter += 2
    event = str(input())

if counter > 5:
    print(f'You need extra sleep')
else:
    print(counter)
