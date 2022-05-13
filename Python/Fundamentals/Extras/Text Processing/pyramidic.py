rows = int(input())

collection = []
uniques = []
pyramid = []

for row in range(rows):
    string = input()
    collection.append(string)

for elem in collection:
    for letter in elem:
        if letter not in uniques:
            uniques.append(letter)

for unique in uniques:
    for elem in collection[::-1]:
        for letter in elem:
            if len(pyramid) == 0:
                if len(elem) % 2 == 1:
                    length = len(elem)
                else:
                    length = len(elem) - 1
                for i in range(length, 0, -2):
                    if elem.count(letter) == i:
                        pyramid.append(letter * i)
            else:
                if elem.count(letter) > len(pyramid[0]):
                    pyramid = []
                    continue
                length = len(pyramid[-1]) - 2
                if elem.count(letter) - len(pyramid) * 2 == length \
                        and letter in pyramid[-1]:
                    pyramid.append(length * letter)

pyramid = sorted(pyramid)
print(*pyramid, sep='\n')
