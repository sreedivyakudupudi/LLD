from .fare_stratergy import FareStratergy
from decimal import Decimal
from ticket import Ticket

class WeekendFareStrategy(FareStratergy):

    WEEKEND_MULTIPLIER = Decimal("1.2")

    def calculate_fare(
        self,
        ticket: Ticket,
        input_fare: Decimal
    ) -> Decimal:

        day = ticket.get_start_time().weekday()

        # Saturday = 5
        # Sunday = 6

        if day == 5 or day == 6:

            return (
                input_fare
                * self.WEEKEND_MULTIPLIER
            )

        return input_fare