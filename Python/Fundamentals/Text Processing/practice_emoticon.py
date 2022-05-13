text = input()

emoticons = []

for i in range(len(text)):
    if ":" in text[i]:
        emoticons.append(text[i:i+2])

print(*emoticons, sep='\n')