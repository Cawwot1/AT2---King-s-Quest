import pygame
from enemy.create_enemy import Create_Enemy

class Map_dungeon:
    """
    Map/Area 3 -> Dungeon
    """

    # Attributes
    __area_level = None
    __enemies = None
    __bosses = None
    __map_sprite = None
    __num_of_enemies = None

    # Constructor
    def __init__(self):
        self.setNum_of_enemies(20)
        self.setArea_level(3)
        self.setEnemies([
            Create_Enemy.Bandit(),   # Create instances #UPDAATE LATTTTER
            Create_Enemy.Goblin(),   # Create instances
            Create_Enemy.Zombie()    # Create instances
        ])
        self.setBosses([Create_Enemy.MMmole()]) # Update Later
        self.map_image = pygame.image.load('assets/mud_map.png').convert_alpha()
        self.map_width, self.map_height = self.map_image.get_size()

    # Getters
    def getNum_of_enemies(self):
        return self.__num_of_enemies
    def getArea_level(self):
        return self.__area_level
    def getEnemies(self):
        return self.__enemies
    def getBosses(self):
        return self.__bosses
    def getMap_sprite(self):
        return self.map_image
    def get_map_size(self):
        return self.map_width, self.map_height

    # Setters
    def setArea_level(self, area_level):
        self.__area_level = area_level
    def setEnemies(self, enemies):
        self.__enemies = enemies
    def setBosses(self, bosses):
        self.__bosses = bosses
    def setNum_of_enemies(self, num_of_enemies):
        self.__num_of_enemies = num_of_enemies
        
    # Behaviours
