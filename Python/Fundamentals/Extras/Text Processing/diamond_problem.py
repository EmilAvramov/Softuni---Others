data = input()
diamonds = []
carats = 0

for letter in data:
    if "<" not in data:
        break
    if letter != ">" and letter.isdigit():
        carats += int(letter)
    elif letter == ">":
        if carats >= 1:
            diamonds.append(carats)
        carats = 0

if len(diamonds) == 0:
    print(f"Better luck next time")
else:
    for diamond in diamonds:
        print(f"Found {diamond} carat diamond")
