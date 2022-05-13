list_numbers = [int(i) for i in input().split()]
reverse_list = list_numbers[::-1]

print(*reverse_list, sep=' ')