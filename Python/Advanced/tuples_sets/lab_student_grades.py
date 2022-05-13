num_students = int(input())

student_dict = {}

for i in range(num_students):
    data = input().split()
    student = data[0]
    grade = float(data[1])
    if student not in student_dict:
        student_dict[student] = [grade]
    else:
        student_dict[student].append(grade)

for key, value in student_dict.items():
    print(f"{key} -> ", end="")
    for val in value:
        print(f"{val:.2f}", end=" ")
    print(f"(avg: {sum(value)/len(value):.2f})")
