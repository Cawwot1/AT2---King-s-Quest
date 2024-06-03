from equipment.armour.armour import Armour
from abilities import abilities 

class Helmet(Armour):
    
    #Atributes
    _abilities = None
    _ability_list = None
    
    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, abilities):
        super().__init__(name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element)
        self._abilities = len(abilities.split(" "))
        self._ability_list = []
        while len(self._abilities) != 0:
            
            pass
    
    # Accessors for abilities

    def getAbilites(self):
        return self._abilities

    # Mutators for abilities

    def setAbilities(self, abilities):
        self._abilities = abilities


    # Behaviours

    def defence_mult(self):
        # Logic for attacking a target
        pass

    def info(self):
        return (f"{super().info()} \n"
                f"Abilities: {self._abilities}")