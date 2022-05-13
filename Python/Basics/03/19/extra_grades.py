num_students = int(input())

total_grade = 0
fail = 0
barely = 0
decent = 0
great = 0

for i in range(1, num_students+1):
    grade = float(input())
    if 2 <= grade <= 2.99:
        fail += 1
        total_grade += grade
    elif 3 <= grade <= 3.99:
        barely += 1
        total_grade += grade
    elif 4 <= grade <= 4.99:
        decent += 1
        total_grade += grade
    else:
        great += 1
        total_grade += grade

print(f'Top students: {(great/num_students)*100:.2f}%', end='\n')
print(f'Between 4.00 and 4.99: {(decent/num_students)*100:.2f}%', end='\n')
print(f'Between 3.00 and 3.99: {(barely/num_students)*100:.2f}%', end='\n')
print(f'Fail: {(fail/num_students)*100:.2f}%', end='\n')
print(f'Average: {total_grade/num_students:.2f}')