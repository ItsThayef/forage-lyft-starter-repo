import unittest
from datetime import date
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_should_be_replaced(self):
        last_service_date = date.today()
        current_mileage = 30001
        last_service_milage = 0

        engine = CapuletEngine(last_service_date, current_mileage, last_service_milage)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_shoul_not_be_replaced(self):
        last_service_date = date.today()
        current_mileage = 29000
        last_service_milage = 0

        engine = CapuletEngine(last_service_date, current_mileage, last_service_milage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
