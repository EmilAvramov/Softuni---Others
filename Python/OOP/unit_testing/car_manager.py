class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(2008, "Skoda", 20, 2000)

    def tearDown(self) -> None:
        self.car.fuel_amount = 0

    def test_constructor(self):
        self.assertEqual(self.car.make, 2008)
        self.assertEqual(self.car.model, "Skoda")
        self.assertEqual(self.car.fuel_consumption, 20)
        self.assertEqual(self.car.fuel_capacity, 2000)

    def test_make_setter_getter(self):
        self.assertRaises(Exception, self.car.make, "")
        self.car.make = 2000
        self.assertEqual(self.car.make, 2000)

    def test_model_setter_getter(self):
        self.assertRaises(Exception, self.car.model, "")
        self.car.model = "Audi"
        self.assertEqual(self.car.model, "Audi")

    def test_consumption_setter_getter(self):
        self.assertRaises(Exception, self.car.fuel_consumption, -1)
        self.assertRaises(Exception, self.car.fuel_consumption, 0)
        self.car.fuel_consumption = 200
        self.assertEqual(self.car.fuel_consumption, 200)

    def test_capacity_setter_getter(self):
        self.assertRaises(Exception, self.car.fuel_capacity, -1)
        self.assertRaises(Exception, self.car.fuel_capacity, 0)
        self.car.fuel_capacity = 20000
        self.assertEqual(self.car.fuel_capacity, 20000)

    def test_amount_setter_getter(self):
        self.assertRaises(Exception, self.car.fuel_amount, -1)
        self.assertRaises(Exception, self.car.fuel_amount, 0)
        self.car.fuel_amount = 1000
        self.assertEqual(self.car.fuel_amount, 1000)

    def test_refuel(self):
        self.assertRaises(Exception, self.car.refuel, 0)
        self.assertRaises(Exception, self.car.refuel, -1)
        self.car.refuel(200)
        self.assertEqual(self.car.fuel_amount, 200)
        self.car.refuel(5000)
        self.assertEqual(self.car.fuel_amount, 2000)

    def test_drive(self):
        self.assertRaises(Exception, self.car.drive, 1)
        self.car.refuel(20)
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 0)


if __name__ == "__main__":
    unittest.main()
