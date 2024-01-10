from abc import ABC
from datetime import date
from car import Car
class NubbinBattery(Car, ABC):

    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        return (date.today() - self.last_service_date)/365 < 24