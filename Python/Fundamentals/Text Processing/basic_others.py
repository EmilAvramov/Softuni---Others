# Method 1, list comprehension
# string = str(input())
# numbers = [i for i in string if i.isdigit()]
# letters = [i for i in string if i.isalpha()]
# symbols = [i for i in string if i.isdigit() is False and i.isalpha() is False]
#
# print(*numbers, sep='')
# print(*letters, sep='')
# print(*symbols, sep='')

# Method 2, If
string = str(input())
numbers = ""
letters = ""
symbols = ""

for char in string:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        symbols += char

print(numbers)
print(letters)
print(symbols)