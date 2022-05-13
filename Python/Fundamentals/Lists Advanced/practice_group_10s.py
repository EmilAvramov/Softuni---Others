numbers = [int(i) for i in str(input()).split(', ')]

boundary = 0
copy_counter = 0

for i in range(1, (max(numbers) // 10 + 1) + 1):
    boundary = i * 10
    temp_list = [number for number in numbers if boundary - 10 < number <= boundary]
    print(f"Group of {i}0's: {temp_list}")
    copy_counter += len(temp_list)
    if copy_counter == len(numbers):
        break
    temp_list.clear()
