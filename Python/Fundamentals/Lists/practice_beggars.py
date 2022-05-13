numbers = [int(i) for i in str(input()).split(', ')]
beggars = int(input())

totals = [0 for i in range(beggars)]
count = 0

for coin in numbers:
    totals[count] += coin
    count += 1
    if count >= beggars:
        count = 0

print(totals)

# Too long
# for beggar in range(len(totals)):
#     current_beggar = beggar
#     for number in range(len(numbers)):
#         current_num = number % beggars
#         if current_num == current_beggar:
#             if totals[beggar] == 0:
#                 if numbers[number] == 0:
#                     totals[current_num] = 0
#                     break
#                 totals[current_num] = numbers[number]
#             else:
#                 totals[current_num] += numbers[number]


