class Inventory:

    def __init__(self, items):
        self.items = {}

        for item in items:
            self.items[item.get_id()] = item

    def is_available(self, item_id):
        if item_id not in self.items:
            return False

        return self.items[item_id].get_quantity() > 0

    def get_item(self, item_id):
        return self.items.get(item_id)

    def update_quantity(self, item_id, new_quantity):
        if item_id in self.items:
            self.items[item_id].set_quantity(new_quantity)

    def add_item(self, item):
        self.items[item.get_id()] = item

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]

    def get_all_items(self):
        return self.items.values()