import sys

array = [int(i) for i in input().split(" ")]
data = input()


def evens(arr):
    return [i for i in arr if i % 2 == 0]


def odds(arr):
    return [i for i in arr if i % 2 != 0]


def first(arr, count, method):
    if method == "even":
        data = evens(arr)
    else:
        data = odds(arr)
    if data:
        if count <= len(data):
            return data[:count]
        return data
    return []


def last(arr, count, method):
    if method == "even":
        data = evens(arr)
    else:
        data = odds(arr)
    if data:
        data = data[::-1]
        if count <= len(data):
            data = data[:count]
            return data[::-1]
        return data
    return []


while data != "end":
    cmd = data.split(" ")[0]
    if cmd == "exchange":
        idx = int(data.split(" ")[1])
        if idx < 0 or idx >= len(array):
            print("Invalid index")
        else:
            p1 = array[0 : idx + 1]
            p2 = array[idx + 1 :]
            array = p2 + p1
    elif cmd == "min" or cmd == "max":
        attr = data.split(" ")[1]
        if cmd == "min":
            if attr == "even":
                num = sys.maxsize
                idx = 0
                for i in range(len(array)):
                    if array[i] % 2 == 0:
                        if array[i] <= num:
                            num = array[i]
                            idx = i
                if num != sys.maxsize:
                    print(idx)
                else:
                    print("No matches")
            elif attr == "odd":
                num = sys.maxsize
                idx = 0
                for i in range(len(array)):
                    if array[i] % 2 != 0:
                        if array[i] <= num:
                            num = array[i]
                            idx = i
                if num != -sys.maxsize:
                    print(idx)
                else:
                    print("No matches")
        else:
            if attr == "even":
                num = -sys.maxsize
                idx = 0
                for i in range(len(array)):
                    if array[i] % 2 == 0:
                        if array[i] >= num:
                            num = array[i]
                            idx = i
                if num != sys.maxsize:
                    print(idx)
                else:
                    print("No matches")
            elif attr == "odd":
                num = -sys.maxsize
                idx = 0
                for i in range(len(array)):
                    if array[i] % 2 != 0:
                        if array[i] >= num:
                            num = array[i]
                            idx = i
                if num != -sys.maxsize:
                    print(idx)
                else:
                    print("No matches")
    elif cmd == "first" or cmd == "last":
        count = int(data.split(" ")[1])
        attr = data.split(" ")[2]
        if count > len(array):
            print("Invalid count")
        else:
            if cmd == "first":
                print(first(array, count, attr))
            else:
                print(last(array, count, attr))

    data = input()

print(array)
