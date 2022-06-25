data = [int(i) for i in input().split(" ")]
average = sum(data) / len(data)
top_5 = [i for i in data if i > average]
top_5 = sorted(top_5, reverse=True)

if len(top_5) == 0:
    print("No")
elif len(top_5) < 5:
    print(*top_5, sep=" ")
else:
    for i in range(5):
        print(top_5[i], end=" ")
