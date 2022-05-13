start = ord(input())
end = ord(input())
string = input()

total_sum = 0

for letter in string:
    if start < ord(letter) < end:
        total_sum += ord(letter)

print(total_sum)