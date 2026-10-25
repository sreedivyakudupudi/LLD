from abc import ABC, abstractmethod
from typing import Optional

from enums import VehicleSize
from vehicle import Vehicle


class ParkingSpot(ABC):

    def __init__(self, spot_number: int):
        self.spot_number = spot_number
        self.vehicle: Optional[Vehicle] = None

    def is_available(self) -> bool:
        return self.vehicle is None

    def occupy(self, vehicle: Vehicle) -> None:

        if not self.is_available():
            raise ValueError(
                f"Parking spot {self.spot_number} is already occupied"
            )

        self.vehicle = vehicle

    def vacate(self) -> None:
        self.vehicle = None

    def get_spot_number(self) -> int:
        return self.spot_number

    @abstractmethod
    def get_size(self) -> VehicleSize:
        pass

