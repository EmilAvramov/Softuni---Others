numbers = str(input()).split()
string = str(input())

index_sum = 0
index_list = []
index_char = 0
word = []

for number in numbers:
    for index, value in enumerate(number):
        index_sum += int(value)
        if index == len(number) - 1:
            index_list.append(index_sum)
            index_sum = 0

for number in index_list:
    index_char = number
    if index_char > len(string):
        index_char = index_char % len(string)
    for index, char in enumerate(string):
        if index == index_char:
            word.append(char)
            string = string[:index] + string[index + 1:]

print(*word, sep='')

