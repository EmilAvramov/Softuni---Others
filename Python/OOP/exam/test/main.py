from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_constructor(self):
        self.assertEqual(self.toy_store.toy_shelf["A"], None)
        self.assertEqual(self.toy_store.toy_shelf["B"], None)
        self.assertEqual(self.toy_store.toy_shelf["C"], None)
        self.assertEqual(self.toy_store.toy_shelf["D"], None)
        self.assertEqual(self.toy_store.toy_shelf["E"], None)
        self.assertEqual(self.toy_store.toy_shelf["F"], None)
        self.assertEqual(self.toy_store.toy_shelf["G"], None)

    def test_add_toy_success(self):
        self.assertEqual(
            self.toy_store.add_toy("A", "test"),
            f"Toy:test placed successfully!",
        )
        self.assertEqual(self.toy_store.toy_shelf["A"], "test")

    def test_add_toy_exception_1(self):
        with self.assertRaises(Exception) as e:
            self.toy_store.add_toy("X", "test")

        self.assertEqual(str(e.exception), "Shelf doesn't exist!")
        self.assertEqual(len(self.toy_store.toy_shelf), 7)

    def test_add_toy_exception_2(self):
        self.toy_store.add_toy("A", "test")
        with self.assertRaises(Exception) as e:
            self.toy_store.add_toy("A", "test")

        self.assertEqual(str(e.exception), "Toy is already in shelf!")
        self.assertEqual(self.toy_store.toy_shelf["A"], "test")

    def test_add_toy_exception_3(self):
        self.toy_store.add_toy("A", "test")
        with self.assertRaises(Exception) as e:
            self.toy_store.add_toy("A", "test2")

        self.assertEqual(str(e.exception), "Shelf is already taken!")
        self.assertEqual(self.toy_store.toy_shelf["A"], "test")

    def test_remove_toy_success(self):
        self.toy_store.add_toy("A", "test")
        self.assertEqual(
            self.toy_store.remove_toy("A", "test"),
            f"Remove toy:test successfully!",
        )
        self.assertEqual(self.toy_store.toy_shelf["A"], None)

    def test_remove_toy_exception_1(self):
        with self.assertRaises(Exception) as e:
            self.toy_store.remove_toy("Z", "test")

        self.assertEqual(str(e.exception), "Shelf doesn't exist!")
        self.assertEqual(len(self.toy_store.toy_shelf), 7)

    def test_remove_toy_exception_2(self):
        with self.assertRaises(Exception) as e:
            self.toy_store.remove_toy("A", "test")

        self.assertEqual(str(e.exception), "Toy in that shelf doesn't exists!")
        self.assertEqual(self.toy_store.toy_shelf["A"], None)

    def test_remove_toy_exception_3(self):
        self.toy_store.add_toy("A", "test")
        with self.assertRaises(Exception) as e:
            self.toy_store.remove_toy("A", "test2")

        self.assertEqual(str(e.exception), "Toy in that shelf doesn't exists!")
        self.assertEqual(self.toy_store.toy_shelf["A"], "test")


if __name__ == "__main__":
    main()
