from equipment.weapons.weapon import Weapon

class Sword(Weapon):
    
    #Atributes
    __titan_slayer = None
    
    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, titan_slayer, item_type):
        super().__init__(name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, item_type)
        self.setTitan_slayer(titan_slayer)

    #Getters
    def getTitan_slayer(self): return self.__titan_slayer

    #Setters
    def setTitan_slayer(self, new_titan_slayer): self.__titan_slayer = new_titan_slayer

    # Behaviours
    def attack_mult(self):
        #Attack Stats
        pass

    def block_mult(self):
        # Logic for blocking
        pass