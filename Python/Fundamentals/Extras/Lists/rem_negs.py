full_list = [int(i) for i in input().split() if int(i) > 0]

full_list = full_list[::-1]

if len(full_list) > 0:
    print(*full_list, sep=' ')
else:
    print(f'empty')
