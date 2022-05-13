numbers = [float(i) for i in input().split()]
numbers_2 = input()
numbers_set = set()

for number in numbers:
    if number not in numbers_set:
        numbers_set.add(number)
        print(f"{number:.1f} - {numbers.count(number)} times")
