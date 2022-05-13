puzzle_price = float(2.6)
t_doll_price = float(3)
plush_price = float(4.1)
minion_price = float(8.2)
truck_price = float(2)

excursion_price = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_plush = int(input())
num_minions = int(input())
num_trucks = int(input())
total_num = num_puzzles + num_dolls + num_plush + num_minions + num_trucks
summed_price = puzzle_price * num_puzzles + t_doll_price * num_dolls + \
               plush_price * num_plush + minion_price * num_minions + truck_price * num_trucks

if total_num >= 50:
    total_price = summed_price * 0.75
    final_price = total_price * 0.9
else:
    final_price = summed_price * 0.9

if final_price >= excursion_price:
    remaining_funds = final_price - excursion_price
    print(f'Yes! {remaining_funds:.2f} lv left.')
else:
    remaining_funds = abs(excursion_price - final_price)
    print(f'Not enough money! {remaining_funds:.2f} lv needed.')
