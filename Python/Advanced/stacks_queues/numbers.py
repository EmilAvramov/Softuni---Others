set_one = {int(i) for i in input().split(" ")}
set_two = {int(i) for i in input().split(" ")}
lines = int(input())

for _ in range(lines):
    tokens = input().split(" ")
    command = tokens[0]
    sub_c = tokens[1]
    if command == "Add" or command == "Remove":
        numbers = [int(i) for i in tokens[2:]]
        if command == "Add":
            for number in numbers:
                if sub_c == "First":
                    set_one.add(number)
                elif sub_c == "Second":
                    set_two.add(number)
        elif command == "Remove":
            for number in numbers:
                if sub_c == "First":
                    if set_one:
                        if number in set_one:
                            set_one.remove(number)
                elif sub_c == "Second":
                    if set_two:
                        if number in set_two:
                            set_two.remove(number)
    elif command == "Check":
        if set_one.issubset(set_two) or set_two.issubset(set_one):
            print("True")
        else:
            print("False")

set_one_sorted = sorted(list(set_one))
set_two_sorted = sorted(list(set_two))

print(*set_one_sorted, sep=", ")
print(*set_two_sorted, sep=", ")
