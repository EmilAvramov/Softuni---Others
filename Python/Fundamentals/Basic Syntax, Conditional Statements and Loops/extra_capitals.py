word = str(input())

list_word = []

for index, value in enumerate(word):
    if 65 <= ord(value) <= 90:
        list_word.append(index)

print(list_word)