num_names = int(input())
set_names = {input() for i in range(num_names)}

for name in set_names:
    print(name, end="\n")
