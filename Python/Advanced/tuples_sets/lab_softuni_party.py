regex = r"\d"

num_guests = int(input())
regulars = set()
vips = set()

for guest in range(num_guests):
    code = input()
    if code.startswith(regex):
        vips.add(code)
    else:
        regulars.add(code)

incoming = input()

while incoming != "END":
    if incoming in regulars:
        regulars.discard(incoming)
    elif incoming in vips:
        vips.discard(incoming)
    incoming = input()

print(f"{len(regulars) + len(vips)}")
for guest in sorted(vips):
    print(f"{guest}")
for guest in sorted(regulars):
    print(f"{guest}")
