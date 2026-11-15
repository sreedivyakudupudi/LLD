import uuid
from inventory import Inventory

class Character:
    def __init__(self, name, health, strength, attack_strength, defence_strength, level, experience_points, character_type, special_ability):
        self.character_id = None
        self.name = name
        self.character_type = character_type
        self.health = health
        self.strength = strength
        self.attack_power = attack_strength
        self.defence_power = defence_strength
        self.level = level
        self.experience = experience_points
        self.skills = []
        self.special_ability = special_ability
        self.weapons = []
        self.inventory = Inventory()

        
    #Getters and Setters
    def set_id(self, character_id):
        self.character_id = character_id

    def get_id(self):
        return self.character_id
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_character_type(self):
        return self.character_type

    def set_character_type(self, character_type):
        self.character_type = character_type

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    def get_attack_power(self):
        return self.attack_power

    def set_attack_power(self, attack_strength):
        self.attack_power = attack_strength

    def get_defence_power(self):
        return self.defence_power

    def set_defence_power(self, defence_strength):
        self.defence_power = defence_strength

    def set_level(self, level):
        self.level = level

    def set_experience(self, experience_points):
        self.experience = experience_points

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"Skill {skill.get_name()} added to {self.get_name()}'s skill set.")

    def remove_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
            print(f"Skill {skill.get_name()} removed from {self.get_name()}'s skill set.")
        else:
            print(f"Skill {skill.get_name()} not found in {self.get_name()}'s skill set.")

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        print(f"Weapon {weapon.get_name()} added to {self.get_name()}'s inventory.")

    def remove_weapon(self, weapon):
        if weapon in self.weapons:
            self.weapons.remove(weapon)
            print(f"Weapon {weapon.get_name()} removed from {self.get_name()}'s inventory.")
        else:
            print(f"Weapon {weapon.get_name()} not found in {self.get_name()}'s inventory.")