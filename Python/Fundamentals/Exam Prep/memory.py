data = input().split(" ")
cmd = input()

moves = 0
matching = 0

while cmd != "end":
    moves += 1
    mid = int(len(data) / 2)
    num_1 = cmd.split(" ")[0]
    num_2 = cmd.split(" ")[1]
    if num_1.isalpha() or num_2.isalpha():
        data.insert(mid, f"-{moves}a")
        data.insert(mid, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif num_1 == num_2:
        data.insert(mid, f"-{moves}a")
        data.insert(mid, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if (
            0 > int(num_1)
            or int(num_1) >= len(data)
            or 0 > int(num_2)
            or int(num_2) >= len(data)
        ):
            data.insert(mid, f"-{moves}a")
            data.insert(mid, f"-{moves}a")
            print("Invalid input! Adding additional elements to the board")
        else:
            idx_1 = data[int(num_1)]
            idx_2 = data[int(num_2)]
            if idx_1 == idx_2:
                if num_1 > num_2:
                    data.remove(idx_1)
                    data.remove(idx_2)
                else:
                    data.remove(idx_2)
                    data.remove(idx_1)
                matching += 1
                print(f"Congrats! You have found matching elements - {idx_1}!")
                if len(data) == 0:
                    break
            else:
                print("Try again!")
    cmd = input()

if data:
    print("Sorry you lose :(")
    print(*data, sep=" ")
else:
    print(f"You have won in {moves} turns!")
