import pygame

class Equipment:
    
    #Atributes
    _name = None
    _description = None
    _quality = None
    _rarity = None
    _level_req = None
    _type = None

    #Constructor
    def __init__(self, name, description, quality, rarity, type, level_req):
        self._name = name
        self._description = description
        self._quality = quality
        self._rarity = rarity
        self._level_req = level_req
        self._type = type
    
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
                f"Type: {self._type}")
