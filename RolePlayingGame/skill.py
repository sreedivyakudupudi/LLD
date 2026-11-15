class Skill:
    def __init__(self, name, level, damage_multiplier=1.0, cooldown=0):
        self.name = name
        self.level = level
        self.damage_multiplier = damage_multiplier
        self.cooldown = cooldown

    def __str__(self):
        return f"{self.name} (Level {self.level})"

    #Setters
    def set_name(self, name):
        self.name = name

    def set_level(self, level):
        self.level = level

    def set_damage_multiplier(self, damage_multiplier):
        self.damage_multiplier = damage_multiplier

    def set_cooldown(self, cooldown):
        self.cooldown = cooldown

    #Getters
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_damage_multiplier(self):
        return self.damage_multiplier

    def get_cooldown(self):
        return self.cooldown

    