from equipment.equipment import Equipment
from abilities.ability_list import Ability_list
#QUESTION: Abtraction or No Abtraction

class Armour(Equipment):

    #Atributes
    _defence = None
    _hardness = None
    _elemental_def = None
    _abilities = None
    _ability_list = None
    _armour_piece = None

    def __init__(self, name, description, quality, rarity, level_req, defence, hardness, armour_piece, elemental_def, abilities, item_type):
        super().__init__(name, description, quality, rarity, level_req, item_type)
        self._defence = defence
        self._hardness = hardness
        self._armour_piece = armour_piece
        self._elemental_def = elemental_def
        self._abilities = abilities.split(" ")
        self._ability_list = []
        for ability in self._abilities:
            self._ability_list.append(getattr(Ability_list, ability))

    # Accessors

    def getDefence(self):
        return self._defence

    def getHardness(self):
        return self._hardness
    
    def getPiece(self):
        return self._armour_piece

    def getElementalDef(self):
        return self._elemental_def
    
    def getAbilitesList(self):
        return self._ability_list

    # Mutators

    def setDefence(self, new_defence):
        self._defence = new_defence

    def setHardness(self, new_hardness):
        self._hardness = new_hardness

    def setPeice(self, new_armour_piece):
        self._armour_piece = new_armour_piece

    def setElementalDef(self, new_elemental_def):
        self._elemental_def = new_elemental_def

    def setAbilities(self, new_ability_list):
        self._abilities = new_ability_list
    
    #Methods
    
    def info(self): #Calls from Parent Class (Inherited Behaviours)
        return (f"{super().info()}\n"
                f"Defence: {self._defence}\n"
                f"Hardness: {self._hardness}\n"
                f"Armour Piece: {self._armour_piece}\n"
                f"Elemental Defence: {self._elemental_def}\n"
                f"Abilities: {self._abilities}")
                
    #Possible Expasion ... If i have the time

    def killCounter(self):
        pass

    def upgrades(self):
        pass