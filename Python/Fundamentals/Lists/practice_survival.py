numbers = [int(i) for i in str(input()).split(" ")]
count = int(input())

sorted_list = sorted(numbers)
exclusion_list = sorted_list[:count]
output_list = []

for number in range(len(numbers)):
    if numbers[number] not in exclusion_list:
        output_list.append(numbers[number])

print(*output_list, sep=", ")
# can also do the below
# print(', '.join(map(str, output_list)))
