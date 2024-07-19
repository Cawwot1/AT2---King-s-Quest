from enemy.enemy_list import Enemy_list

class map_woodlands:
    
    # Attributes
    __area_level = None
    __enemies = None
    __bosses = None

    # Constructor
    def __init__(self):
        self.setArea_level(1)
        self.setEnemies(Enemy_list.getLevel1_enemies)
        self.setBosses()

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