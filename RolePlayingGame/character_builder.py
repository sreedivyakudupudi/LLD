from character import Character

class CharacterBuilder:

    def __init__(self):
        self.reset()

    def reset(self):
        self.character_id = None
        self.name = "Unknown"
        self.health = 100
        self.strength = 50
        self.attack_strength = 50
        self.defence_strength = 50
        self.level = 1
        self.experience_points = 0
        self.character_type = "Unknown"
        self.special_ability = None
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_health(self, health):
        self.health = health
        return self

    def set_strength(self, strength):
        self.strength = strength
        return self

    def set_attack_strength(self, attack):
        self.attack_strength = attack
        return self

    def set_defence_strength(self, defence):
        self.defence_strength = defence
        return self

    def set_level(self, level):
        self.level = level
        return self

    def set_experience_points(self, xp):
        self.experience_points = xp
        return self

    def set_character_type(self, character_type):
        self.character_type = character_type
        return self

    def set_special_ability(self, ability):
        self.special_ability = ability
        return self

    # def set_id(self, character_id):
    #     self.character_id = character_id
    #     return self

    def build(self):
        return Character(
            # self.character_id,
            self.name,
            self.health,
            self.strength,
            self.attack_strength,
            self.defence_strength,
            self.level,
            self.experience_points,
            self.character_type,
            self.special_ability
        )