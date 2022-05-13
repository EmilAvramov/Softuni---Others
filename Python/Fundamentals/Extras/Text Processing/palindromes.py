orig_list = [i for i in input().split() if i == i[::-1]]
new_list = []

for word in orig_list:
    if word not in new_list:
        new_list.append(word)

print(', '.join(sorted(new_list, key=str.lower)))
