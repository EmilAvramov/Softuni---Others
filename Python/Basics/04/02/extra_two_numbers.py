start = int(input())
end = int(input())
magic_number = int(input())

counter = 0
break_flag = False
match_flag = False

for x in range(start, end + 1):
    for y in range(start, end + 1):
        counter += 1
        if x + y == magic_number:
            print(f'Combination N:{counter} ({x} + {y} = {magic_number})')
            break_flag = True
            match_flag = True
            break
    if break_flag:
        break

if match_flag is False:
    print(f'{counter} combinations - neither equals {magic_number}')