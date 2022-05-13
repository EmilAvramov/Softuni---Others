size = int(input())

for i in range(1, size):
    print(" " * (size - i) + "* " * i)
print("* " * size)
for i in range(size - 1, 0, -1):
    print(" " * (size - i) + "* " * i)
