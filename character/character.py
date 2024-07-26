#Inventory & Abilities
from character.attributes.skill import Skill
from equipment.create_equipment import Create_Equipment

#Maps & Environment
from maps.woodlands import Map_Woodlands

#Map & Camera
from game_run.settings import *

import pygame
import time

class Character(pygame.sprite.Sprite):
    """
    Character class
    """
    
    #Atributes

        #Character
    __name = None
    __character_class = None
    __inventory = None

        #Character Sprite/Image
    image = None #MUST BE PUBLIC
    rect = None #MUST BE PUBLIC

        #Character Movement
    __direction = None
    __movement_speed = None


        #Equipped
    __equipped_ring = None
    __equipped_necklace = None
    __equipped_helmet = None
    __equipped_chestplate = None
    __equipped_legs = None
    __equipped_boots = None
    __equipped_weapon = None
    __equipment_list = None #Equipped List

        #Character Stats
    __speed = None
    __health = None
    __defence = None
    __damage = None
    #Total Stats
    __total_defence = None
    __total_hardness = None
    __total_element_def = None
    __total_attack = None

        #Progression
    __level = None
    __xp = None
    __world_level = None
    __attribute_points = None
    __map = None  

    MAX_LEVEL = 50  # Maximum level a character can reach
    ATTRIBUTE_POINTS_PER_LEVEL = 3  # Number of attribute points gained per level

    #Conctructor
    def __init__(self, name, character_class, inventory_cap, pos, group): #requests input (into constr.) for name, cha. class, pos. of character & group
        super().__init__(group)

            #Skills instance -> skills object for character
        self.setSkills_instance(Skill(self))

            #Character
        self.setName(name)
        self.setCharacter_class(character_class)
        self.setInventory(inventory_cap)
        
            #Character Sprite
        self.setImage(pygame.image.load(f'assets/classes/{character_class.lower()}.png').convert_alpha()) #MUST BE PUBLIC
        self.setRect(self.image.get_rect(center=pos)) #MUST BE PUBLIC
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

            #Character Movement
        self.setDirection(pygame.math.Vector2())
        self.setMovement_speed(5)

            #equipped
        self.setEquipped_ring(None)
        self.setEquipped_necklace(None)
        self.setEquipped_helmet(None)
        self.setEquipped_chestplate(None)
        self.setEquipped_legs(None)
        self.setEquipped_boots(None)
        self.setEquipped_weapon(None)
        #Equipped List
        self.setEquipment_list(None, None, None, None, None, None, None)

            #Player Stats
        self.setSpeed(10)
        self.setHealth(100)
        self.setDefence(10)
        self.setDamage(10)
        #Total Stats (for combat_stats fuction)
        self.setTotal_defence(0)
        self.setTotal_hardness(0)
        self.setTotal_element_def(0)
        self.setTotal_attack(0)

            #Progression
        self.setLevel(0)
        self.setXp(0)
        self.setWorld_level(1)
        self.setAttribute_points(0)
        self.setMap(Map_Woodlands())

    #Accessors

        #Character
    def getName(self): return self.__name
    def getCharacter_class(self): return self.__character_class
        
        #Character stats
    def getSpeed(self): return self.__speed
    def getHealth(self): return self.__health
    def getDefence(self): return self.__defence
    def getDamage(self): return self.__damage
    #Total Stats
    def getTotal_defence(self): return self.__total_defence
    def getTotal_hardness(self): return self.__total_hardness
    def getTotal_element_def(self): return self.__total_element_def
    def getTotal_attack(self): return self.__total_attack
    #UNUSED
    def getInventory(self): return self.__inventory
    
        #Character Movement
    def getDirection(self): return self.__direction
    def getMovement_speed(self): return self.__movement_speed

        #Progression
    def getLevel(self): return self.__level
    def getXp(self): return self.__xp
    def getWorld_level(self): return self.__world_level
    def getMap(self): return self.__map
    def getAttribute_points(self): return self.__attribute_points #Skill Points
    
        #Equip Items -> UNUSED
    def getEquipped_ring(self): return self.__equipped_ring
    def getEquipped_necklace(self): return self.__equipped_necklace
    def getEquipped_helmet(self): return self.__equipped_helmet
    def getEquipped_chestplate(self): return self.__equipped_chestplate
    def getEquipped_legs(self): return self.__equipped_legs
    def getEquipped_boots(self): return self.__equipped_boots
    def getEquipped_weapon(self): return self.__equipped_weapon
    def getEquipment_list(self): return self.__equipment_list #Equipment List
    
        #Character Sprite
    #MUST BE PUBLIC/Character must have attribute image & rect -> assits with pygame.sprite.Sprite library or returns an error) 
    def getImage(self): return self.image #MUST BE PUBLIC
    def getRect(self): return self.rect #MUST BE PUBLIC 
        
        #Skills instance -> skills object for character
    def getSkills_instance(self): return self.__skills_instace

    #Mutators
        
        #Character
    def setName(self, name): self.__name = name
    def setCharacter_class(self, character_class): self.__character_class = character_class
        
        #Character Stats
    def setSpeed(self, speed): self.__speed = speed
    def setHealth(self, health): self.__health = health
    def setDefence(self, defence): self.__defence = defence
    def setDamage(self, damage): self.__damage = damage
    #Total stats
    def setTotal_defence(self, total_defence): self.__total_defence = total_defence
    def setTotal_hardness(self, total_hardness): self.__total_hardness = total_hardness
    def setTotal_element_def(self, total_element_def): self.__total_element_def = total_element_def
    def setTotal_attack(self, total_attack): self.__total_attack = total_attack
    #UNUSED 
    def setInventory(self, inventory):
        self.__inventory = inventory

        #Character Movement
    def setDirection(self, direction): self.__direction = direction
    def setMovement_speed(self, movement_speed): self.__movement_speed = movement_speed

        #Progression
    def setLevel(self, level): self.__level = level
    def setXp(self, xp): self.__xp = xp
    def setWorld_level(self, world_level): self.__world_level = world_level
    def setMap(self, map): self.__map = map
    def setAttribute_points(self, attribute_points): self.__attribute_points = attribute_points #Skill points

        #Equip Items -> UNUSED
    def setEquipped_ring(self, equipped_ring): self.__equipped_ring = equipped_ring
    def setEquipped_necklace(self, equipped_necklace): self.__equipped_necklace = equipped_necklace
    def setEquipped_helmet(self, equipped_helmet): self.__equipped_helmet = equipped_helmet
    def setEquipped_chestplate(self, equipped_chestplate): self.__equipped_chestplate = equipped_chestplate
    def setEquipped_legs(self, equipped_legs): self.__equipped_legs = equipped_legs
    def setEquipped_boots(self, equipped_boots): self.__equipped_boots = equipped_boots
    def setEquipped_weapon(self, equipped_weapon): self.__equipped_weapon = equipped_weapon
        #Has to get updates (through combat_stats) -> ONLY USED FOR COMBAT STATS
    def setEquipment_list(self, boots, helmet, chestplate, legs, necklace, ring, weapon): self.__equipment_list = [boots, helmet, chestplate, legs, necklace, ring, weapon]

        #Character Sprite
    def setImage(self, image): self.image = image #MUST BE PUBLIC
    def setRect(self, rect): self.rect = rect #MUST BE PUBLIC

       #Skills instance -> skills object for character
    def setSkills_instance(self, skills_instance): self.__skills_instace = skills_instance

    #Behaviours
        
        #Character Movement
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.__direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.__direction.y = 1
        else:
            self.__direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.__direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.__direction.x = -1
        else:
            self.__direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.__direction * self.__movement_speed

        #Inventory
    def inventory_info(self):
        #Example inventory display
        inventory_items = [f"{item.getName()}: {item.getQuantity()}" for item in self.__inventory.getItems()]
        return inventory_items
    
    def combat_stats(self): #Used for combat action

        """
        Combat Stats (total stats -> combines character, skills & equipment)
        """

        self.setEquipment_list(self.getEquipped_boots, self.getEquipped_helmet, self.getEquipped_chestplate, self.setEquipped_legs, self.getEquipped_necklace, self.getEquipped_ring, self.getEquipped_weapon)
        equipment_list = self.getEquipment_list()

        # Iterate over equipment list and calculate totals
        for item in equipment_list:
            if hasattr(item, 'getDefence'):
                self.__total_defence += item.getDefence()
            if hasattr(item, 'getHardness'):
                self.__total_hardness += item.getHardness()
            if hasattr(item, 'getElementalDef'):
                self.__total_element_def += item.getElementalDef()
            if hasattr(item, 'getAttack'):
                self.__total_attack += item.getAttack()

        # Add additional stats from the .get methods
        self.__total_defence += self.getDefence() + self.__skills_instace.getAtri_def()
        self.__total_attack += self.getDamage() + self.__skills_instace.getAtri_atk()

        #Weapon Gimick attribute is Retrived in Combat
        if hasattr(self.getEquipped_weapon, "getDamage"):
            total_attack += self.getEquipped_weapon.getDamage()
            return(self.__total_defence, 
               self.__total_hardness, 
               self.__total_attack, 
               self.__total_element_def, 
               self.getEquipped_weapon.getWeaponType(), 
               self.getEquipped_weapon.getElementDamage(), 
               self.getEquipped_weapon.getElement(),
               self.getEquipped_weapon.getPiercing())
        else: #No Weapon Equipped
            return(self.__total_defence, 
               self.__total_hardness, 
               self.__total_attack, 
               self.__total_element_def, 
               None, None, None ,None)

    def equip_weapon(self, weapon_object): 
        
        """
        Equips Weapon
        """

        if self.__equipped_weapon == True: #if a weapon is equipped
            user_input = input(f"{self.__equipped_weapon.getName()} is equipped, do you want to replace? (y/n)")
            if user_input.lower() != "y": #cancelation of weap. equip
                print("Action Cancelled")
                return
        self.__equipped_weapon = weapon_object #equips weapon
        print(f"{weapon_object} equipped")
        
    def equip_armour(self, armour_object):

        """
        Equips Armour 
        """

        piece_equipped = { 
            "helmet": self.__equipped_helmet,
            "chestplate": self.__equipped_chestplate,
            "legs": self.__equipped_legs,
            "boots": self.__equipped_boots}
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
            "ring": self.__equipped_ring,
            "necklace": self.__equipped_necklace}
        acc_piece = acc_equipped(accessory_object.getPiece())

        if acc_piece == True: #if a accessory is equipped
            user_input = input(f"{accessory_object.getName()} is equipped, do you want to replace? (y/n)")
            if user_input.lower() != "y": #cancelation of acces. equip
                print("Action Cancelled")
                return
        acc_equipped = accessory_object #equips accessory
        print(f"{accessory_object} equipped") 

    def gain_experience(self, experience, screen): 
        
        """
        Exp & Level System with visual effects
        """

        self.__xp += experience  # Increase character's experience points
        required_experience = self.calculate_required_experience(self.__level)
        
        while self.__xp >= required_experience and self.__level < self.MAX_LEVEL: #Checks if character has enough to Level-up
            self.__level += 1  # Level up the character
            self.__xp -= required_experience  # Subtract level-up experience points
            
            # Level-up boosts
            self.__health += 5
            self.__damage += 2
            self.__attribute_points += self.ATTRIBUTE_POINTS_PER_LEVEL  # Allocate attribute points

            # Display level-up message with additional info
            self.show_level_up_message(screen, self.__level, 5, 2, self.ATTRIBUTE_POINTS_PER_LEVEL)
        
            required_experience = self.calculate_required_experience(self.__level + 1) # Experience required for next level
    
    def calculate_required_experience(self, level): 
        """
        Calculates requred experience for next level
        """
        return round(int(level + 10*level**1.2))
    
    def show_level_up_message(self, screen, level, health_bonus, attack_bonus, skill_points):
        """
        Displays a level-up message with additional information on the screen
        """
        font_large = pygame.font.Font(None, 74)
        font_small = pygame.font.Font(None, 36)

        # Create text surfaces
        text_level_up = font_large.render("Level Up!", True, (255, 215, 0))
        text_level = font_small.render(f"Level: {level}", True, (255, 215, 0))
        text_health_bonus = font_small.render(f"Health +{health_bonus}", True, (255, 215, 0))
        text_attack_bonus = font_small.render(f"Attack +{attack_bonus}", True, (255, 215, 0))
        text_skill_points = font_small.render(f"Skill Points +{skill_points}", True, (255, 215, 0))

        # Positioning
        screen_center = (screen.get_width() // 2, screen.get_height() // 2)
        text_rects = [
            text_level_up.get_rect(center=(screen_center[0], screen_center[1] - 60)),
            text_level.get_rect(center=(screen_center[0], screen_center[1])),
            text_health_bonus.get_rect(center=(screen_center[0], screen_center[1] + 30)),
            text_attack_bonus.get_rect(center=(screen_center[0], screen_center[1] + 60)),
            text_skill_points.get_rect(center=(screen_center[0], screen_center[1] + 90)),
        ]

        # Animation duration and fade effect
        start_time = time.time()
        duration = 3  # Duration in seconds

        while time.time() - start_time < duration:
            screen.fill((0, 0, 0))  # Clear screen
            alpha = int(255 * (1 - (time.time() - start_time) / duration))
            
            # Handle events to prevent freezing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            # Set alpha for each text surface
            text_level_up.set_alpha(alpha)
            text_level.set_alpha(alpha)
            text_health_bonus.set_alpha(alpha)
            text_attack_bonus.set_alpha(alpha)
            text_skill_points.set_alpha(alpha)

            # Blit text surfaces
            screen.blit(text_level_up, text_rects[0])
            screen.blit(text_level, text_rects[1])
            screen.blit(text_health_bonus, text_rects[2])
            screen.blit(text_attack_bonus, text_rects[3])
            screen.blit(text_skill_points, text_rects[4])

            pygame.display.flip() 

    #Player Actions
    def combat(self, screen, enemy):
        from character.actions.combat import Combat #Fuction import to stop circular importing (since combat is a child of character)
        combat_instance = Combat(screen, self, enemy) #Initialise combat
        return combat_instance.combat(self, enemy)

    def skills(self, screen, clock):
        return(self.__skills_instace.show_skill_point_screen(screen, clock))
