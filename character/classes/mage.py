from character.classes.character_class import CharacterClass

class Mage(CharacterClass):
    def __init__(self):
        super().__init__(name="Mage", health=100, attack=20, defense=10, speed=15)

    def special_ability(self):
        return "Cast a powerful spell that deals magic damage to enemies."
