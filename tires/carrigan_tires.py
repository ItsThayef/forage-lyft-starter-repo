from abc import ABC
from datetime import date
from car import Car

class CarriganTires(Car, ABC):
    def __init__(self, last_service_date, sensor):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        sensor = [0,0,0,0]
        self.sensor = sensor

        # maybe add valueError for length and typeError of sensor array

    def needs_service(self):
        if sensor[0] or sensor[1] or sensor[2] or sensor[3] >= 0.9:
            return True
        else:
            return False