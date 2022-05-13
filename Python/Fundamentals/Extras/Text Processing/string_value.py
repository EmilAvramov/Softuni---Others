data = input()
command = input()

upper_sum = 0
lower_sum = 0

if command == "UPPERCASE":
    for letter in data:
        if letter.isupper():
            upper_sum += ord(letter)
else:
    for letter in data:
        if letter.islower():
            lower_sum += ord(letter)

if command == "UPPERCASE":
    print(f"The total sum is: {upper_sum}")
else:
    print(f"The total sum is: {lower_sum}")
