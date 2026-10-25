from .fare_stratergy import FareStratergy
from decimal import Decimal

class BasicStratergy(FareStratergy):

    SMALL_VEHICLE_RATE = Decimal("1.0")
    MEDIUM_VEHICLE_RATE = Decimal("2.0")
    LARGE_VEHICLE_RATE = Decimal("3.0") 

    def calculate_fare(self, ticket, input_fare):
        vehicle_size = ticket.get_vehicle().get_size()

        duration = ticket.get_duration()

        if vehicle_size == vehicle_size.SMALL:
            rate = self.SMALL_VEHICLE_RATE

        if vehicle_size == vehicle_size.MEDIUM:
            rate = self.MEDIUM_VEHICLE_RATE

        if vehicle_size == vehicle_size.LARGE:
            rate = self.LARGE_VEHICLE_RATE

        fare = (rate * duration) + input_fare

        return fare



        
