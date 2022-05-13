weather_data = float(input())
if 26.00 <= weather_data <= 35.00:
    print("Hot")
elif 20.1 <= weather_data <= 25.9:
    print("Warm")
elif 15 <= weather_data <= 20:
    print("Mild")
elif 12 <= weather_data <= 14.9:
    print("Cool")
elif 5 <= weather_data <= 11.9:
    print("Cold")
else:
    print("unknown")
