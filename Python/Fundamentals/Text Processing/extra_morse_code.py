morse = [i.split(" ") for i in input().split(" | ")]

morse_dict = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
              "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
              "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
              "-.--": "Y", "--..": "Z"}

result = ""

for word in morse:
    for letter in word:
        if letter in morse_dict.keys():
            result += morse_dict[letter]
    result += " "

print(result)