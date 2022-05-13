numbers = str(input()).split(', ')

numbers = [int(i) for i in numbers]

for element in numbers:
    if element == 0:
        numbers.remove(element)
        numbers.append(element)

print(numbers)