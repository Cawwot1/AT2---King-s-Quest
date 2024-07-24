from character.classes.character_class import CharacterClass

class Rogue(CharacterClass):
    def __init__(self):
        super().__init__(name="Rogue", health=80, attack=35, defense=8, speed=25)

    def special_ability(self):
        return "Execute a stealth attack that deals high damage from behind."
