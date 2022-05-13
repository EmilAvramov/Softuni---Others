rooms = int(input())

free_chairs = 0
print_counter = 0

for i in range(1, rooms + 1):
    data = str(input()).split()
    if len(data[0]) < int(data[1]):
        print(f'{abs(int(data[1]) - len(data[0]))} more chairs needed in room {i}')
        print_counter = 1
    else:
        free_chairs += len(data[0]) - int(data[1])

if print_counter != 1:
    print(f'Game On, {free_chairs} free chairs left')
