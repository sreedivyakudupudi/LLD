from datetime import datetime
from decimal import Decimal

class Ticket:
    def __init__(self, ticket_id, vehicle, start_time, parking_spot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.start_time = start_time
        self.parking_spot = parking_spot
        self.end_time = None

    def set_end_time(self, time):
        self.end_time = time

    # ---------------------------------------------------------
    # Calculate parking duration
    # ---------------------------------------------------------
    def get_duration(self):
        end_time = self.end_time or datetime.now()
        duration = end_time - self.start_time

        return Decimal(duration.total_seconds()/60)

    def get_vehicle(self):
        return self.vehicle

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time