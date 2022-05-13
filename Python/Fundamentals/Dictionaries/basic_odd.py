data = input().lower().split()
odd_dict = {key: data.count(key) for key in data}

for key, value in odd_dict.items():
    if value % 2 != 0:
        print(key, end=' ')
