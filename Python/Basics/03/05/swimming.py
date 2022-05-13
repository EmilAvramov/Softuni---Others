import math
record_in_seconds = float(input())
own_distance = float(input())
own_time_per_meter = float(input())

base_time = own_distance * own_time_per_meter
mid_time = math.floor(own_distance / 15)
addl_time = mid_time * 12.5
total_time = base_time + addl_time
seconds_needed = abs(record_in_seconds - total_time)

if total_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
elif total_time >= record_in_seconds:
    print(f'No, he failed! He was {seconds_needed:.2f} seconds slower.')
