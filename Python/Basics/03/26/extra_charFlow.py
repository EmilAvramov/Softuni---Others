mid_word = ""
word = ""
secret_counter = 0
char = ""
c_counter = 0
o_counter = 0
n_counter = 0

while char != "End":
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        if char == "c" and c_counter == 0:
            c_counter += 1
            secret_counter += 1
        elif char == "o" and o_counter == 0:
            o_counter += 1
            secret_counter += 1
        elif char == "n" and n_counter == 0:
            n_counter += 1
            secret_counter += 1
        else:
            mid_word += char
        if secret_counter == 3:
            word += mid_word + " "
            mid_word = ""
            secret_counter = 0
            c_counter = 0
            o_counter = 0
            n_counter = 0
    char = str(input())

print(word)
