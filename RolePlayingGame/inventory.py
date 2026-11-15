import copy
class Inventory:
    def __init__(self):
        self.__items = {}

    def add_item(self, item, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        name = item.get_name()

        if name in self.__items:
            existing_item = self.__items[name]

            if existing_item.get_category() != item.get_category():
                raise ValueError("Item category mismatch.")

            existing_item.update_quantity(quantity)
        else:
            item.set_quantity(quantity)
            self.__items[name] = item


    def remove_item(self, item_name, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity to remove must be positive.")
        if item_name in self.__items:
            item = self.__items[item_name]
            if item.get_quantity() >= quantity:
                item.update_quantity(-quantity)
                if item.get_quantity() == 0:
                    del self.__items[item_name]
            else:
                raise ValueError(f"Not enough {item_name} in inventory to remove.")
        else:
            raise ValueError(f"{item_name} not found in inventory.")


    def update_quantity(self, item_name, new_quantity):
        if new_quantity < 0:
            raise ValueError("New quantity cannot be negative.")
        if item_name in self.__items:
            item = self.__items[item_name]
            item.set_quantity(new_quantity)
            if new_quantity == 0:
                del self.__items[item_name]
        else:
            raise ValueError(f"{item_name} not found in inventory.")

    def get_item(self, item_name):
        if item_name not in self.__items:
            raise ValueError(f"{item_name} not found.")

        return copy.deepcopy(self.__items[item_name])

    def list_items(self):
        return copy.deepcopy(list(self.__items.values()))

    def display_inventory(self):
        if not self.__items:
            print("Inventory is empty.")
            return

        print("Inventory Items:")
        print("----------------")
        print("Name\tCategory\tQuantity")
        for item in self.__items.values():
            print(f"{item.get_name()}\t{item.get_category()}\t{item.get_quantity()}")