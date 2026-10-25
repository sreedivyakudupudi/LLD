from datetime import datetime
from decimal import Decimal
from typing import Dict, Optional
import uuid

from vehicle import Vehicle
from ticket import Ticket
from parking_manager import ParkingManager
from fare_calculator import FareCalculator


class ParkingLot:

    def __init__(
        self,
        parking_manager: ParkingManager,
        fare_calculator: FareCalculator
    ):

        self.parking_manager = parking_manager
        self.fare_calculator = fare_calculator

        # Ticket ID -> Ticket
        self.active_tickets: Dict[str, Ticket] = {}

    # ---------------------------------------------------------
    # Vehicle Entry
    # ---------------------------------------------------------

    def enter_vehicle(
        self,
        vehicle: Vehicle
    ) -> Optional[Ticket]:

        # Ask ParkingManager to find and assign spot.

        spot = self.parking_manager.park_vehicle(
            vehicle
        )

        if spot is None:

            print(
                f"No parking spot available for "
                f"{vehicle.get_license_plate()}"
            )

            return None

        # Generate ticket.

        ticket_id = str(uuid.uuid4())

        ticket = Ticket(
            ticket_id=ticket_id,
            vehicle=vehicle,
            parking_spot=spot,
            start_time=datetime.now()
        )

        self.active_tickets[
            ticket_id
        ] = ticket

        print(
            f"Vehicle {vehicle.get_license_plate()} "
            f"parked at spot "
            f"{spot.get_spot_number()}"
        )

        print(
            f"Ticket ID: {ticket_id}"
        )

        return ticket

    # ---------------------------------------------------------
    # Vehicle Exit
    # ---------------------------------------------------------

    def leave_vehicle(
        self,
        ticket: Ticket
    ) -> Decimal:

        if ticket is None:

            raise ValueError(
                "Invalid ticket"
            )

        if ticket.get_end_time() is not None:

            raise ValueError(
                "Vehicle has already exited"
            )

        # Set exit time.

        ticket.set_end_time(
            datetime.now()
        )

        # Calculate fare.

        fare = self.fare_calculator.calculate_fare(
            ticket
        )

        # Free parking spot.

        self.parking_manager.unpark_vehicle(
            ticket.get_vehicle()
        )

        # Remove active ticket.

        self.active_tickets.pop(
            ticket.ticket_id,
            None
        )

        print(
            f"Vehicle "
            f"{ticket.get_vehicle().get_license_plate()} "
            f"has left the parking lot"
        )

        print(
            f"Parking duration: "
            f"{ticket.get_duration():.2f} "
            f"minutes"
        )

        print(
            f"Total fare: ₹{fare:.2f}"
        )

        return fare