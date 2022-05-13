banned_words = str(input()).split(", ")
text = str(input())

for word in banned_words:
    if word in text:
        text = text.replace(word, '*' * len(word))

print(text)