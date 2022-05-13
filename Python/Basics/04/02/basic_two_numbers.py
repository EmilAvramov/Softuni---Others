start = int(input())
end = int(input())
number = int(input())

sequence = 0
is_found = False

for i in range(start, end + 1):
    for x in range(start, end + 1):
        sequence += 1
        if i + x == number:
            print(f'Combination N:{sequence} ({i} + {x} = {number})')
            is_found = True
            break
    if is_found:
        break

if is_found is False:
    print(f'{sequence} combinations - neither equals {number}')