from equipment.weapons.weapon import Weapon

class Bow(Weapon):
    
    #Atributes
    __multishot = None
    
    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, multishot, item_type):
        super().__init__(name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, item_type)
        self.setMultishot(multishot)

    
    #Getters
    def getMultishot(self): return self.__multishot

    #Setters
    def setMultishot(self, multishot): self._volley = multishot

    # Behaviours
    def attack_mult(self):
        # Logic for attacking a target
        attack_factor = self.__damage * self.__multishot
        pass

    def block_mult(self):
        # Logic for blocking
        pass