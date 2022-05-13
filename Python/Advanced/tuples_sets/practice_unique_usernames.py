count = int(input())
uniques = {input() for i in range(count)}

print(*uniques, sep="\n")
