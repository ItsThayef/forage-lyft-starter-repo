import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_should_be_replaced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(last_service_date, 0, 0)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_replaced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 2)

        battery = SpindlerBattery(last_service_date, 0, 0)
        self.assertFalse(battery.needs_service())

    # There is an error if you consider the months and/or days as well as the year. The date time function
    # cannot compute going back before Jan (month 1); it cannot cycle back through the years. This can be
    # fixed by writing the code in a similar style to how we wrote the function which checks whether the
    # battery needs service.

    # Changed years before service from 2 -> 3

if __name__ == '__main__':
    unittest.main()
