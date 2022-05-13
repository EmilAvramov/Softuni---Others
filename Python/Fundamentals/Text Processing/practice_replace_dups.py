text = input()

new_text = []

for index, value in enumerate(text):
    if index != len(text) - 1:
        if not text[index] == text[index+1]:
            new_text.append(value)
    else:
        new_text.append(value)

print(''.join(new_text))