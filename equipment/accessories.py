from equipment.equipment import Equipment
from abilities.ability_list import Ability_list
#QUESTION: Abtraction or No Abtraction

class Accessories(Equipment):

    #Atributes
    _defence = None
    _attack = None
    _acces_piece = None
    _elemental_def = None
    _elemental_atk = None
    _abilities = None
    _ability_list = None
    _armour_piece = None

    def __init__(self, name, description, quality, rarity, level_req, defence, attack, acces_piece, elemental_def, elemental_atk, abilities):
        super().__init__(name, description, quality, rarity, level_req)
        self._defence = defence
        self._attack = attack
        self._acces_piece = acces_piece
        self._elemental_def = elemental_def
        self._elemental_atk = elemental_atk
        self._abilities = abilities.split(" ")
        self._ability_list = []
        for ability in self._abilities:
            self._ability_list.append(getattr(Ability_list, ability))

    # Accessors

    def getDefence(self):
        return self._defence

    def getAttack(self):
        return self._attack

    def getAccesPiece(self):
        return self._acces_piece

    def getElementalDef(self):
        return self._elemental_def
    
    def getElementaAtk(self):
        return self._elemental_atk
    
    def getAbilityList(self):
        return self._ability_list

    # Mutators

    def setDefence(self, new_defence):
        self._defence = new_defence

    def setAttack(self, new_hardness):
        self._hardness = new_hardness
    
    def setAccesPiece(self, new_piece):
        self._acces_piece = new_piece

    def setElementalDef(self, new_elemental_def):
        self._elemental_def = new_elemental_def
    
    def setElementaAtk(self, new_element_atk):
        self._elemental_atk = new_element_atk

    def setAbilityList(self, new_ability_list):
        self._abilities = new_ability_list

    #Methods

    def defence_mult(self):
        return (self._defence, self._elemental_def)

    def attack_mult(self):
        return (self._attack, self._elemental_atk)

    def info(self): #Calls from Parent Class (Inherited Behaviours)
        return (f"{super().info()}\n"
                f"Defence: {self._defence}\n"
                f"Hardness: {self._attack}\n"
                f"Armour Piece: {self._acces_piece}\n"
                f"Elemental Defence: {self._elemental_def}\n"
                f"Elemental Attack: {self._elemental_atk}\n"
                f"Abilities: {self._abilities}")
                
    #Possible Expasion ... If i have the time

    def killCounter(self):
        pass

    def upgrades(self):
        pass