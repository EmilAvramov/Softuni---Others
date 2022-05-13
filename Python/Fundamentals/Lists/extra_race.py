numbers = str(input()).split()

numbers = [int(i) for i in numbers]
mid = len(numbers) // 2

left_sum = 0
right_sum = 0

for left in numbers[:mid]:
    if left != 0:
        left_sum += left
    else:
        left_sum *= 0.8

for right in reversed(numbers[mid + 1:]):
    if right != 0:
        right_sum += right
    else:
        right_sum *= 0.8

if left_sum < right_sum:
    print(f'The winner is left with total time: {left_sum:.1f}')
else:
    print(f'The winner is right with total time: {right_sum:.1f}')
