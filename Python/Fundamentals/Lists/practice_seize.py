indicators = str(input()).replace(' = ', '#').split('#')
water = int(input())

nested_list = [indicators[i:i+2] for i in range(0, len(indicators), 2)]
nested_list = [[int(element) if element.isdigit() else element for element in row] for row in nested_list]
for element in nested_list:
    element.append(0)

effort = 0
total_fire = 0
stop_flag = False
used_cells = []

while stop_flag is False:
    for cell in nested_list:
        if cell[1] <= water:
            if (cell[0] == "High" and 81 <= cell[1] <= 125 and cell[2] == 0) or \
                    (cell[0] == "Medium" and 51 <= cell[1] <= 80 and cell[2] == 0) or \
                    (cell[0] == "Low" and 1 <= cell[1] <= 50 and cell[2] == 0):
                water -= cell[1]
                effort += cell[1] * 0.25
                total_fire += cell[1]
                cell[2] = 1
    stop_flag = True

for element in nested_list:
    if element[2] == 1:
        used_cells.append(element[1])

print(f'Cells:', end='\n')
if len(used_cells) >= 1:
    print(f' -', end=' ')
    print(*used_cells, sep='\n - ')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
