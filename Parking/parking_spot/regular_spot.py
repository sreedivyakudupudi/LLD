from enums import VehicleSize
from .Basic_parking_spot import ParkingSpot

class RegularSpot(ParkingSpot):

    def get_size(self) -> VehicleSize:
        return VehicleSize.MEDIUM