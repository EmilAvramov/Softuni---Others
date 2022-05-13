num_pairs = int(input())
prev_sum = int(input()) + int(input())

max_diff = 0

for i in range(1, num_pairs):
    current_sum = int(input()) + int(input())
    if abs(prev_sum - current_sum) > max_diff:
        max_diff = abs(prev_sum - current_sum)
    prev_sum = current_sum

if max_diff == 0:
    print(f'Yes, value={prev_sum}')
else:
    print(f'No, maxdiff={max_diff}')