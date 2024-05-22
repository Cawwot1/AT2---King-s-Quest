from equipment.weapons.weapon import Weapon

class Bow(Weapon):
    
    #Atributes
    _percision = None
    
    def __init__(self, name, description, quality, rarity, level_req, piercing, damage, weapon_type, isElement_damage, element_damage, element, precision):
        super().__init__(name, description, quality, rarity, level_req, piercing, damage, weapon_type, isElement_damage, element_damage, element)
        self._percision = precision

    def attack(self, target):
        # Logic for attacking a target
        pass

    def block(self, target):
        # Logic for blocking
        pass

    def info(self):
        return super().info()