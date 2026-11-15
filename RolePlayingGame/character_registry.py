class CharacterRegistry:

    def __init__(self):
        self.prototypes = {}

    def register_prototype(self, character_type, prototype):
        if character_type in self.prototypes:
            raise ValueError(f"Character type '{character_type}' is already registered.")
        self.prototypes[character_type] = prototype

    def get_prototype(self, character_type):
        return self.prototypes.get(character_type)

    def create_character(self, character_type, new_name):
        prototype = self.get_prototype(character_type)
        if prototype:
            return prototype.clone(new_name)
        else:
            raise ValueError(f"Character type '{character_type}' not found in registry.")