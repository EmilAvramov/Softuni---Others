guests = {}


def read_guestlist(file_name):
    text_file = open(file_name, "r")
    value = None
    while True:
        if value is None:
            line_data = text_file.readline().strip().split(",")
        else:
            line_data = value.strip().split(",")
        if len(line_data) < 2:
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        value = yield name, age


guests_gen = read_guestlist("guest_list.txt")
for i in range(10):
    next(guests_gen)
guests_gen.send("Jane, 35")
for i in range(4):
    next(guests_gen)
guests_over_21 = ({key: value} for key, value in guests.items() if value > 21)
print(*guests)
for guest in guests_over_21:
    print(guest)
