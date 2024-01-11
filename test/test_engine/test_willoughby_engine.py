import unittest
from datetime import date
from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine_should_be_replaced(self):
        last_service_date = date.today()
        current_mileage = 60001
        last_service_milage = 0

        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_milage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_shoul_not_be_replaced(self):
        last_service_date = date.today()
        current_mileage = 59000
        last_service_milage = 0

        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_milage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
