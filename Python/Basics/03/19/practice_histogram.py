sequence = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, sequence + 1):
    num = float(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    else:
        p5 += 1

print(f'{(p1/sequence)*100:.2f}%', end='\n')
print(f'{(p2/sequence)*100:.2f}%', end='\n')
print(f'{(p3/sequence)*100:.2f}%', end='\n')
print(f'{(p4/sequence)*100:.2f}%', end='\n')
print(f'{(p5/sequence)*100:.2f}%')