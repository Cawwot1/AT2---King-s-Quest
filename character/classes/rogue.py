from character.classes.character_class import CharacterSelection

class Rogue(CharacterSelection):
    def __init__(self):
        super().__init__(name="Rogue", health=80, attack=45, defense=8, speed=25)

    def special_ability(self):
        return "Execute a stealth attack that deals high damage from behind."

    def attack_names(attack_level):
        if attack_level == 1:
            return ("Dark Stab")
        else:
            return ("Shadow Strike")