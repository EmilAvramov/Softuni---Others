def forecast(*args):
    def sort_data(data: dict):
        sorted_sunny = {}
        sorted_cloudy = {}
        sorted_rainy = {}
        for key, value in data.items():
            if value == "Sunny" and key not in sorted_sunny.keys():
                sorted_sunny[key] = value
        for key, value in data.items():
            if value == "Cloudy" and key not in sorted_cloudy.keys():
                sorted_cloudy[key] = value
        for key, value in data.items():
            if value == "Rainy" and key not in sorted_rainy.keys():
                sorted_rainy[key] = value
        sorted_sunny = dict(sorted(sorted_sunny.items(), key=lambda x: x[0]))
        sorted_cloudy = dict(sorted(sorted_cloudy.items(), key=lambda x: x[0]))
        sorted_rainy = dict(sorted(sorted_rainy.items(), key=lambda x: x[0]))
        final_dict = {**sorted_sunny, **sorted_cloudy, **sorted_rainy}
        return final_dict

    weather_dict = {}

    for arg in args:
        location = arg[0]
        weather = arg[1]
        weather_dict[location] = weather

    sorted_weather = sort_data(weather_dict)

    return "\n".join([f"{k} - {v}" for k, v in sorted_weather.items()])


print(
    forecast(("Sofia", "Sunny"), ("London", "Cloudy"), ("New York", "Sunny"))
)
print(
    forecast(
        ("Beijing", "Sunny"),
        ("Hong Kong", "Rainy"),
        ("Tokyo", "Sunny"),
        ("Sofia", "Cloudy"),
        ("Peru", "Sunny"),
        ("Florence", "Cloudy"),
        ("Bourgas", "Sunny"),
    )
)
