# Method 1 using list comprehension
string = [index for index, value in enumerate(str(input()).split(', ')) if int(value) % 2 == 0]

print(string)

# Method 2 using map and lambda
# string = list(map(int, input().split(', ')))
# detect_even_indices = map(
#     lambda x: x if string[x] % 2 == 0 else "False",
#     range(len(string))
# )
# found_evens = list(filter(lambda x: x != "False", detect_even_indices))
# print(found_evens)
