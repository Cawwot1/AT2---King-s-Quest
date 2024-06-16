from equipment.weapons.weapon import Weapon

class Dagger(Weapon):
    
    #Atributes
    _stealth = None
    
    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, stealth, item_type):
        super().__init__(name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, item_type)
        self._stealth = stealth
    
    # Accessors for stealth

    def getStealth(self):
        return self._stealth

    # Mutators for stealth

    def setStealth(self, new_stealth):
        self._stealth = new_stealth


    # Behaviours
    def attack_mult(self, target):
        # Logic for attacking a target
        pass

    def block_mult(self, target):
        # Logic for blocking
        pass

    def info(self):
        return (f"{super().info()} \n"
                f"Stealth: {self._stealth}")