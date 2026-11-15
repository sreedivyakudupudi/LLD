class Weapon:
    def __init__(self, name, damage, weight, weapon_type, durability):
        self.__name = name
        self.__damage = damage
        self.__weight = weight
        self.__weapon_type = weapon_type
        self.__durability = durability

    # Setters with validation
    def set_name(self, name):
        if not name:
            raise ValueError("Weapon name cannot be empty")
        self.__name = name

    def set_damage(self, damage):
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        self.__damage = damage

    def set_weight(self, weight):
        if weight <= 0:
            raise ValueError("Weight must be positive")
        self.__weight = weight

    def set_weapon_type(self, weapon_type):
        self.__weapon_type = weapon_type

    def set_durability(self, durability):
        if durability < 0:
            raise ValueError("Durability cannot be negative")
        self.__durability = durability

    # Getters
    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def get_weight(self):
        return self.__weight

    def get_weapon_type(self):
        return self.__weapon_type

    def get_durability(self):
        return self.__durability