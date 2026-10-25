from vehicle import Vehicle
from enums import VehicleSize

class Truck(Vehicle):

    def get_size(self) -> VehicleSize:
        return VehicleSize.LARGE