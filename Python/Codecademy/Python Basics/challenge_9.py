# # Task 1
# def unique_english_letters(word):
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#     count = 0
#     match = ""
#     for letter in letters:
#         if letter in word:
#             if letter not in match:
#                 match += letter
#                 count += 1
#     return count
#
# # Task 2
# def count_char_x(word, x):
#     count = 0
#     for index, value in enumerate(str(word)):
#         if value == x:
#             count += 1
#     return count
#
# # Task 3
# def count_multi_char_x(word, x):
#     splits = word.split(x)
#     return len(splits) - 1
#
# # Task 4
# def substring_between_letters(word, start, end):
#     if start in word and end in word:
#         return word[word.index(start) + 1: word.index(end)]
#     else:
#         return word
#
# # Task 5
# def x_length_words(sentence, x):
#     sentence = sentence.split()
#     count = 0
#     for word in sentence:
#         if len(word) >= x:
#             count += 1
#     if count == len(sentence):
#         return True
#     else:
#         return False