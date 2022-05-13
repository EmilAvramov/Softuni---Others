first = int(input())
second = int(input())

for n_int in range(first, second + 1):
    n_str = str(n_int)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(n_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(n_int, end=' ')

