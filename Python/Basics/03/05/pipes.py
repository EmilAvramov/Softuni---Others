volume = float(input())
debit_1 = float(input())
debit_2 = float(input())
hours = float(input())

interim_debit_1 = debit_1 * hours
interim_debit_2 = debit_2 * hours
total_inflow = (debit_1 + debit_2) * hours
total_filled = (total_inflow / volume) * 100
debit_1_filled = (interim_debit_1 / total_inflow) * 100
debit_2_filled = (interim_debit_2 / total_inflow) * 100
extra_flow = total_inflow - volume

if total_inflow <= volume:
    print(f'The pool is {total_filled:.2f}% full. Pipe 1: {debit_1_filled:.2f}%. Pipe 2: {debit_2_filled:.2f}%.')
else:
    print(f'For {hours} hours the pool overflows with {extra_flow} liters.')