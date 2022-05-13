dwarf_dict = {}
dwarf_colors = {}

command = input()

while command != "Once upon a time":
    command = command.split(" <:> ")
    name = command[0]
    color = command[1]
    physics = int(command[2])
    dwarf_id = name + ":" + color
    if dwarf_id not in dwarf_dict:
        dwarf_dict[dwarf_id] = [physics, color]
        if color not in dwarf_colors:
            dwarf_colors[color] = 1
        else:
            dwarf_colors[color] += 1
    else:
        if dwarf_dict[dwarf_id][0] < physics:
            dwarf_dict[dwarf_id][0] = physics
    command = input()

for key, value in sorted(dwarf_dict.items(), key=lambda x: (x[1][0], dwarf_colors[x[1][1]]), reverse=True):
    f_name = key.split(":")
    print(f'({value[1]}) {f_name[0]} <-> {value[0]}')
