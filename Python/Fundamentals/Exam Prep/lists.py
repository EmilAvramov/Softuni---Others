data = input()


while data != "stop playing":
    data = [int(i) for i in data.split(" ") if i]
    if len(data) == len(set(data)):
        for i in range(len(data)):
            if data[i] % 2 == 0:
                data[i] += 2
        data = sorted(data)
        print(f"Unique list: {','.join([str(i) for i in data])}")
        print(f"Output: {sum(data)/len(data):.2f}")
    else:
        for i in range(len(data)):
            if data[i] % 2 != 0:
                data[i] += 3
        data = sorted(data)
        print(f"Non-unique list: {':'.join([str(i) for i in data])}")
        print(f"Output: {sum(data)/len(data):.2f}")
    data = input()
