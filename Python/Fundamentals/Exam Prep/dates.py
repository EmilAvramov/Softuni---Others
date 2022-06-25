from datetime import datetime

date = datetime.strptime(input(), "%Y-%m-%d")
benchmark = datetime.strptime("2018-08-26", "%Y-%m-%d")

delta = date - benchmark
if delta.days - 1 > 0:
    print(f"{delta.days + 1} days left")
elif delta.days < 0:
    print("Passed")
else:
    print("Today date")
