lines = int(input())
odd_set = set()
even_set = set()
final_set = set()
sum_name = 0

for i in range(1, lines + 1):
    name = input()
    for letter in name:
        sum_name += ord(letter)
    sum_name = sum_name // i
    if sum_name % 2 == 0:
        even_set.add(sum_name)
    else:
        odd_set.add(sum_name)
    sum_name = 0

if sum(odd_set) == sum(even_set):
    final_set = odd_set | even_set
elif sum(odd_set) > sum(even_set):
    final_set = odd_set - even_set
else:
    final_set = odd_set ^ even_set

print(*final_set, sep=", ")
