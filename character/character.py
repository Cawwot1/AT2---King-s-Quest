from item_management.inventory import Inventory
from character.attributes.skill import Skill
import random
import math
import pygame

class Character():
    """
    Character class
    """
    
    #Atributes
    
    #Other
    _name = None
    _character_class = None

    #Combat
    _speed = None
    _health = None
    _defence = None
    
    #Progression
    _level = None
    _xp = None
    _attribute_points = None
    __world_level = None
    __map = None    
    

    #Skills
    _skill_attack = None
    _skill_defence = None
    _skill_speed = None

    #Equipment & Inventory
    _inventory = None
    _gold = None
    _attribute_points = None
    __inventory = None

    #Equipped
    _equipped_ring = None
    _equipped_necklace = None
    _equipped_helmet = None
    _equipped_chestplate = None
    _equipped_legs = None
    _equipped_boots = None
    _equipped_weapon = None

    #Why are these caps?
    MAX_LEVEL = 50  # Maximum level a character can reach
    ATTRIBUTE_POINTS_PER_LEVEL = 3  # Number of attribute points gained per level

    #Conctructor
    def __init__(self, name, character_class, inventory_cap): #requests input (into constr.) for name & cha. class     
        self._name = name
        self._character_class = character_class
        self.__inventory = Inventory(inventory_cap)
        
        #skills
        self._skill_attack = 0
        self._skill_defence = 0
        self._skill_speed = 0

        #equipped
        self._equipped_ring = False
        self._equipped_necklace = False
        self._equipped_helmet = False
        self._equipped_chestplate = False
        self._equipped_legs = False
        self._equipped_boots = False
        self._equipped_weapon = False

        #preset atribute values
        self._level = 0  # Character's current level
        self._attack = 10
        self._speed = 10
        self._xp = 0  # Character's current experience points
        self._health = 100  # Example starting value for character's hit points
        self._defence = 10  # Example starting value for character's armor class
        self._skills = []  # Example empty dictionary for character's skills
        self.gold = 0  # Example starting value for character's gold
        self.attribute_points = 0  # Attribute points available to allocate
        self.crit_chance = 10 #percent (%)
        self.crit_damage = 50 #precent (%)

        #Progression
        self.setWorld_level(1)
        self.setMap("Woodlands")

    #Accessors
    def getWorld_level(self):
        return self.__world_level
    def getMap(self):
        return self.__map

    #Mutators
    def setWorld_level(self, world_level):
        self.__world_level = world_level
    def setMap(self, map):
        self.__map = map

    #UP TO HERE ###########

    def basic_info(self):
        return (f"Health: {self._health}"
                f"Attack: {self._attack}"
                f"Defence: {self._defence}")

    def getInventory(self):
        return self.__inventory

    def assign_attribute_points(self, attribute, points):

        """
        Skill Points
        """

        if attribute == "attack":
            self._skill_attack = Skill.boost_attack(points)
        elif attribute == "defence":
            self._skill_defence = Skill.boost_defence(points)
        elif attribute == "speed":
            self._skill_speed = Skill.boost_speed(points)
        else:
            print(f"Error: Attribute '{attribute}' does not exist.")

    def equip_weapon(self, weapon_object): 
        
        """
        Equips Weapon
        """

        if self._equipped_weapon == True: #if a weapon is equipped
            user_input = input(f"{self._equipped_weapon.getName()} is equipped, do you want to replace? (y/n)")
            if user_input.lower() != "y": #cancelation of weap. equip
                print("Action Cancelled")
                return
        self._equipped_weapon = weapon_object #equips weapon
        print(f"{weapon_object} equipped")

    def equip_armour(self, armour_object): ### IS THIS ALLOWED (having a dictionary here)???

        """
        Equips Armour 
        """

        piece_equipped = { 
            "helmet": self._equipped_helmet,
            "chestplate": self._equipped_chestplate,
            "legs": self._equipped_legs,
            "boots": self._equipped_boots}
        armour_piece = piece_equipped[armour_object.getPiece()] #checks for the current equiped armour piece
        
        if armour_piece == True: #if a piece is equipped
            user_input = input(f"{piece_equipped.getName()} is equipped, do you want to replace? (y/n)")
            if user_input.lower() != "y": #cancellation of armour equip.
                print("Action Cancelled")
                return
        piece_equipped = armour_object #equips new piece
        print(f"{armour_object.getName()} equipped") 

    def equip_accessory(self, accessory_object):

        """
        Equips Accessory
        """
        acc_equipped = {
            "ring": self._equipped_ring,
            "necklace": self._equipped_necklace}
        acc_piece = acc_equipped(accessory_object.getPiece())

        if acc_piece == True: #if a accessory is equipped
            user_input = input(f"{accessory_object.getName()} is equipped, do you want to replace? (y/n)")
            if user_input.lower() != "y": #cancelation of acces. equip
                print("Action Cancelled")
                return
        acc_equipped = accessory_object #equips accessory
        print(f"{accessory_object} equipped") 

    def gain_experience(self, experience): 
        """
        Exp & Level System
        """
        self._xp += experience  # Increase character's experience points
        required_experience = self.calculate_required_experience(self._level)
        
        while self._xp >= required_experience and self._level < self.MAX_LEVEL: #Checks if character has enough to Level-up
            self._level += 1  # Level up the character
            self._xp -= required_experience  #Subtract level-up experience points
            
            #Level-up boosts
            self._health += 5
            self._attack += 2
            
            self.attribute_points += self.ATTRIBUTE_POINTS_PER_LEVEL  # Allocate attribute points
            print(f"Level up! {self._name} is now level {self._level}.")
            required_experience = self.calculate_required_experience(self._level + 1)#Experience required for next level

    def calculate_required_experience(self, level): 
        """
        Calculates requred experience for next level
        """
        return round(int(level + 10*level**1.2))