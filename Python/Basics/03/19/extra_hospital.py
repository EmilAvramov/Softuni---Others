days = int(input())

medics = 7
unattended = 0
attended = 0

for i in range(1, days + 1):
    if i % 3 == 0 and unattended > attended:
        medics += 1
    patient = 0
    patient = int(input())
    if patient > medics:
        attended += medics
        unattended += patient - medics
    elif patient == medics:
        attended += medics
    else:
        attended += patient

print(f'Treated patients: {attended}.', end='\n')
print(f'Untreated patients: {unattended}.')