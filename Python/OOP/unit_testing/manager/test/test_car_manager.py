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
