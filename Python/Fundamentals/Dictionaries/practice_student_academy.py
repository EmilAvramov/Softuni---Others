rows = int(input())

student_dict = {}

for i in range(rows):
    name = input()
    grade = float(input())
    if name not in student_dict:
        student_dict[name] = [grade]
    else:
        student_dict[name] += [grade]

for key, value in student_dict.items():
    if sum(value) / len(value) >= 4.50:
        print(f"{key} -> {sum(value) / len(value):.2f}")
