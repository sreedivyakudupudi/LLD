from .idle_state import IdleState
from .vending_state import VendingState
class ItemSelectedState(VendingState):

    def insert_money(self, machine, amount):
        machine.balance += amount

    def select_item(self, machine, item_id):
        print("Item already selected")

    def dispense(self, machine):
        from .dispensing_state import DispensingState

        item = machine.selected_item

        if machine.balance < item.price:
            print("Insufficient money")
            return

        machine.state = DispensingState()
        machine.dispense()

    def cancel(self, machine):
        print(f"Returning ₹{machine.balance}")

        machine.balance = 0
        machine.selected_item = None
        machine.state = IdleState()