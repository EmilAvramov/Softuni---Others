command = input().split(" : ")

courses = {}

while command[0] != "end":
    course = command[0]
    student = command[1]
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course] += [student]
    command = input().split(" : ")

for key, value in courses.items():
    print(f'{key}: {len(value)}')
    for key_sub, value_sub in courses.items():
        for i in range(len(value_sub)):
            if key_sub in key:
                print(f'-- {value_sub[i]}')
