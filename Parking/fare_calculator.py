from decimal import Decimal
from typing import List

from Fare.fare_stratergy import FareStratergy
from ticket import Ticket


class FareCalculator:

    def __init__(
        self,
        fare_strategies: List[FareStratergy]
    ):

        self.fare_strategies = fare_strategies

    def calculate_fare(
        self,
        ticket: Ticket
    ) -> Decimal:

        fare = Decimal("0")

        for strategy in self.fare_strategies:

            fare = strategy.calculate_fare(
                ticket,
                fare
            )

        return fare