from abc import ABC, abstractmethod

class VendingState(ABC):

    @abstractmethod
    def insert_money(self, machine, amount):
        pass

    @abstractmethod
    def select_item(self, machine, item_id):
        pass

    @abstractmethod
    def dispense(self, machine):
        pass

    @abstractmethod
    def cancel(self, machine):
        pass