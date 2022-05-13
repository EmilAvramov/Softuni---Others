string = [i for i in str(input()).split() if len(i) % 2 == 0]

print(*string, sep='\n')
