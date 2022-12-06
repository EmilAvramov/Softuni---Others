from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Test", "Type Test", "Sound Test")

    def test_constructor(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Type Test", self.mammal.type)
        self.assertEqual("Sound Test", self.mammal.sound)

    def test_sound(self):
        self.assertEqual("Test makes Sound Test", self.mammal.make_sound())

    def test_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual('Test is of type Type Test', self.mammal.info())


if __name__ == "__main__":
    main()
