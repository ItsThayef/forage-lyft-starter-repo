import unittest
from datetime import date
from tires.carrigan_tires import CarriganTires
class TestCarriganTires(unittest.TestCase):
    def test_carrigan_tires_should_be_replaced(self):
        last_service_date = date.today()
        sensor = [0.5, 0.9, 0.1, 0.4]

        tires = CarriganTires(last_service_date, sensor)
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_should_not_be_replaced(self):
        last_service_date = date.today()
        sensor = [0.5, 0.1, 0.1, 0.4]

        tires = CarriganTires(last_service_date, sensor)
        self.assertFlase(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
