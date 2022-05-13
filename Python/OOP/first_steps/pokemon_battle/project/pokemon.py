class Pokemon:
    def __init__(self, _name: str, _health: int) -> None:
        self.name = _name
        self.health = _health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"
