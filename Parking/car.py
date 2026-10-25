from vehicle import Vehicle
from enums import VehicleSize

class Car(Vehicle):

    def get_size(self) -> VehicleSize:
        return VehicleSize.MEDIUM