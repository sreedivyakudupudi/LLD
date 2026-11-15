class CharacterManager:
    def __init__(self, character_registry):
        self.character_registry = character_registry
        self.characters = {}

    def create_character(self, character_type, new_name):
        character = self.character_registry.create_character(character_type, new_name)
        self.add_character(character)
        return character

    def add_character(self, character):
        if character.character_id is None or character.character_id in self.characters:
            raise ValueError("Character must have a unique and Valid ID before adding to the manager.")
        self.characters[character.character_id] = character

    def remove_character_by_id(self, character_id):
        if character_id in self.characters:
            del self.characters[character_id]
        else:
            raise ValueError(f"Character with ID '{character_id}' not found.") 
        
        
    def get_character_by_id(self, character_id):
        if character_id in self.characters:
            return self.characters[character_id]
        else:
            raise ValueError(f"Character with ID '{character_id}' not found.")

    def list_characters(self):
        return list(self.characters.values())

    def display_character(self, character_id):
        character = self.get_character_by_id(character_id)
        print("Character Details:")
        print(f"ID: {character.character_id}, Name: {character.name}, Type: {character.character_type}, Health: {character.health}, Strength: {character.strength}, Level: {character.level}, XP: {character.experience}")



    