#Inventory & Abilities
from item_management.inventory import Inventory
from character.attributes.skill import Skill

#Maps & Environment
from enemy.create_enemy import Create_Enemy
from maps.woodlands import Map_Woodlands

#Character actions imported in Behaviours to stop curcular import/dependancy error

import random
import math
import pygame
import time

class Character():
    """
    Character class
    """
    
    #Atributes
    
    #Character Constr.
    __name = None
    __character_class = None

    #Combat
    __speed = None
    __health = None
    __defence = None
    __damage = None
    
    #Progression
    __level = None
    __xp = None
    __world_level = None
    __map = None  

    #Skills
    __skill_attack = None
    __skill_defence = None
    __skill_speed = None

    #Equipment & Inventory
    __attribute_points = None
    __inventory = None

    #Resources
    __gold = None
    __wood = None
    __stone = None
    __iron = None

    #Equipped
    __equipped_ring = None
    __equipped_necklace = None
    __equipped_helmet = None
    __equipped_chestplate = None
    __equipped_legs = None
    __equipped_boots = None
    __equipped_weapon = None

    #Why are these caps?
    MAX_LEVEL = 50  # Maximum level a character can reach
    ATTRIBUTE_POINTS_PER_LEVEL = 3  # Number of attribute points gained per level

    #Conctructor
    def __init__(self, name, character_class, inventory_cap): #requests input (into constr.) for name & cha. class     
        self.setName(name)
        self.setCharacter_class(character_class)
        self.__inventory = Inventory(inventory_cap)
        
        
        #skills
        self.setSkill_attack(0)
        self.setSkill_defence(0)
        self.setSkill_speed(0)

        #equipped
        self.setEquipped_ring(None)
        self.setEquipped_necklace(None)
        self.setEquipped_helmet(None)
        self.setEquipped_chestplate(None)
        self.setEquipped_legs(None)
        self.setEquipped_boots(None)
        self.setEquipped_weapon(None)
        
        self.setEquipment_list(None, None, None, None, None, None, None)

        self.setSpeed(10)
        self.setHealth(100)
        self.setDefence(10)
        self.setDamage(10)

        self.setLevel(0)
        self.setXp(0)
        self.setWorld_level(1)
        self.setAttribute_points(0)
    
        self.setGold(0)
        self.setWood(0)
        self.setStone(0)
        self.setIron(0)

        self.setInventory(Inventory(inventory_cap))

        #Progression
        self.setWorld_level(1)
        self.setMap(Map_Woodlands())

    #Accessors
    def getName(self):
        return self.__name
    def getCharacter_class(self):
        return self.__character_class
    
    def getSpeed(self):
        return self.__speed
    def getHealth(self):
        return self.__health
    def getDefence(self):
        return self.__defence
    
    def getLevel(self):
        return self.__level
    def getXp(self):
        return self.__xp
    def getWorld_level(self):
        return self.__world_level
    def getMap(self):
        return self.__map
    
    def getSkill_attack(self):
        return self.__skill_attack
    def getSkill_defence(self):
        return self.__skill_defence
    def getSkill_speed(self):
        return self.__skill_speed
    def getDamage(self):
        return self.__damage

    def getInventory(self):
        return self.__inventory
    def getAttribute_points(self):
        return self.__attribute_points
    
    def getGold(self):
        return self.__gold
    def getWood(self):
        return self.__wood
    def getStone(self):
        return self.__stone
    def getIron(self):
        return self.__iron
    
    def getEquipped_ring(self):
        return self.__equipped_ring
    def getEquipped_necklace(self):
        return self.__equipped_necklace
    def getEquipped_helmet(self):
        return self.__equipped_helmet
    def getEquipped_chestplate(self):
        return self.__equipped_chestplate
    def getEquipped_legs(self):
        return self.__equipped_legs
    def getEquipped_boots(self):
        return self.__equipped_boots
    def getEquipped_weapon(self):
        return self.__equipped_weapon
    
    def getEquipment_list(self):
        return self.__equipment_list

    #Mutators
    def setName(self, name):
        self.__name = name
    def setCharacter_class(self, character_class):
        self.__character_class = character_class

    def setSpeed(self, speed):
        self.__speed = speed
    def setHealth(self, health):
        self.__health = health
    def setDefence(self, defence):
        self.__defence = defence

    def setLevel(self, level):
        self.__level = level
    def setXp(self, xp):
        self.__xp = xp
    def setWorld_level(self, world_level):
        self.__world_level = world_level
    def setMap(self, map):
        self.__map = map

    def setSkill_attack(self, skill_attack):
        self.__skill_attack = skill_attack
    def setSkill_defence(self, skill_defence):
        self.__skill_defence = skill_defence
    def setSkill_speed(self, skill_speed):
        self.__skill_speed = skill_speed    
    def setDamage(self, damage):
        self.__damage = damage

    def setInventory(self, inventory):
        self.__inventory = inventory
    def setAttribute_points(self, attribute_points):
        self.__attribute_points = attribute_points

    def setGold(self, gold):
        self.__gold = gold
    def setWood(self, wood):
        self.__wood = wood
    def setStone(self, stone):
        self.__stone = stone
    def setIron(self, iron):
        self.__iron = iron

    def setEquipped_ring(self, equipped_ring):
        self.__equipped_ring = equipped_ring
    def setEquipped_necklace(self, equipped_necklace):
        self.__equipped_necklace = equipped_necklace
    def setEquipped_helmet(self, equipped_helmet):
        self.__equipped_helmet = equipped_helmet
    def setEquipped_chestplate(self, equipped_chestplate):
        self.__equipped_chestplate = equipped_chestplate
    def setEquipped_legs(self, equipped_legs):
        self.__equipped_legs = equipped_legs
    def setEquipped_boots(self, equipped_boots):
        self.__equipped_boots = equipped_boots
    def setEquipped_weapon(self, equipped_weapon):
        self.__equipped_weapon = equipped_weapon

    #Has to get updates (through combat_stats) -> ONLY USED FOR COMBAT STATS
    def setEquipment_list(self, boots, helmet, chestplate, legs, necklace, ring, weapon):
        self.__equipment_list = [boots, helmet, chestplate, legs, necklace, ring, weapon]
    
    #Behaviours

    def basic_stats(self):
        return (f"Health: {self._health}"
                f"Attack: {self._attack}"
                f"Defence: {self._defence}")
    
    def combat_stats(self): #Used for combat action
        
        self.setEquipment_list(self.getEquipped_boots, self.getEquipped_helmet, self.getEquipped_chestplate, self.setEquipped_legs, self.getEquipped_necklace, self.getEquipped_ring, self.getEquipped_weapon)
        equipment_list = self.getEquipment_list()

        # Initialize totals
        total_defence = 0
        total_hardness = 0
        total_element_def = 0
        total_attack = 0

        # Iterate over equipment list and calculate totals
        for item in equipment_list:
            if hasattr(item, 'getDefence'):
                total_defence += item.getDefence()
            if hasattr(item, 'getHardness'):
                total_hardness += item.getHardness()
            if hasattr(item, 'getElementalDef'):
                total_element_def += item.getElementalDef()
            if hasattr(item, 'getAttack'):
                total_attack += item.getAttack()

        # Add additional stats from the .get methods
        total_defence += self.getDefence()
        total_attack += self.getDamage()

        #Weapon Gimick attribute is Retrived in Combat
        if hasattr(self.getEquipped_weapon, "getDamage"):
            total_attack += self.getEquipped_weapon.getDamage()
            return(total_defence, 
               total_hardness, 
               total_attack, 
               total_element_def, 
               self.getEquipped_weapon.getWeaponType(), 
               self.getEquipped_weapon.getElementDamage(), 
               self.getEquipped_weapon.getElement(),
               self.getEquipped_weapon.getPiercing())
        else: #No Weapon Equipped
            return(total_defence, 
               total_hardness, 
               total_attack, 
               total_element_def, 
               None, None, None ,None)

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
    
    def explore(self, screen):
        from character.actions.explore import Explore
        explore = Explore(screen)
        explore.explore(self, screen)

    def combat(self, screen, enemy):
        from character.actions.combat import Combat
        combat = Combat(screen, self, enemy)
        combat.combat(self, enemy)
    

