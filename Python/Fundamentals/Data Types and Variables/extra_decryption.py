key = int(input())
rows = int(input())

message = ""

for i in range(1, rows + 1):
    letter = str(input())
    letter_transformed = chr(ord(letter) + key)
    message += letter_transformed

print(message)