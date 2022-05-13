hall_length = float(input())
hall_width = float(input())
desk_length = float(1.2)
desk_width = float(0.7)
hall_free_width = hall_width - float(1)
desk_width_qty = float(hall_free_width // desk_width)
desk_length_qty = float(hall_length // desk_length)
desk_total_qty = desk_length_qty * desk_width_qty - 3
print(f'{desk_total_qty:.0f}')
