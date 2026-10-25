from .idle_state import IdleState
from .vending_state import VendingState
class DispensingState(VendingState):

    def insert_money(self, machine, amount):
        print("Currently dispensing item")

    def select_item(self, machine, item_id):
        print("Currently dispensing item")

    def dispense(self, machine):
        item = machine.selected_item

        print(f"Dispensing {item.name}")

        machine.inventory.update_quantity(item.id, item.quantity-1)

        change = machine.balance - item.price

        if change > 0:
            print(f"Returning change: ₹{change}")

        machine.balance = 0
        machine.selected_item = None

        machine.state = IdleState()

    def cancel(self, machine):
        print("Cannot cancel while dispensing")