class Vehicle:
    def __init__(self, _mileage: int, _speed=150) -> None:
        self.mileage = _mileage
        self.max_speed = _speed
        self.gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append("Hudly Wireless")
print(car.gadgets)
