from typing import Dict, List, Optional

from enums import VehicleSize
from vehicle import Vehicle
from parking_spot.Basic_parking_spot import ParkingSpot


class ParkingManager:

    def __init__(
        self,
        available_spots: Dict[VehicleSize, List[ParkingSpot]]
    ):

        self.available_spots = available_spots

        # Vehicle license plate -> ParkingSpot
        self.vehicle_to_spot_map: Dict[str, ParkingSpot] = {}

        # Spot number -> Vehicle
        self.spot_to_vehicle_map: Dict[int, Vehicle] = {}

    # ---------------------------------------------------------
    # Find a suitable parking spot
    # ---------------------------------------------------------

    def find_spot_for_vehicle(
        self,
        vehicle: Vehicle
    ) -> Optional[ParkingSpot]:

        vehicle_size = vehicle.get_size()

        # Find the smallest spot that can accommodate
        # the vehicle.

        for size in VehicleSize:

            if size.value >= vehicle_size.value:

                spots = self.available_spots.get(size, [])

                for spot in spots:

                    if spot.is_available():
                        return spot

        return None

    # ---------------------------------------------------------
    # Park vehicle
    # ---------------------------------------------------------

    def park_vehicle(
        self,
        vehicle: Vehicle
    ) -> Optional[ParkingSpot]:

        license_plate = vehicle.get_license_plate()

        # Don't allow the same vehicle to park twice.

        if license_plate in self.vehicle_to_spot_map:

            raise ValueError(
                f"Vehicle {license_plate} is already parked"
            )

        spot = self.find_spot_for_vehicle(vehicle)

        if spot is None:
            return None

        # Occupy the spot.

        spot.occupy(vehicle)

        # Vehicle -> Spot
        self.vehicle_to_spot_map[license_plate] = spot

        # Spot -> Vehicle
        self.spot_to_vehicle_map[
            spot.get_spot_number()
        ] = vehicle

        # Remove the spot from available spots.

        self.available_spots[
            spot.get_size()
        ].remove(spot)

        return spot

    # ---------------------------------------------------------
    # Unpark vehicle
    # ---------------------------------------------------------

    def unpark_vehicle(
        self,
        vehicle: Vehicle
    ) -> None:

        license_plate = vehicle.get_license_plate()

        spot = self.vehicle_to_spot_map.pop(
            license_plate,
            None
        )

        if spot is None:

            raise ValueError(
                f"Vehicle {license_plate} is not parked"
            )

        # Remove reverse mapping.

        self.spot_to_vehicle_map.pop(
            spot.get_spot_number(),
            None
        )

        # Free the spot.

        spot.vacate()

        # Add it back to available spots.

        self.available_spots[
            spot.get_size()
        ].append(spot)

    # ---------------------------------------------------------
    # Find spot using vehicle
    # ---------------------------------------------------------

    def find_spot_by_vehicle(
        self,
        vehicle: Vehicle
    ) -> Optional[ParkingSpot]:

        return self.vehicle_to_spot_map.get(
            vehicle.get_license_plate()
        )

    # ---------------------------------------------------------
    # Find vehicle using spot
    # ---------------------------------------------------------

    def find_vehicle_by_spot(
        self,
        spot: ParkingSpot
    ) -> Optional[Vehicle]:

        return self.spot_to_vehicle_map.get(
            spot.get_spot_number()
        )