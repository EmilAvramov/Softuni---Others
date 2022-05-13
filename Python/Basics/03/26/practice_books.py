fav_book = str(input())
current_book = str(input())
count = 0

while current_book != "No More Books":
    if fav_book != current_book:
        count += 1
    else:
        print(f'You checked {count} books and found it.')
        break
    current_book = str(input())

if current_book == "No More Books":
    print(f'The book you search is not here!', end='\n')
    print(f'You checked {count} books.')
