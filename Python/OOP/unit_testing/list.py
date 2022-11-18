class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2, 3)

    def tearDown(self) -> None:
        for i in range(len(self.integer_list.get_data())):
            self.integer_list.remove_index(0)

    def test_constructor(self):
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3])
        self.assertIsInstance(self.integer_list.get_data(), list)

    def test_data_type(self):
        self.integer_list = IntegerList("string", "string")
        self.assertEqual(len(self.integer_list.get_data()), 0)

        self.integer_list = IntegerList(1, 2, 3)
        self.assertIsInstance(self.integer_list.get_data(), list)
        self.assertEqual(len(self.integer_list.get_data()), 3)

    def test_assignment(self):
        self.assertEqual(hasattr(self.integer_list, "data"), False)
        self.assertEqual(hasattr(self.integer_list, "__data"), False)

    def test_add(self):
        self.assertRaises(ValueError, self.integer_list.add, "1")
        items = self.integer_list.add(4)
        self.assertEqual(items, [1, 2, 3, 4])

    def test_get(self):
        self.assertRaises(IndexError, self.integer_list.get, 3)
        self.assertEqual(self.integer_list.get(2), 3)

    def test_insert(self):
        self.assertRaises(IndexError, self.integer_list.insert, 4, 5)
        self.assertRaises(ValueError, self.integer_list.insert, 2, "$")

    def test_get_biggest(self):
        self.assertEqual(self.integer_list.get_biggest(), 3)

    def test_get_index(self):
        self.assertEqual(self.integer_list.get_index(1), 0)
        self.assertRaises(ValueError, self.integer_list.get_index, 5)

    def test_remove_index(self):
        self.assertRaises(IndexError, self.integer_list.remove_index, 3)
        removed = self.integer_list.remove_index(0)
        self.assertEqual(self.integer_list.get_data(), [2, 3])
        self.assertEqual(removed, 1)


if __name__ == "__main__":
    unittest.main()
