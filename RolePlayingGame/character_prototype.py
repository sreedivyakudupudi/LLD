from character_builder import CharacterBuilder
from character_registry import CharacterRegistry
from character import Character
from weapon import Weapon
from skill import Skill
import copy
from abc import ABC, abstractmethod
import uuid

class CharacterPrototype(ABC):

    def __init__(self, character):
        self.character = character

    @abstractmethod
    def clone(self, new_name):
        pass

    def _clone_character(self, new_name):
        cloned = copy.deepcopy(self)
        cloned.character.set_id(str(uuid.uuid4()))  # Assign a new unique ID to the cloned character
        cloned.character.set_name(new_name)
        return cloned.character


class WarriorPrototype(CharacterPrototype):
    def __init__(self):
        builder = CharacterBuilder()
        warrior = (builder.set_name("Warrior Template")
                   .set_health(200)
                   .set_strength(80)
                   .set_attack_strength(80)
                   .set_defence_strength(100)
                   .set_level(1)
                   .set_experience_points(0)
                   .set_character_type("Warrior")
                   .set_special_ability("Shield Block")
                   .build())
        super().__init__(warrior)

        self.character.add_weapon(Weapon("sword", 10, 50, "Melee", 100))
        self.character.add_weapon(Weapon("shield", 15, 60, "Defense", 120))

        self.character.add_skill(Skill("Shield Block", 1, 1.5, 5))
        self.character.add_skill(Skill("Heavy Attack", 1, 2.0, 3))

    def clone(self, new_name):
        return self._clone_character(new_name)

class MagePrototype(CharacterPrototype):
    def __init__(self):
        builder = CharacterBuilder()
        mage = (builder.set_name("Mage Template")
                 .set_health(150)
                 .set_strength(50)
                 .set_attack_strength(100)
                 .set_defence_strength(50)
                 .set_level(1)
                 .set_experience_points(0)
                 .set_character_type("Mage")
                 .set_special_ability("Fireball")
                 .build())
        super().__init__(mage)

        self.character.add_weapon(Weapon("staff", 8, 40, "Magic", 80))
        self.character.add_skill(Skill("Fireball", 1, 2.0, 3))

    def clone(self, new_name):
        return self._clone_character(new_name)

class ArcherPrototype(CharacterPrototype):
    def __init__(self):
        builder = CharacterBuilder()
        archer = (builder.set_name("Archer Template")
                   .set_health(120)
                   .set_strength(60)
                   .set_attack_strength(90)
                   .set_defence_strength(60)
                   .set_level(1)
                   .set_experience_points(0)
                   .set_character_type("Archer")
                   .set_special_ability("Precise Shot")
                   .build())
        super().__init__(archer)

        self.character.add_weapon(Weapon("bow", 5, 30, "Ranged", 60))
        self.character.add_weapon(Weapon("dagger", 7, 20, "Melee", 50))
        self.character.add_skill(Skill("Precise Shot", 1, 1.5, 5))
        self.character.add_skill(Skill("Multi-Shot", 1, 2.0, 3))

    def clone(self, new_name):
        return self._clone_character(new_name)


    