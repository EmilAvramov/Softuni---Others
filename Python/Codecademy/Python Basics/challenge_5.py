# # Task 1
# def divisible_by_ten(nums):
#     counter = 0
#     for i in nums:
#         if i % 10 == 0:
#             counter += 1
#     return counter
#
# # Task 2
# def add_greetings(names):
#     list_names = []
#     for i in names:
#         list_names.append(f'Hello, {i}')
#     return list_names

# # Task 3
# def delete_starting_evens(lst):
#     while lst[0] % 2 == 0:
#         lst.pop(0)
#         if len(lst) == 0:
#             break
#     return lst

# # Task 4
# def odd_indices(lst):
#     result = [lst[i] for i in range(1, len(lst), 2)]
#     return result


# Task 5
# def exponents(bases, powers):
#     result = [b ** p for b in bases for p in powers]
#     return result
#