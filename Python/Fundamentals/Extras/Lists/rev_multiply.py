num_list = [int(i) for i in input().split()]
multiplier = int(input())

mult_list = []

for number in num_list:
    mult_list.append(number * multiplier)

print(*mult_list, sep=' ')
