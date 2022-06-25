data = input()
no_tax = 0
total = 0
tax = 0

while data != "special" and data != "regular":
    if float(data) <= 0:
        print("Invalid price!")
    else:
        no_tax += float(data)
    data = input()

if no_tax <= 0:
    print("Invalid order!")
else:
    tax = no_tax * 0.2
    total = no_tax + tax
    if data == "special":
        total = total * 0.9
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {no_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total:.2f}$")
