num_fail = int(input())

text = ""
score = 0
problem_count = 0
fail_count = 0
total_score = 0
last_problem = ""

while text != "Enough" or fail_count < num_fail:
    text = str(input())
    if text != "Enough":
        last_problem = text
    else:
        print(f'Average score: {total_score / problem_count:.2f}', end='\n')
        print(f'Number of problems: {problem_count}', end='\n')
        print(f'Last problem: {last_problem}')
        break
    score = float(input())
    total_score += score
    if score <= 4:
        fail_count += 1
    if fail_count == num_fail:
        print(f'You need a break, {fail_count} poor grades.')
        break
    problem_count += 1
