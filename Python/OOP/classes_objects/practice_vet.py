class Vet:
    animals = []
    space = 5

    def __init__(self, _name: str) -> None:
        self.name = _name
        self.animals = []

    def register_animal(self, _animal_name: str):
        if Vet.space > 0:
            Vet.animals.append(_animal_name)
            Vet.space -= 1
            self.animals.append(_animal_name)
            return f"{_animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, _animal_name: str):
        if _animal_name in Vet.animals:
            Vet.animals.remove(_animal_name)
            Vet.space += 1
            self.animals.remove(_animal_name)
            return f"{_animal_name} unregistered successfully"
        else:
            return f"{_animal_name} not in the clinic"

    def info(self):
        return (
            f"{self.name} has {len(self.animals)} animals. {Vet.space} space"
            f" left in clinic"
        )


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
