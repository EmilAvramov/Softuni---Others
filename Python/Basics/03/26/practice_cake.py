width = int(input())
length = int(input())

cake_pieces = width * length
total_taken = 0
leftover_cake = cake_pieces

while leftover_cake > 0:
    guest_pieces = str(input())
    if guest_pieces == "STOP":
        print(f'{leftover_cake:.0f} pieces are left.')
        break
    else:
        guest_pieces_int = int(guest_pieces)
        total_taken += guest_pieces_int
        leftover_cake -= guest_pieces_int
        if leftover_cake < 0:
            print(f'No more cake left! You need {abs(leftover_cake)} pieces more.')
            break
