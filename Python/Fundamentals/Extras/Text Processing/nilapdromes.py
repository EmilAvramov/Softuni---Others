from math import floor

word = input()
border = ""
core = ""
result = ""

while word != "end":
    for i in range(floor(len(word)/2), 0, -1):
        if word[:i] == word[-i:] and len(word[i:-i]) > 0:
            border = word[:i]
            core = word[i:-i]
            result = core + border + core
            print(result)
            break
    word = input()
