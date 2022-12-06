from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(105.5, 25.5)

    def test_constructor(self):
        self.assertEqual(105.5, self.vehicle.fuel)
        self.assertEqual(105.5, self.vehicle.capacity)
        self.assertEqual(25.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_success(self):
        self.vehicle.drive(20)
        consumption = self.vehicle.fuel_consumption * 20
        self.assertEqual(self.vehicle.fuel, 105.5 - consumption)

    def test_drive_failure(self):
        with self.assertRaises(Exception) as e:
            self.vehicle.drive(200)

        self.assertEqual(str(e.exception), "Not enough fuel")

    def test_refuel_success(self):
        self.vehicle.drive(30)
        self.vehicle.refuel(30 * 1.25)
        self.assertEqual(self.vehicle.fuel, 105.5)

    def test_refuel_failure(self):
        with self.assertRaises(Exception) as e:
            self.vehicle.refuel(20)

        self.assertEqual("Too much fuel", str(e.exception))

    def test_str(self):
        self.assertEqual(
            "The vehicle has 25.5 "
            f"horse power with 105.5 fuel left and 1.25 fuel consumption",
            str(self.vehicle),
        )


if __name__ == "__main__":
    main()
