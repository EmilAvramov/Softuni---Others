numbers = [int(i) for i in str(input()).split()]
command = str(input()).split()

transform = []
even = []
odd = []

while command[0] != "end":
    even = [int(i) for i in numbers if i % 2 == 0]
    odd = [int(i) for i in numbers if i % 2 != 0]
    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(numbers):
            transform.append(numbers[int(command[1]) + 1:])
            transform.append(numbers[:int(command[1]) + 1])
            numbers.clear()
            numbers = [li for element in transform for li in element]
        else:
            print(f'Invalid index')
    elif command[0] == "max":
        if command[1] == "even":
            if len(even) == 0:
                print('No matches')
            else:
                print((len(numbers) - numbers[::-1].index(max(even)) - 1))
        else:
            if len(odd) == 0:
                print('No matches')
            else:
                print((len(numbers) - numbers[::-1].index(max(odd)) - 1))
    elif command[0] == "min":
        if command[1] == "even":
            if len(even) == 0:
                print('No matches')
            else:
                print((len(numbers) - numbers[::-1].index(min(even)) - 1))
        else:
            if len(odd) == 0:
                print('No matches')
            else:
                print((len(numbers) - numbers[::-1].index(min(odd)) - 1))
    elif command[0] == "first":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even[0:int(command[1])])
            else:
                print(odd[0:int(command[1])])
        else:
            print(f"Invalid count")
    elif command[0] == "last":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even[-int(command[1]):])
            else:
                print(odd[-int(command[1]):])
        else:
            print(f"Invalid count")
    odd.clear()
    even.clear()
    transform.clear()
    command = str(input()).split()

if command[0] == "end":
    print(numbers)
