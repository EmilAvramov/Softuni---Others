front_back_walls_side = float(input())
side_walls_side = float(input())
ceiling_height = float(input())
front_door_area = 1.2 * 2
window_area = 1.5 * 1.5 * 2
front_back_walls_area = (front_back_walls_side * front_back_walls_side) * 2 - front_door_area
side_walls_side_area = (front_back_walls_side * side_walls_side) * 2 - window_area
ceiling_area = ((front_back_walls_side * side_walls_side) * 2) + (((front_back_walls_side * ceiling_height) / 2) * 2)
paint_green = float((front_back_walls_area + side_walls_side_area) / 3.4)
paint_red = float(ceiling_area / 4.3)
print(f'{paint_green:.2f}', end='\n')
print(f'{paint_red:.2f}')


area = (side_a + side_b) * height / 2
print(f'{area:.2f}')