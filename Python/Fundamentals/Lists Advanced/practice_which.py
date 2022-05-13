line_1 = str(input()).split(', ')
line_2 = str(input()).split(', ')

line_3 = [word_1 for word_1 in line_1 if any(word_1 in word_2 for word_2 in line_2)]

print(line_3)
