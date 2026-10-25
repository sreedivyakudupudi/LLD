from .fare_stratergy import FareStratergy
from decimal import Decimal

class PeakHoursFareStratergy(FareStratergy):
    PEAK_HOURS_MULTIPLIER = Decimal("1.5")

    def calculate_fare(self, ticket, input_fare):
        if self.is_peak_hour(ticket.get_start_time()):
            return input_fare * self.PEAK_HOURS_MULTIPLIER


    def is_peak_hour(self, entry_time):
        hour = entry_time.hour
        morning_peak = 7 <= hour <= 10
        evening_peak = 16 <= hour <= 19

        return morning_peak or evening_peak
