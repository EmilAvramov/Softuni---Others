time = [int(i) for i in input().split(":")]
secs = [3600, 60, 1]

steps = int(input())
time_steps = int(input())

total_secs = sum([a * b for a, b in zip(secs, time)])
summed = total_secs + steps * time_steps

hours = summed // 3600
if hours > 24:
    hours = hours % 24
if hours == 24:
    hours = 0
minutes = (summed % 3600) // 60
seconds = ((summed % 3600) % 60) % 60

print(f"Time Arrival: {hours:02}:{minutes:02}:{seconds:02}")
