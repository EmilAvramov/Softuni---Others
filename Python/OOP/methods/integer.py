from math import floor


class Integer:
    def __init__(self, _value: int) -> None:
        self.value = _value

    @classmethod
    def from_float(cls, _float_value: float):
        if isinstance(_float_value, float) is False:
            return "value is not a float"
        else:
            return Integer(floor(_float_value))

    @classmethod
    def from_roman(cls, _value):
        romans = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        result = 0
        for i in range(len(_value)):
            number = romans[_value[i]]
            if i + 1 < len(_value) and romans[_value[i + 1]] > number:
                result -= number
            else:
                result += number
        return Integer(result)

    @classmethod
    def from_string(cls, _value):
        if isinstance(_value, str) is False:
            return "wrong type"
        else:
            return Integer(int(_value))


import unittest


class IntegerTests(unittest.TestCase):
    def test_basic_init(self):
        integer = Integer(1)
        self.assertEqual(integer.value, 1)

    def test_from_float_success(self):
        integer = Integer.from_float(2.5)
        self.assertEqual(integer.value, 2)

    def test_from_float_wrong_type(self):
        result = Integer.from_float("2.5")
        self.assertEqual(result, "value is not a float")

    def test_from_roman(self):
        integer = Integer.from_roman("XIX")
        self.assertEqual(integer.value, 19)

    def test_from_string_success(self):
        integer = Integer.from_string("10")
        self.assertEqual(integer.value, 10)

    def test_from_string_wrong_type(self):
        result = Integer.from_string(1.5)
        self.assertEqual(result, "wrong type")


if __name__ == "__main__":
    unittest.main()
