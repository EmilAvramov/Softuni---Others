# # Task 1
# def every_three_nums(start):
#     lst = []
#     for i in range(start, 101, 3):
#         lst.append(i)
#     return lst
#
# # Task 2
# def remove_middle(lst, start, end):
#     return lst[:start] + lst[end + 1:]
#
# # Task 3
# def more_frequent_item(lst, item1, item2):
#     if lst.count(item1) >= lst.count(item2):
#         return item1
#     else:
#         return item2
#
# # Task 4
# def double_index(lst, index):
#     if index < len(lst) - 1:
#         if lst[index] in lst:
#             lst[index] *= 2
#             return lst
#     else:
#         return lst
#
# # Task 5
# def middle_element(lst):
#     if len(lst) % 2 != 0:
#         return lst[int(len(lst) / 2)]
#     else:
#         average = (lst[int((len(lst) / 2) - 1)] + lst[int((len(lst) / 2))]) / 2
#         return average
