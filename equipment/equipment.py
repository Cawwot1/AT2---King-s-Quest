import pygame
from abc import ABC, abstractclassmethod

class Equipment(ABC):
    
    #Atributes
    _name = None
    _description = None
    _quality = None
    _rarity = None
    _level_req = None
    _type = None
    _element = None
    _piercing = None

    #Constructor
    def __init__(self, name, description, quality, rarity, level_req):
        self._name = name
        self._description = description
        self._quality = quality
        self._rarity = rarity
        self._level_req = level_req
    
    # Accessors

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def getQuality(self):
        return self._quality

    def getRarity(self):
        return self._rarity

    def getLevelReq(self):
        return self._level_req

    # Mutators

    def setName(self, new_name):
        self._name = new_name

    def setDescription(self, new_description):
        self._description = new_description

    def setQuality(self, new_quality):
        self._quality = new_quality

    def setRarity(self, new_rarity):
        self._rarity = new_rarity

    def setLevelReq(self, new_level_req):
        self._level_req = new_level_req


    #Behaviours
    def equip(self, character):
        # Logic for equipping the item
        pass

    def unequip(self, character):
        # Logic for unequipping the item
        pass

    def info(self):
        return (f"{self._name}: {self._description}\n"
                f"Quality: {self._quality}\n"
                f"Rarity: {self._rarity}\n"
                f"Level Requirement: {self._level_req}\n"
                f"Equipment Type: {self._type}")
