from equipment.equipment import Equipment
from abilities.ability_list import Ability_list
#QUESTION: Abtraction or No Abtraction

class Accessories(Equipment):

    #Atributes
    __defence = None
    __attack = None
    __piece = None
    __abilities = None
    __ability_list = None

    def __init__(self, name, description, quality, rarity, level_req, defence, attack, piece, abilities, item_type):
        super().__init__(name, description, quality, rarity, level_req, item_type)

        self.setDefence(defence)
        self.setAttack(attack)
        self.setPiece(piece)
        self.setAbilities(abilities.split(" "))
        self.setAbility_list([])
        
        for ability in self.__abilities:
            self.__ability_list.append(getattr(Ability_list, ability))

    #Getters
        #Stats
    def getDefence(self): return self.__defence
    def getAttack(self): return self.__attack
        #Other
    def getPiece(self): return self.__piece
    def getAbilities(self): return self.__abilities
    def getAbility_list(self): return self.__ability_list

    # Setters
        #Stats
    def setDefence(self, defence):
        self.__defence = defence
    def setAttack(self, attack):
        self.__attack = attack
        #Other
    def setPiece(self, piece):
        self.__piece = piece
    def setAbilities(self, abilities):
        self.__abilities = abilities
    def setAbility_list(self, ability_list):
        self.__ability_list = ability_list

    #Behaviours
    def defence_mult(self):
        return (self.__defence)

    def attack_mult(self):
        return (self.__attack)

    def info(self): #Calls from Parent Class (Inherited Behaviours)
        return (f"{super().info()}\n"
                f"Defence: {self.__defence}\n"
                f"Hardness: {self.__attack}\n"
                f"Armour Piece: {self.__piece}\n"
                f"Abilities: {self.__abilities}")