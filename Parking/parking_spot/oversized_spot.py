from enums import VehicleSize
from .Basic_parking_spot import ParkingSpot

class OverSizedSpot(ParkingSpot):

    def get_size(self) -> VehicleSize:
        return VehicleSize.LARGE