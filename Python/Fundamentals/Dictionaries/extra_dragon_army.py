dragons = int(input())

dragon_dict = {}

for dragon in range(dragons):
    stats = input().split()
    d_type = stats[0]
    d_name = stats[1]
    if stats[2] == "null":
        d_damage = 45
    else:
        d_damage = int(stats[2])
    if stats[3] == "null":
        d_health = 250
    else:
        d_health = int(stats[3])
    if stats[4] == "null":
        d_armor = 10
    else:
        d_armor = int(stats[4])
    if d_type not in dragon_dict:
        dragon_dict[d_type] = {d_name: [d_damage, d_health, d_armor]}
    else:
        dragon_dict[d_type][d_name] = [d_damage, d_health, d_armor]

for key, value in dragon_dict.items():
    print(f'{key}::'
          f'({round(sum([i[0] for i in value.values()])/len(value),2):.2f}/'
          f'{round(sum([i[1] for i in value.values()])/len(value),2):.2f}/'
          f'{round(sum([i[2] for i in value.values()])/len(value),2):.2f})')
    for sub_key, sub_value in sorted(value.items(), key=lambda x: x[0]):
        print(f'-{sub_key} -> damage: {sub_value[0]}, health: {sub_value[1]}, armor: {sub_value[2]}')
