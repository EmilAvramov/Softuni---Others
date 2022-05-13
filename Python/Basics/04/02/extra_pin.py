num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
holder_1 = 0
holder_2 = 0
holder_3 = 0

for x in range(1, num_1 + 1):
    if x % 2 == 0:
        holder_1 = int(x)
        for y in range(2, num_2 + 1):
            if y == 2 or y == 3 or y == 5 or y == 7:
                holder_2 = int(y)
                for z in range(1, num_3 + 1):
                    if z % 2 == 0:
                        holder_3 = int(z)
                        print(f'{holder_1} {holder_2} {holder_3}')




