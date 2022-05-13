banned = input().split()
text = input()

for word in banned:
    text = text.replace(word, len(word) * "*")

print(text)
