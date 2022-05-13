count = int(input())
total = 0

for i in range(1, count + 1):
    number = int(input())
    total += number

print(f'{total/count:.2f}')