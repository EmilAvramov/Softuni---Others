total_detergent = int(input()) * 750
initial_input = input()

times_counter = 0
washed_plates = 0
washed_saucepan = 0
remaining_detergent = total_detergent
insufficient_counter = 0

while initial_input != "End":
    times_counter += 1
    num_dishes = int(initial_input)
    if times_counter % 3 == 0:
        if remaining_detergent >= num_dishes * 15:
            washed_saucepan += num_dishes
            remaining_detergent -= num_dishes * 15
        else:
            print(f'Not enough detergent, {abs(num_dishes * 15 - remaining_detergent)} ml. more necessary!')
            insufficient_counter += 1
            break
    else:
        if remaining_detergent >= num_dishes * 5:
            washed_plates += num_dishes
            remaining_detergent -= num_dishes * 5
        else:
            print(f'Not enough detergent, {abs(num_dishes * 5 - remaining_detergent)} ml. more necessary!')
            insufficient_counter += 1
            break
    initial_input = input()

if insufficient_counter == 0:
    print(f'Detergent was enough!', end='\n')
    print(f'{washed_plates} dishes and {washed_saucepan} pots were washed.', end='\n')
    print(f'Leftover detergent {remaining_detergent} ml.')