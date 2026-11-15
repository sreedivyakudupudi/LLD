class InventoryItem:
    VALID_CATEGORIES = {"Potion", "Armor", "Special"}

    def __init__(self, name, category, quantity=1):
        if not name or not name.strip():
            raise ValueError("Item name cannot be empty.")

        if category not in self.VALID_CATEGORIES:
            raise ValueError("Invalid item category.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.__name = name
        self.__category = category
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def update_quantity(self, count):
        if self.__quantity + count < 0:
            raise ValueError("Resulting quantity cannot be negative.")
        self.__quantity += count

    def get_category(self):
        return self.__category

    