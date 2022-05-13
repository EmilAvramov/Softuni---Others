string = input().split()

other_list = [string[-1]] + [i for i in string[0:-1]]

print(*other_list, sep=' ')
