length = float(input())
width = float(input())
height = float(input())
wasted_space = float(input())
volume_total = float((length * width * height)/1000)
volume_wasted = volume_total * (wasted_space / 100)
clean_volume = volume_total - volume_wasted
print(clean_volume)
