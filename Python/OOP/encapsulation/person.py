class Person:
    def __init__(self, _name: str, _age: int) -> None:
        self._Person__name = _name
        self._Person__age = _age

    def get_name(self):
        return self._Person__name

    def get_age(self):
        return self._Person__age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())
