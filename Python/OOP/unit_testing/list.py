import unittest


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


class IntegerListTestCase(unittest.TestCase):
    def test_data_type_correct(self):
        self.integer_list = IntegerList(1, 2, 3)
        self.assertIsInstance(
            self.integer_list.get_data(), list, "Incorrect type"
        )

    def test_data_type_incorrect(self):
        self.integer_list = IntegerList("string", "string")
        self.assertEqual(
            len(self.integer_list.get_data()), 0, "Incorrect type"
        )

    def test_assignment(self):
        with self.assertRaises(AttributeError) as cm:
            self.integer_list.__data = [1, 2]
        exception = cm.exception
        self.assertIsNot(exception, "")

    def test_add(self):
        self.integer_list = IntegerList(1, 2, 3)
        self.assertRaises(ValueError, self.integer_list.add, "1")
        self.integer_list.add(4)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3, 4])

    def test_remove_index(self):
        self.integer_list = IntegerList(1, 2, 3)
        self.assertRaises(IndexError, self.integer_list.remove_index, 3)


if __name__ == "__main__":
    unittest.main()
