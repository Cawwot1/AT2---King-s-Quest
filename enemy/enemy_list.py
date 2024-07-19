#Factory Class
class Enemy_list:  

    #Atribtues
    __level1_enemies = None
    __level2_enemies = None
    __level3_enemies = None
    __mini_bosses = None
    __bosses = None

    #List Orginisation
    __all_enemies = None
    
    def __init__(self):
        self.setLevel1_enemies = []
        self.setLevel2_enemies = []
        self.setLevel3_enemies = []
        self.setMini_bosses = []
        self.setBosses = []
        self.setAll_enemies = []

    #Getters
    def getLevel1_enemies(self):
        return self.__level1_enemies
    def getLevel2_enemies(self):
        return self.__level2_enemies
    def getLevel3_enemies(self):
        return self.__level3_enemies
    def getMini_bosses(self):
        return self.__mini_bosses
    def getBosses(self):
        return self.__bosses
    def getAll_enemies(self):
        return self.__all_enemies

    
    #Mutators
    def setLevel1_enemies(self, level1_enemies):
        self.__level1_enemies.append(level1_enemies)   
    def setLevel2_enemies(self, level2_enemies):
        self.__level2_enemies.append(level2_enemies)
    def setLevel3_enemies(self, level3_enemies):
        self.__level3_enemies.apend(level3_enemies)
    def setMini_bosses(self, mini_bosses):
        self.__mini_bosses.append(mini_bosses)
    def setBosses(self, bosses):
        self.__bosses.append(bosses)
    def setAll_enemies(self, all_enemies):
        self.__all_enemies = all_enemies

    #Behaviours
    def add_enemy(self, enemy, enemy_type):
        if enemy_type == 'level1':
            self.__level1_enemies.append(enemy)
        elif enemy_type == 'level2':
            self.__level2_enemies.append(enemy)
        elif enemy_type == 'level3':
            self.__level3_enemies.append(enemy)
        elif enemy_type == 'Mini_Boss':
            self.__mini_bosses.append(enemy)
        elif enemy_type == "Boss":
            self.__bosses.append(enemy)
        else:
            return("Invalid Input") #error check
    
    def world_level_up(self):
        for lists in self.__all_enemies:
            for enemy in lists:
                enemy.setEnemy_hp(enemy.getEnemy_hp() * 1.25)
                enemy.setEnemy_attack(enemy.getEnemy_attack() * 1.25)
                enemy.setEnemy_speed(enemy.getEnemy_speed() * 1.25)
    
    
        
