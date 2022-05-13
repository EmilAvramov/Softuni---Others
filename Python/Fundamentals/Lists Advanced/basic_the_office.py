numbers = [int(i) for i in str(input()).split()]
factor = int(input())

mult_list = list(map(lambda x: x * factor, numbers))
filtered_list = list(filter(lambda x: x > sum(mult_list)/len(mult_list), mult_list))

if len(filtered_list) < len(mult_list) / 2:
    print(f'Score {len(filtered_list)}/{len(mult_list)}. Employees are not happy!')
else:
    print(f'Score {len(filtered_list)}/{len(mult_list)}. Employees are happy!')
