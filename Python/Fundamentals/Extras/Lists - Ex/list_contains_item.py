list_numbers = [int(i) for i in input().split()]
search = int(input())

if search in list_numbers:
    print("yes")
else:
    print("no")