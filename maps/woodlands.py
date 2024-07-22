from enemy.create_enemy import Create_Enemy

class Map_Woodlands:
    """
    Map/Area 1 -> Woodlands
    """

    # Attributes
    __area_level = None
    __enemies = None
    __bosses = None

    # Constructor
    def __init__(self):
        self.setArea_level(1)
        self.setEnemies([
            Create_Enemy.Bandit(),   # Create instances
            Create_Enemy.Goblin(),   # Create instances
            Create_Enemy.Zombie()    # Create instances
        ])
        self.setBosses(None) #Update Later

    # Getters
    def getArea_level(self):
        return self.__area_level
    def getEnemies(self):
        return self.__enemies
    def getBosses(self):
        return self.__bosses

    # Setters
    def setArea_level(self, area_level):
        self.__area_level = area_level
    def setEnemies(self, enemies):
        self.__enemies = enemies
    def setBosses(self, bosses):
        self.__bosses = bosses