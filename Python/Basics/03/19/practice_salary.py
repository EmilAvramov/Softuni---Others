browser_tabs = int(input())
salary = int(input())

penalty = 0
total_penalty = 0

for i in range(1, browser_tabs + 1):
    site = str(input())
    if site == "Facebook":
        penalty = 150
        total_penalty += penalty
    elif site == "Instagram":
        penalty = 100
        total_penalty += penalty
    elif site == "Reddit":
        penalty = 50
        total_penalty += penalty
    if total_penalty >= salary:
        print(f'You have lost your salary.')
        break

if total_penalty < salary:
    print(f'{abs(salary - total_penalty):.0f}')

