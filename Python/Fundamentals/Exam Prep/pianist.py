count = int(input())
pieces = {}

for i in range(count):
    data = input().split("|")
    pieces[data[0]] = [data[1], data[2]]

data = input()

while data != "Stop":
    cmd = data.split("|")[0]
    if cmd == "Add":
        piece = data.split("|")[1]
        composer = data.split("|")[2]
        key = data.split("|")[3]
        if piece in pieces.keys():
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif cmd == "Remove":
        piece = data.split("|")[1]
        if piece in pieces.keys():
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(
                f"Invalid operation! {piece} does not exist in the collection."
            )
    elif cmd == "ChangeKey":
        piece = data.split("|")[1]
        key = data.split("|")[2]
        if piece in pieces.keys():
            pieces[piece][1] = key
            print(f"Changed the key of {piece} to {key}!")
        else:
            print(
                f"Invalid operation! {piece} does not exist in the collection."
            )
    data = input()

for [piece, values] in pieces.items():
    print(f"{piece} -> Composer: {values[0]}, Key: {values[1]}")
