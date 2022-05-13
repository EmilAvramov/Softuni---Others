class Flower:
    is_happy = False

    def __init__(self, _name: str, _water_requirements: int) -> None:
        self.name = _name
        self.water_requirements = _water_requirements

    def water(self, _qty: int):
        if _qty >= self.water_requirements:
            Flower.is_happy = True

    def status(self):
        if Flower.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
