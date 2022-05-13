text = str(input())
sum_total = 0

for i in range(0, len(text)):
    if text[i] == "a":
        sum_total += 1
    if text[i] == "e":
        sum_total += 2
    if text[i] == "i":
        sum_total += 3
    if text[i] == "o":
        sum_total += 4
    if text[i] == "u":
        sum_total += 5
print(sum_total)
