width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

while free_space > 0:
    num_boxes = str(input())
    if num_boxes == "Done":
        print(f'{free_space} Cubic meters left.')
        break
    else:
        num_boxes_int = int(num_boxes)
        free_space -= num_boxes_int
        if free_space <= 0:
            print(f'No more free space! You need {abs(free_space)} Cubic meters more.')
            break
