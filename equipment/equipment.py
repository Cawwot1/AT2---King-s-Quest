import pygame
from abc import ABC, abstractclassmethod

class Equipment(ABC):
    
    #Atributes
    __name = None
    __description = None
    __quality = None
    __rarity = None
    __level_req = None
    __item_type = None

    #Constructor
    def __init__(self, name, description, quality, rarity, level_req, item_type):
        self.setName(name)
        self.setDescription(description)
        self.setQuality(quality)
        self.setRarity(rarity)
        self.setLevel_req(level_req)
        self.setItem_type(item_type)
            
    
    #Getters
    def getName(self): return self.__name
    def getDescription(self): return self.__description
    def getQuality(self): return self.__quality
    def getRarity(self): return self.__rarity
    def getLevel_req(self): return self.__level_req
    def getItem_type(self): return self.__item_type

    #Setters
    def setName(self, name): self.__name = name
    def setDescription(self, description): self.__description = description
    def setQuality(self, quality): self.__quality = quality
    def setRarity(self, rarity): self.__rarity = rarity
    def setLevel_req(self, level_req): self.__level_req = level_req
    def setItem_type(self, item_type): self.__item_type = item_type

    #Behaviours
    def equip(self, character):
        # Logic for equipping the item
        pass

    def unequip(self, character):
        # Logic for unequipping the item
        pass
