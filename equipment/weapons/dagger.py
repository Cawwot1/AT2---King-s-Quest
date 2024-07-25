from equipment.weapons.weapon import Weapon

class Dagger(Weapon):
    
    #Atributes
    __stealth = None
    
    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, stealth, item_type):
        super().__init__(name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, item_type)
        self.setStealth(stealth)
    
    #Getters
    def getStealth(self): return self.__stealth

    #Setters
    def setStealth(self, new_stealth): self.__stealth = new_stealth

    # Behaviours
    def attack_mult(self, target):
        # Logic for attacking a target
        pass

    def block_mult(self, target):
        # Logic for blocking
        pass