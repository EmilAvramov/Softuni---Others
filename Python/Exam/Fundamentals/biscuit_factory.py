from math import floor

bis_per_worker = int(input())
workers = int(input())
compete_30 = int(input())
own_30 = 0

for i in range(30):
    if i % 3 != 0:
        own_30 += bis_per_worker * workers
    else:
        own_30 += floor(bis_per_worker * workers * 0.75)

print(f"You have produced {own_30} biscuits for the past month.")
if own_30 > compete_30:
    print(
        f"You produce {(((own_30 - compete_30)/compete_30) * 100):.2f} percent more biscuits."
    )
else:
    print(
        f"You produce {(((compete_30 - own_30)/compete_30) * 100):.2f} percent less biscuits."
    )
