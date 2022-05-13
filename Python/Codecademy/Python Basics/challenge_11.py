# # Task 1
# def sum_values(my_dictionary):
#     return sum(my_dictionary.values())
#
# # Task 2
# def sum_even_keys(my_dictionary):
#     counter = 0
#     for key, value in my_dictionary.items():
#         if key % 2 == 0:
#             counter += value
#     return counter
#
# # Task 3
# def add_ten(my_dictionary):
#     for keys, value in my_dictionary.items():
#         my_dictionary[keys] += 10
#     return my_dictionary
#
# # Task 4
# def values_that_are_keys(my_dictionary):
#     return [value for value in my_dictionary.values() if value in my_dictionary.keys()]
#
# # Task 5
# import sys
#
# def max_key(my_dictionary):
#     largest_key = ""
#     largest_value = -sys.maxsize
#     for key, value in my_dictionary.items():
#         if value > largest_value:
#             largest_key = key
#             largest_value = value
#     return largest_key
