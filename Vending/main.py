from vending_machine import VendingMachine
from Inventory import Inventory
from item import Item


def create_vending_machine():

    item1 = Item("1", "Kitkat", 2, 15)
    item2 = Item("2", "Boost", 3, 13)
    item3 = Item("3", "Oreo", 3, 14)
    item4 = Item("4", "Maggi", 1, 15)

    items_list = [item1, item2, item3, item4]

    # Inventory converts the list into a dictionary
    inventory = Inventory(items_list)

    vending_machine = VendingMachine(inventory)

    vending_machine.show_all_items()

    # Buy Kitkat
    vending_machine.insert_money(30)
    vending_machine.select_item("1")
    vending_machine.dispense()

    # Add new item
    vending_machine.insert_item(
        "6",
        "Bun",
        8,
        3
    )

    vending_machine.show_all_items()


if __name__ == "__main__":
    create_vending_machine()