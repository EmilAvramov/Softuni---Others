people = int(input())
name = ""

sum_total = 0
sum_per_name = 0
name_count = 0

while name != "Finish":
    name = str(input())
    if name == "Finish":
        print(f"Student's final assessment is {round((sum_total / name_count),2):.2f}.")
        break
    for i in range(1, people + 1):
        grade = float(input())
        sum_per_name += grade
        if i == people:
            print(f'{name} - {round((sum_per_name / people),2):.2f}.')
            name_count += 1
            sum_total += (sum_per_name / people)
            sum_per_name = 0
            break