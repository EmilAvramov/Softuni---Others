def is_valid(_item):
    count = 0
    for char in _item:
        if char.isalnum() or (char == "_" or char == "-"):
            count += 1
    if 3 <= len(_item) <= 16 and count == len(_item):
        return True


valid_usernames = [i for i in input().split(', ') if is_valid(i)]

print(*valid_usernames, sep='\n')
