from item_management.inventory import Inventory
from character.attributes.skill import Skill
import random

class Character():
    
    #Atributes
    
    #Other
    _name = None
    _character_class = None

    #Combat
    _speed = None
    _health = None
    _defence = None
    
    #Progression
    _Level = None
    _xp = None
    _attribute_points = None

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
        self._equipped_ring = None
        self._equipped_necklace = None
        self._equipped_helmet = None
        self._equipped_chestplate = None
        self._equipped_legs = None
        self._equipped_boots = None
        self._equipped_weapon = None

        #preset atribute values
        self._level = 1  # Character's current level
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

        #Other

    #UP TO HERE ###########

    def getInventory(self):
        return self.__inventory

    def assign_attribute_points(self, attribute, points): #Basic Skills
        if attribute == "attack":
            self._skill_attack = Skill.boost_attack(points)
        elif attribute == "defence":
            self._skill_defence = Skill.boost_defence(points)
        elif attribute == "speed":
            self._skill_speed = Skill.boost_speed(points)
        else:
            print(f"Error: Attribute '{attribute}' does not exist.")

    def equip_weapon(self, weapon_object):
        if self._equipped_weapon: #if equipped_weap true
            user_input = input(f"{self._equipped_weapon.name} is equipped, do you want to replace? (y/n)")
            if user_input.lower() != "y":
                print("Action Cancelled")
                return

        self._equipped_weapon = weapon_object
        print(f"{weapon_object} equipped")

    def equip_armour(self, armour_object): ### IS THIS ALLOWED (having a dictionary here)???
        
        piece_equipped = {
            "helmet": self._equipped_helmet,
            "chestplate": self._equipped_chestplate,
            "legs": self._equipped_legs,
            "boots": self._equipped_boots}
        armour_piece = armour_piece(armour_object.getPiece())
        
        if piece_equipped: #if piece_equipped true
            user_input = input(f"{piece_equipped.getName()} is equipped, do you want to replace? (y/n)")
            if user_input.lower() != "y":
                print("Action Cancelled")
                return
        piece_equipped = armour_object
        print(f"{armour_object} equipped")

    def equip_accessory(self, accessory_object):
        acc_equipped = {
            "ring": self._equipped_ring,
            "necklace": self._equipped_necklace}
        acc_equipped = acc_equipped(accessory_object.getAccesPiece())

        if acc_equipped: #if acc_piece true
            user_input = input(f"{accessory_object.getName()} is equipped, do you want to replace? (y/n)")
            if user_input.lower() != "y":
                print("Action Cancelled")
                return
        acc_equipped = accessory_object
        print(f"{accessory_object} equipped")

    def attack(self, enemy_defence, enemy_hardness):
        isCrit = random.random() < self.crit_chance/100
        
    def equipment_stats(self):
        #Offence
        offence_items = [self._equipped_weapon, self._equipped_necklace, self._equipped_ring]
        raw_damage = sum(item.getDamage() for item in offence_items)
        piercing = sum(item.getPiercing() for item in offence_items)
        elemental_damage = self._equipped_weapon.getElementDamage() + self._equipped_necklace.getElementalAtk()
        weapon_element = self._equipped_weapon.getElement()
        #Defence
        defence_items = [self._equipped_helmet, self._equipped_chestplate, self._equipped_legs, self._equipped_boots, self._equipped_necklace, self._equipped_ring]
        raw_defence = sum(item.getDefence() for item in defence_items)
        hardness = self._equipped_helmet.getHardness() + self._equipped_chestplategetHardness() + self._equipped_legs.getHardness() + self._equipped_boots.getHardness() 
        elemental_defence = sum(item.getElementalDef() for item in defence_items)

    def gain_experience(self, experience):
        self.experience_points += experience  # Increase character's experience points
        # Calculate experience required for next level
        required_experience = self.calculate_required_experience(self.level + 1)
        # Check if character has enough experience to level up and is below the level cap
        while self.experience_points >= required_experience and self.level < self.MAX_LEVEL:
            self.level += 1  # Level up the character
            self.experience_points -= required_experience  # Decrease character's experience points
            self.hit_points += 10  # Example: Increase hit points by 10 each level up
            self.attribute_points += self.ATTRIBUTE_POINTS_PER_LEVEL  # Allocate attribute points
            print(f"Level up! {self.name} is now level {self.level}.")
            # Calculate experience required for next level
            required_experience = self.calculate_required_experience(self.level + 1)

    def calculate_required_experience(self, level):
        # Example exponential scaling: Each level requires 100 more experience points than the previous level
        return int(100 * (1.5 ** (level - 1)))

    def is_alive(self):
        return self.hit_points > 0

    def take_damage(self, amount):
        # Calculate the actual damage taken, taking into account the character's armor
        actual_damage = max(0, amount - self.armor)
        self.hit_points -= actual_damage
        if self.hit_points <= 0:
            print(f"{self.name} takes {actual_damage} damage and has been defeated!")
        else:
            print(f"{self.name} takes {actual_damage} damage. Remaining hit points: {self.hit_points}")
