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

    #Why are these caps?
    MAX_LEVEL = 50  # Maximum level a character can reach
    ATTRIBUTE_POINTS_PER_LEVEL = 3  # Number of attribute points gained per level

    #Conctructor
    def __init__(self, name, character_class, atri_attack, atri_defence, atri_speed): #requests input (into constr.) for name & cha. class
        super().__init__(atri_attack, atri_defence, atri_speed)      
        self._name = name
        self._character_class = character_class
        
        #Skills
        self._skill_attack = 0
        self._skill_defence = 0
        self._skill_speed = 0

        #preset atribute values
        self._level = 1  # Character's current level
        self._attack = 10
        self._speed = 10
        self._xp = 0  # Character's current experience points
        self._health = 100  # Example starting value for character's hit points
        self._defence = 10  # Example starting value for character's armor class
        self._skills = []  # Example empty dictionary for character's skills
        self.inventory = []  # Example empty list for character's inventory
        self.gold = 0  # Example starting value for character's gold
        self.attribute_points = 0  # Attribute points available to allocate
        self.crit_chance = 10 #percent (%)
        self.crit_damage = 50 #precent (%)

    #UP TO HERE ###########

    def assign_attribute_points(self, attribute, points): #Basic Skills
        if attribute == "attack":
            self._skill_attack = Skill.boost_attack(points)
        elif attribute == "defence":
            self._skill_defence = Skill.boost_defence(points)
        elif attribute == "speed":
            self._skill_speed = Skill.boost_speed(points)
        else:
            print(f"Error: Attribute '{attribute}' does not exist.")

    def attack(self, enemy_defence):
        isDouble_hit = random.random() < self._speed/200
        isCrit = random.random() < self.crit_chance/100
        
        #Double Hit Calculator
        if isDouble_hit == True:
            dub_dmg_mult = 2
        else:
            dub_dmg_mult = 1
        
        #Crit Chance
        if isCrit == True:
            crit_dmg_mult = 1 + self.crit_damage/100
        else:
            crit_dmg_mult = 1

        character_damage = (self.attack + self._skill_attack) * crit_dmg_mult * isDouble_hit
        weapon_damage = ()
        artifact_damage =()
        
        return (character_damage + weapon_damage + artifact_damage)

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
