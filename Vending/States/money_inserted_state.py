from .vending_state import VendingState
from .idle_state import IdleState
from .item_selected_state import ItemSelectedState

class MoneyInsertedState(VendingState):

    def insert_money(self, machine, amount):
        machine.balance += amount
        print(f"Inserted ₹{amount}")

    def select_item(self, machine, item_id):

        if not machine.inventory.is_available(item_id):
            print("Item not available")
            return

        machine.selected_item = machine.inventory.get_item(item_id)
        machine.state = ItemSelectedState()

        print(f"Selected {machine.selected_item.name}")

    def dispense(self, machine):
        print("Please select an item first")

    def cancel(self, machine):
        print(f"Returning ₹{machine.balance}")

        machine.balance = 0
        machine.state = IdleState()