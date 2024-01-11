import unittest
from datetime import date
from tires.octoprime_tires import OctoprimeTires
class TestOctoprimeTires(unittest.TestCase):
    def test_ocotprime_tires_should_be_replaced(self):
        last_service_date = date.today()
        sensor = [0.8, 0.8, 0.8, 0.8]

        tires = OctoprimeTires(last_service_date, sensor)
        self.assertTrue(tires.needs_service())

    def test_ocotprime_tires_should_not_be_replaced(self):
        last_service_date = date.today()
        sensor = [0.1, 0.1, 0.1, 0.4]

        tires = OctoprimeTires(last_service_date, sensor)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()