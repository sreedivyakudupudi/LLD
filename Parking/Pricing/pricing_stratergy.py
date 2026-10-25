from abc import ABC, abstractmethod

class PricingStratergy(ABC):
    @abstractmethod
    def calculate_fees(self, session):
        pass
