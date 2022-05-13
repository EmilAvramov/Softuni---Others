class Party:
    people = []


command = str(input())

while command != "End":
    Party.people.append(command)
    command = str(input())

print(f'Going: {", ".join(Party.people)}')
print(f'Total: {len(Party.people)}')