import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_replaced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date, 0, 0)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_replaced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(last_service_date, 0, 0)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
