from character.classes.character_class import CharacterSelection

class Archer(CharacterSelection):

    #Constructor
    def __init__(self):
        super().__init__(name="Archer", health=90, attack=30, defense=12, speed=20)

    def special_ability(self):
        return "Shoot a volley of arrows that hits multiple enemies."
    
    def attack_names(attack_level):
        if attack_level == 1:
            return ("Sharp Shot")
        else:
            return ("Harming Arrow")