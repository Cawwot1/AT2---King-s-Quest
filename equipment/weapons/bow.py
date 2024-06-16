from equipment.weapons.weapon import Weapon

class Bow(Weapon):
    
    #Atributes
    _multishot = None
    
    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, multishot, item_type):
        super().__init__(name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, item_type)
        self._multishot = multishot

    
    # Accessors for multishot

    def getMultishot(self):
        return self._multishot

    # Mutators for multishot

    def setMultishot(self, multishot):
        self._volley = multishot


    # Behaviours
    def attack_mult(self):
        # Logic for attacking a target
        attack_factor = self._damage * self._multishot
        pass

    def block_mult(self):
        # Logic for blocking
        pass

    def info(self):
        return (f"{super().info()} \n"
                f"Mutlishot Percentage: {self._multishot}")