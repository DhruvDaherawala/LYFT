from abc import ABC
from engine import Engine

class CapuletEngine(Engine, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.service_miles = 30000
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.service_miles = service_miles

    def needs_service(self):
        if self.current_mileage - self.last_service_mileage < service_miles:
            return True
        else:
            return False
