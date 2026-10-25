from .vending_state import VendingState

class IdleState(VendingState):

    def insert_money(self, machine, amount):
        from .money_inserted_state import MoneyInsertedState
        machine.balance += amount
        machine.state = MoneyInsertedState()
        print(f"Inserted ₹{amount}")

    def select_item(self, machine, item_id):
        print("Please insert money first")

    def dispense(self, machine):
        print("Please select an item first")

    def cancel(self, machine):
        print("No transaction to cancel")