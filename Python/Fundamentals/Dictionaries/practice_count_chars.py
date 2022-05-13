data = "".join(input().split())

# Method 1, comprehension
letter_dict = {value: data.count(value) for index, value in enumerate(data)}

# Method 2, long way
# letter_dict = {}
# for index, value in enumerate(data):
#     if value not in letter_dict:
#         letter_dict[value] = 1
#     else:
#         letter_dict[value] += 1

for key, value in letter_dict.items():
    print(f"{key} -> {value}")
