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


    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element):
        super().__init__(name, description, quality, rarity, level_req)
        self._piercing = piercing
        self._damage = damage
        self._weapon_type = weapon_type
        self._isElement_damage = isElement_damage
        self._element_damage = element_damage
        self._element = element

    # Accessors

    def getDamage(self):
        return self._damage

    def getPiercing(self):
        return self._piercing

    def getWeaponType(self):
        return self._weapon_type

    def getIsElementDamage(self):
        return self._isElement_damage

    def getElementDamage(self):
        return self._element_damage

    def getElement(self):
        return self._element

    # Mutators

    def setDamage(self, new_damage):
        self._damage = new_damage

    def setPiercing(self, new_piercing):
        self._piercing = new_piercing

    def setWeaponType(self, new_weapon_type):
        self._weapon_type = new_weapon_type

    def setIsElementDamage(self, new_isElement_damage):
        self._isElement_damage = new_isElement_damage

    def setElementDamage(self, new_element_damage):
        self._element_damage = new_element_damage

    def setElement(self, new_element):
        self._element = new_element


    @abstractmethod
    def attack_mult(self, target):
        #Abtracted Method -> Modified in Subclasses
        pass
    
    @abstractmethod
    def block_mult(self, target):
        #Abtracted Method -> Modified in Subclasses
        pass

    @abstractmethod
    def info(self): #Calls from Parent Class (Inherited Behaviours)
        damage_info = f"Damage: {self._damage}\nWeapon Type: {self._weapon_type}\nPiercing: {self._piercing}"
        if self._isElement_damage:
            return (f"{super().info()}\n"
                    f"Damage Type: {self._element} & Physical\n"
                    f"{self._element} Elemental Damage: {self._element_damage}\n"
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