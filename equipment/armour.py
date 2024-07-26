from equipment.equipment import Equipment
from abilities.ability_list import Ability_list
#QUESTION: Abtraction or No Abtraction

class Armour(Equipment):

    #Atributes
    __defence = None
    __hardness = None
    __elemental_def = None
    __abilities = None
    __ability_list = None
    __armour_piece = None

    #Constructor
    def __init__(self, name, description, quality, rarity, level_req, defence, hardness, armour_piece, elemental_def, abilities, item_type):
        super().__init__(name, description, quality, rarity, level_req, item_type)
            #Stats
        self.setDefence(defence)
        self.setHardness(hardness)
        self.setElemental_def(elemental_def)
            #Other
        self.setAbilities(abilities.split(" "))
        self.setAbility_list([])
        self.setArmour_piece(armour_piece)

        for ability in self.__abilities:
            self.__ability_list.append(getattr(Ability_list, ability))

    #Getters
        #Stats
    def getDefence(self): return self.__defence
    def getHardness(self): return self.__hardness
    def getElemental_def(self): return self.__elemental_def
        #Other
    def getAbilities(self): return self.__abilities
    def getAbility_list(self): return self.__ability_list
    def getArmour_piece(self): return self.__armour_piece

    #Setters
    def setDefence(self, defence): self.__defence = defence
    def setHardness(self, hardness): self.__hardness = hardness
    def setElemental_def(self, elemental_def): self.__elemental_def = elemental_def
    def setAbilities(self, abilities): self.__abilities = abilities
    def setAbility_list(self, ability_list): self.__ability_list = ability_list
    def setArmour_piece(self, armour_piece): self.__armour_piece = armour_piece