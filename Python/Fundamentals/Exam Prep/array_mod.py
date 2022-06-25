arr = [int(i) for i in input().split(" ")]
cmd = input()

while cmd != "end":
    operation = cmd.split(" ")[0]
    if operation == "swap":
        idx_1 = int(cmd.split(" ")[1])
        idx_2 = int(cmd.split(" ")[2])
        arr[idx_1], arr[idx_2] = arr[idx_2], arr[idx_1]
    elif operation == "multiply":
        idx_1 = int(cmd.split(" ")[1])
        idx_2 = int(cmd.split(" ")[2])
        arr[idx_1] = arr[idx_1] * arr[idx_2]
    elif operation == "decrease":
        arr = [i - 1 for i in arr]
    cmd = input()


print(*arr, sep=", ")
