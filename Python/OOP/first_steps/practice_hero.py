class Hero:
    def __init__(self, _name: str, _health: int) -> None:
        self.name = _name
        self.health = int(_health)

    def defend(self, _damage: int):
        self.health -= int(_damage)
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, _amount: int):
        self.health += int(_amount)


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
