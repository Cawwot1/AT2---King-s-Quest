from character.classes.character_class import CharacterSelection

class Warrior(CharacterSelection):
    def __init__(self):
        super().__init__(name="Warrior", health=150, attack=30, defense=25, speed=10)

    def special_ability(self):
        return "Perform a powerful melee attack that can stun the enemy."
    
    def attack_names(attack_level):
        if attack_level == 1:
            return ("Swift Swing")
        else:
            return ("Heavy Strike")
