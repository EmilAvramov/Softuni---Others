budget = float(input())
flour_kg = float(input())

recipe = flour_kg + flour_kg * 0.75 + (flour_kg * 1.25) / 4
instances = int(budget // recipe)
leftover_budget = float(budget % recipe)
colored_eggs = 0
bread_count = 0

for count in range(1, instances + 1):
    colored_eggs += 3
    bread_count += 1
    if count % 3 == 0:
        colored_eggs -= count - 2

print(f'You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and '
      f'{leftover_budget:.2f}BGN left.')
