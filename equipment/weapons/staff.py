from equipment.weapons.weapon import Weapon

class Staff(Weapon):
    
    #Atributes
    _mana = None
    
    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, mana):
        super().__init__(name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element)
        self._mana = mana

    # Accessors for mana

    def getMana(self):
        return self._mana

    # Mutators for mana

    def setMana(self, new_mana):
        self._mana = new_mana

    # Behaviours
    def attack_mult(self, target):
        # Logic for attacking a target
        pass

    def block_mult(self, target):
        # Logic for blocking
        pass

    def info(self):
        return (f"{super().info()} \n"
                f"Mana: {self._mana}")