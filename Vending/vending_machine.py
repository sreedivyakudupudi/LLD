from item import Item
from Inventory import Inventory
from States.idle_state import IdleState


class VendingMachine:

    def __init__(self, inventory: Inventory):
        self.balance = 0
        self.inventory = inventory
        self.state = IdleState()

    def insert_item(self, item_id, name, price, quantity):
        item = Item(item_id, name, price, quantity)
        self.inventory.add_item(item)

    def insert_money(self, amount):
        self.state.insert_money(self, amount)

    def select_item(self, item_id):
        self.state.select_item(self, item_id)

    def dispense(self):
        self.state.dispense(self)

    def cancel(self):
        self.state.cancel(self)

    def show_all_items(self):
        for item in self.inventory.get_all_items():
            print(
                item.get_id(),
                item.get_name(),
                item.get_price(),
                item.get_quantity()
            )