message = input()
data = input()

while data != "Decode":
    cmd = data.split("|")[0]
    if cmd == "Move":
        count = int(data.split("|")[1])
        message = message[count:] + message[:count]
    elif cmd == "Insert":
        index = int(data.split("|")[1])
        value = data.split("|")[2]
        message = message[:index] + value + message[index:]
    elif cmd == "ChangeAll":
        substring = data.split("|")[1]
        replacement = data.split("|")[2]
        message = message.replace(substring, replacement)

    data = input()

print(f"The decrypted message is: {message}")
