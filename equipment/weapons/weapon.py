from equipment.equipment import Equipment
from abc import ABC, abstractmethod
#QUESTION: Abtraction or No Abtraction

class Weapon(Equipment, ABC):

    #Atributes
    __piercing = None
    __damage = None
    __weapon_type = None
    __isElement_damage = bool
    __element_damage = None
    __element = None


    def __init__(self, name, description, quality, rarity, level_req, damage, piercing, weapon_type, isElement_damage, element_damage, element, item_type):
        super().__init__(name, description, quality, rarity, level_req, item_type)
        self.setPiercing(piercing)
        self.setDamage(damage)
        self.setWeaponType(weapon_type)
        self.setIsElementDamage(isElement_damage)
        self.setElementDamage(element_damage)
        self.setElement(element)
    
    #Getters
        #Combat Stats
    def getDamage(self): return self.__damage
    def getPiercing(self): return self.__piercing
    def getIsElementDamage(self): return self.__isElement_damage
    def getElementDamage(self): return self.__element_damage
        #Other
    def getWeaponType(self): return self.__weapon_type
    def getElement(self): return self.__element

    #Setters
    def setDamage(self, new_damage): self.__damage = new_damage
    def setPiercing(self, new_piercing): self.__piercing = new_piercing
    def setWeaponType(self, new_weapon_type): self.__weapon_type = new_weapon_type
    def setIsElementDamage(self, new_isElement_damage): self.__isElement_damage = new_isElement_damage
    def setElementDamage(self, new_element_damage): self.__element_damage = new_element_damage
    def setElement(self, new_element): self.__element = new_element

    @abstractmethod
    def attack_mult(self, target):
        #Abtracted Method -> Modified in Subclasses
        pass
    
    @abstractmethod
    def block_mult(self, target):
        #Abtracted Method -> Modified in Subclasses
        pass