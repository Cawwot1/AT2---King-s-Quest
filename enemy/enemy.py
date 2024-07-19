class Enemy:

    #atributes
    __enemy_hp = None
    __enemy_attack = None
    __enemy_speed = None  
    __enemy_type = None  

    #Contructor
    def __init__(self, enemy_hp, enemy_attack, enemy_speed, enemy_type):
        self.setEnemy_hp(enemy_hp)
        self.setEnemy_attack(enemy_attack)
        self.setEnemy_speed(enemy_speed)
        self.setEnemy_type(enemy_type)
    
    # Getters
    def getEnemy_hp(self):
        return self.__enemy_hp
    def getEnemy_attack(self):
        return self.__enemy_attack
    def getEnemy_speed(self):
        return self.__enemy_speed 
    def getEnemy_type(self):
        return self.__enemy_type


    # Mutators
    def setEnemy_hp(self, enemy_hp):
        self.__enemy_hp = enemy_hp

    def setEnemy_attack(self, enemy_attack):
        self.__enemy_attack = enemy_attack

    def setEnemy_speed(self, enemy_speed):
        self.__enemy_speed = enemy_speed

    def setEnemy_type(self, enemy_type):
        self.__enemy_type = enemy_type