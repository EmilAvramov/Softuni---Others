last_sector_name = str(input())
first_sector_rows = int(input())
seats_uneven_row = int(input())

increment_rows = first_sector_rows
seats_even_row = seats_uneven_row + 2
uneven_seat_count = 1
even_seat_count = 1
seat_letter = ""
total_seats = 0

for sectors in range(1, ord(last_sector_name) - 63):
    for rows in range(1, increment_rows + 1):
        if rows % 2 != 0:
            for seats in range(1, seats_uneven_row + 1):
                seat_letter = chr(uneven_seat_count + 96)
                uneven_seat_count += 1
                total_seats +=1
                print(f'{(chr(sectors + 64))}{rows}{seat_letter}')
        else:
            for seats in range(1, seats_even_row + 1):
                seat_letter = chr(even_seat_count + 96)
                even_seat_count += 1
                total_seats +=1
                print(f'{(chr(sectors + 64))}{rows}{seat_letter}')
        seats = 1
        even_seat_count = 1
        uneven_seat_count = 1
    increment_rows += 1
print(total_seats)