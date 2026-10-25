from enums import VehicleSize

from bike import Bike
from car import Car
from truck import Truck

from parking_spot.compact_spot import CompactSpot
from parking_spot.oversized_spot import OverSizedSpot
from parking_spot.regular_spot import RegularSpot

from parking_manager import ParkingManager

from Fare.base_stratergy import BasicStratergy
from Fare.fare_stratergy import FareStratergy
from Fare.peak_fare_stratergy import PeakHoursFareStratergy
from Fare.weekend_stratergy import WeekendFareStrategy

from fare_calculator import FareCalculator

from parking_lot import ParkingLot


def create_parking_lot() -> ParkingLot:

    # ---------------------------------------------------------
    # Create parking spots
    # ---------------------------------------------------------

    small_spots = [
        CompactSpot(1),
        CompactSpot(2),
        CompactSpot(3)
    ]

    medium_spots = [
        RegularSpot(4),
        RegularSpot(5),
        RegularSpot(6)
    ]

    large_spots = [
        OverSizedSpot(7),
        OverSizedSpot(8)
    ]

    # ---------------------------------------------------------
    # Group spots by size
    # ---------------------------------------------------------

    available_spots = {

        VehicleSize.SMALL:
            small_spots,

        VehicleSize.MEDIUM:
            medium_spots,

        VehicleSize.LARGE:
            large_spots
    }

    # ---------------------------------------------------------
    # Create ParkingManager
    # ---------------------------------------------------------

    parking_manager = ParkingManager(
        available_spots
    )

    # ---------------------------------------------------------
    # Create Fare Strategies
    # ---------------------------------------------------------

    fare_strategies = [

        BasicStratergy(),

        PeakHoursFareStratergy(),

        WeekendFareStrategy()
    ]

    # ---------------------------------------------------------
    # Create FareCalculator
    # ---------------------------------------------------------

    fare_calculator = FareCalculator(
        fare_strategies
    )

    # ---------------------------------------------------------
    # Create ParkingLot
    # ---------------------------------------------------------

    parking_lot = ParkingLot(
        parking_manager,
        fare_calculator
    )

    return parking_lot


def main():

    # =========================================================
    # Create Parking Lot
    # =========================================================

    parking_lot = create_parking_lot()

    # =========================================================
    # Create Vehicles
    # =========================================================

    bike = Bike(
        "AP01AB1234"
    )

    car = Car(
        "AP02CD5678"
    )

    truck = Truck(
        "AP03EF9012"
    )

    # =========================================================
    # Vehicle Entry
    # =========================================================

    print("\n========== VEHICLE ENTRY ==========\n")

    bike_ticket = parking_lot.enter_vehicle(
        bike
    )

    car_ticket = parking_lot.enter_vehicle(
        car
    )

    truck_ticket = parking_lot.enter_vehicle(
        truck
    )

    # =========================================================
    # Display Parking Assignments
    # =========================================================

    print("\n========== PARKING ASSIGNMENTS ==========\n")

    if bike_ticket:

        print(
            f"Bike {bike.get_license_plate()} "
            f"-> Spot "
            f"{bike_ticket.parking_spot.get_spot_number()}"
        )

    if car_ticket:

        print(
            f"Car {car.get_license_plate()} "
            f"-> Spot "
            f"{car_ticket.parking_spot.get_spot_number()}"
        )

    if truck_ticket:

        print(
            f"Truck {truck.get_license_plate()} "
            f"-> Spot "
            f"{truck_ticket.parking_spot.get_spot_number()}"
        )

    # =========================================================
    # Vehicle Exit
    # =========================================================

    print("\n========== VEHICLE EXIT ==========\n")

    if bike_ticket:

        print("Bike exiting...")

        parking_lot.leave_vehicle(
            bike_ticket
        )

    if car_ticket:

        print("\nCar exiting...")

        parking_lot.leave_vehicle(
            car_ticket
        )

    # =========================================================
    # Available Spots
    # =========================================================

    print(
        "\n========== AVAILABLE SPOTS ==========\n"
    )

    for size, spots in (
        parking_lot
        .parking_manager
        .available_spots
        .items()
    ):

        print(
            f"{size.name}: "
            f"{len(spots)} spots available"
        )


if __name__ == "__main__":
    main()