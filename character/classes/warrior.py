from character.classes.character_class import CharacterClass

class Warrior(CharacterClass):
    def __init__(self):
        super().__init__(name="Warrior", health=150, attack=30, defense=25, speed=10)

    def special_ability(self):
        return "Perform a powerful melee attack that can stun the enemy."
