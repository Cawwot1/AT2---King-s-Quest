from equipment.weapons.weapon import Weapon

class Sword(Weapon):
    
    #Atributes
    _titan_slayer = None
    
    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, titan_slayer):
        super().__init__(name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element)
        self._titan_slayer = titan_slayer

    # Accessors for titan_slayer

    def getTitan_slayer(self):
        return self._titan_slayer

    # Mutators for titan_slayer

    def setTitan_slayer(self, new_titan_slayer):
        self._titan_slayer = new_titan_slayer

    # Behaviours
    def attack_mult(self):
        #Attack Stats
        pass

    def block_mult(self, target):
        # Logic for blocking
        pass

    def info(self):
        return (f"{super().info()} \n"
                f"Titan Slayer: {self._titan_slayer}")