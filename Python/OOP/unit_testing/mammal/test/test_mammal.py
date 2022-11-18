import unittest
from project.mammal import Mammal

class MammalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("rhino", "herbivore", "ghruuu")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_sound(self):
        self.assertEqual(self.mammal.make_sound(), "rhino makes ghruuu")

    def test_info(self):
        self.assertEqual(self.mammal.info(), "rhino is of type herbivore")


if __name__ == "__main__":
    unittest.main()
