from equipment.equipment import Equipment
from abc import ABC, abstractmethod
#QUESTION: Abtraction or No Abtraction

class Weapon(Equipment, ABC):

    #Atributes
    _piercing = None
    _damage = None
    _weapon_type = None
    _isElement_damage = bool
    _element_damage = None
    _element = None

    #Behaviours
    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element):
        super().__init__(name, description, quality, rarity, "Weapon", level_req)
        self._piercing = piercing
        self._damage = damage
        self._weapon_type = weapon_type
        self._isElement_damage = isElement_damage
        self._element_damage = element_damage
        self._element = element

    @abstractmethod
    def attack(self, target):
        #Abtracted Method -> Modified in Subclasses
        pass
    
    @abstractmethod
    def block(self, target):
        #Abtracted Method -> Modified in Subclasses
        pass

    def info(self): #Calls from Parent Class (Inherited Behaviours)
        damage_info = f"Damage: {self._damage}\nType: {self._weapon_type}\nPiercing: {self._piercing}"
        if self._isElement_damage:
            return (f"{super().info()}\n"
                    f"Damage Type: {self._element} & Physical\n"
                    f"{self._element} Damage: {self._element_damage}\n"
                    f"{damage_info}")
        else:
            return (f"{super().info()}\n"
                    f"Damage Type: Physical Damage\n"
                    f"{damage_info}")

                
    #Possible Expasion ... If i have the time

    def killCounter(self):
        pass

    def upgrades(self):
        pass