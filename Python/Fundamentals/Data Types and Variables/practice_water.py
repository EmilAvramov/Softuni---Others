count = int(input())

capacity = 255
inflow = 0

for i in range(1, count + 1):
    water = int(input())
    inflow += water
    if capacity < inflow:
        print(f'Insufficient capacity!')
        inflow -= water

print(inflow)