from enemy.enemy import Enemy

class Create_Enemy():

    __selection = None

    def __init__(self):
        self.__selection = None
    
    # Accessors
    def getSelection(self):
        return self.__selection
    
    #Mutators
    def setSelection(self, new_selection):
        self.__selection = new_selection
    
    #Behaviors -> Preset Enemy Stats

    def Bandit():
        return Enemy(
            20, #Health
            5, #Attack
            30, #Defence (negatges __ % dmg)
            10, #Speed
            "level1", #Type
            "Bandit" #Name
        )
    
    def Goblin():
        return Enemy(
            10, #Health
            2, #Attack
            15, #Defence
            5, #Speed
            "level1", #Type
            "Goblin" #Name
        )

    def Zombie():
        return Enemy(
            30, #Health
            3, #Attack
            0, #Defence
            1, #Speed
            "level1", #Type
            "Zombie" #Name
        )
