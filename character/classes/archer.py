from character.classes.character_class import CharacterClass

class Archer(CharacterClass):
    def __init__(self):
        super().__init__(name="Archer", health=90, attack=25, defense=12, speed=20)

    def special_ability(self):
        return "Shoot a volley of arrows that hits multiple enemies."
