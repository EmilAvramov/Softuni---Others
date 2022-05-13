# # Task 1
# def check_for_name(sentence, name):
#     return name in sentence or name.lower() in sentence or name.upper() in sentence
#
# # Task 2
# def every_other_letter(word):
#     string = ""
#     for index, letter in enumerate(word):
#         if index % 2 == 0:
#             string += letter
#     return string
#
# # Task 3
# def reverse_string(word):
#     return word[::-1]
#
# # Task 4
# def make_spoonerism(word1, word2):
#     return f'{word2[0] + word1[1:]} {word1[0] + word2[1:]}'
#
# # Task 5
# def add_exclamation(word):
#     while len(word) < 20:
#         word += "!"
#     return word
