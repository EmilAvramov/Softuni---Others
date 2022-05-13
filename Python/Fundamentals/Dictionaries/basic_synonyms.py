n = int(input())
word_dict = {}

for iteration in range(n):
    word = input()
    synonym = input()
    if word not in word_dict:
        word_dict[word] = synonym
    else:
        word_dict[word] += f', {synonym}'

for key, value in word_dict.items():
    print(f"{key} - {value}")
