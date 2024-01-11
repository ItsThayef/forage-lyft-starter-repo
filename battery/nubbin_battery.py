from abc import ABC
from datetime import date
from car import Car
class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date

    def needs_service(self):
        x = date.today() - self.last_service_date
        return (x.days/365) >= 4