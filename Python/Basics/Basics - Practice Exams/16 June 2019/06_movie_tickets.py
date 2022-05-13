a1 = int(input())
a2 = int(input())
n = int(input())

for a in range(ord(chr(a1)), ord(chr(a2))):
    if ord(chr(a)) % 2 != 0:
        for b in range(1, n):
            for c in range(1, int(n / 2)):
                d = ord(chr(a))
                if (b + c + d) % 2 != 0:
                    print(f'{chr(a)}-{ord(chr(b))}{(ord(chr(c)))}{d}')


