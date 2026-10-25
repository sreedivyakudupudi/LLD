from vehicle import Vehicle
from enums import VehicleSize

class Bike(Vehicle):

    def get_size(self) -> VehicleSize:
        return VehicleSize.SMALL