from abc import ABC, abstractmethod
from ticket import Ticket

class FareStratergy(ABC):
    @abstractmethod
    def calculate_fare(ticket, input_fare):
        pass


