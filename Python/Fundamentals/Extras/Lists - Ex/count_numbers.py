numbers = [int(i) for i in input().split()]

for number in sorted(set(numbers)):
    print(f"{number} -> {numbers.count(number)}")
