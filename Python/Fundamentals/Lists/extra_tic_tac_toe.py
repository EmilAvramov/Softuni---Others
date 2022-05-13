line_1 = [int(i) for i in str(input()).split()]
line_2 = [int(i) for i in str(input()).split()]
line_3 = [int(i) for i in str(input()).split()]

first = 0
second = 0

if line_1[0] == 1 and line_1[1] == 1 and line_1[2] == 1:
    first = 1
elif line_2[0] == 1 and line_2[1] == 1 and line_2[2] == 1:
    first = 1
elif line_3[0] == 1 and line_3[1] == 1 and line_3[2] == 1:
    first = 1
elif line_1[0] == 1 and line_2[1] == 1 and line_3[2] == 1:
    first = 1
elif line_1[2] == 1 and line_2[1] == 1 and line_3[0] == 1:
    first = 1
elif line_1[0] == 1 and line_2[0] == 1 and line_3[0] == 1:
    first = 1
elif line_1[1] == 1 and line_2[1] == 1 and line_3[1] == 1:
    first = 1
elif line_1[2] == 1 and line_2[2] == 1 and line_3[2] == 1:
    first = 1

if line_1[0] == 2 and line_1[1] == 2 and line_1[2] == 2:
    second = 1
elif line_2[0] == 2 and line_2[1] == 2 and line_2[2] == 2:
    second = 1
elif line_3[0] == 2 and line_3[1] == 2 and line_3[2] == 2:
    second = 1
elif line_1[0] == 2 and line_2[1] == 2 and line_3[2] == 2:
    second = 1
elif line_1[2] == 2 and line_2[1] == 2 and line_3[0] == 2:
    second = 1
elif line_1[0] == 2 and line_2[0] == 2 and line_3[0] == 2:
    second = 1
elif line_1[1] == 2 and line_2[1] == 2 and line_3[1] == 2:
    second = 1
elif line_1[2] == 1 and line_2[2] == 1 and line_3[2] == 1:
    second = 1

if first == 1:
    print(f'First player won')
elif second == 1:
    print(f'Second player won')
else:
    print(f'Draw!')
