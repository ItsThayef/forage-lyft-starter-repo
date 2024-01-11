from abc import ABC
from datetime import date
from car import Car


class OctoprimeTires(Car, ABC):
    def __init__(self, last_service_date, sensor):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.sensor = sensor

        # maybe add valueError for length and typeError of sensor array

    def needs_service(self):
        if sum(sensor) >= 3:
            return True
        else:
            return False