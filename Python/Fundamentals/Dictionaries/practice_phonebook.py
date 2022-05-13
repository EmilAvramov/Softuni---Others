contact_book = {}

entry = input().split("-")

while entry[0].isdigit() is False:
    contact_book[entry[0]] = entry[1]
    entry = input().split("-")

for i in range(int(entry[0])):
    search = input()
    if search in contact_book.keys():
        print(f"{search} -> {contact_book[search]}")
    else:
        print(f"Contact {search} does not exist.")
