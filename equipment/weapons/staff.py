from equipment.weapons.weapon import Weapon

class Staff(Weapon):
    
    #Atributes
    __mana = None
    
    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, mana, item_type):
        super().__init__(name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, item_type)
        self.setMana(mana)

    #Getters
    def getMana(self): return self.__mana

    #Setters
    def setMana(self, new_mana): self.__mana = new_mana

    # Behaviours
    def attack_mult(self):
        # Logic for attacking a target
        pass

    def block_mult(self):
        # Logic for blocking
        pass