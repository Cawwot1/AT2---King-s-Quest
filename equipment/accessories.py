from equipment.equipment import Equipment
from abilities.ability_list import Ability_list
#QUESTION: Abtraction or No Abtraction

class Accessories(Equipment):

    #Atributes
    _defence = None
    _attack = None
    __piece = None
    _elemental_def = None
    _elemental_atk = None
    _abilities = None
    _ability_list = None
    _armour_piece = None

    def __init__(self, name, description, quality, rarity, level_req, defence, attack, piece, abilities, item_type):
        super().__init__(name, description, quality, rarity, level_req, item_type)

        self._defence = defence
        self._attack = attack
        self.__piece = piece
        self._abilities = abilities.split(" ")
        self._ability_list = []
        for ability in self._abilities:
            self._ability_list.append(getattr(Ability_list, ability))

    # Accessors

    def getDefence(self):
        return self._defence

    def getAttack(self):
        return self._attack

    def getPiece(self):
        return self.__piece
    
    def getAbilityList(self):
        return self._ability_list
    
    # Mutators

    def setDefence(self, new_defence):
        self._defence = new_defence

    def setAttack(self, new_attack):
        self._attack = new_attack
    
    def setPiece(self, new_piece):
        self.__piece = new_piece

    def setAbilityList(self, new_ability_list):
        self._abilities = new_ability_list

    #Methods

    def defence_mult(self):
        return (self._defence)

    def attack_mult(self):
        return (self._attack)

    def info(self): #Calls from Parent Class (Inherited Behaviours)
        return (f"{super().info()}\n"
                f"Defence: {self._defence}\n"
                f"Hardness: {self._attack}\n"
                f"Armour Piece: {self.__piece}\n"
                f"Abilities: {self._abilities}")
                
    #Possible Expasion ... If i have the time

    def killCounter(self):
        pass

    def upgrades(self):
        pass