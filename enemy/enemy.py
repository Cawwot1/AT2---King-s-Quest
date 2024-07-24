class Enemy:

    #atributes
    __enemy_hp = None
    __enemy_attack = None
    __enemy_speed = None  
    __enemy_type = None
    __enemy_name = None
    __enemy_defence = None
    __enemy_image = None
    __enemy_exp = None 

    #Contructor
    def __init__(self, enemy_hp, enemy_attack, enemy_defence, enemy_speed, enemy_type, enemy_name, enemy_image, enemy_exp):
        self.setEnemy_hp(enemy_hp)
        self.setEnemy_attack(enemy_attack)
        self.setEnemy_speed(enemy_speed)
        self.setEnemy_type(enemy_type)
        self.setEnemy_name(enemy_name)
        self.setEnemy_defence(enemy_defence)
        self.setEnemy_image(enemy_image)
        self.setEnemy_exp(enemy_exp)

        
    
    # Getters
    def getEnemy_hp(self):
        return self.__enemy_hp
    def getEnemy_attack(self):
        return self.__enemy_attack
    def getEnemy_speed(self):
        return self.__enemy_speed 
    def getEnemy_type(self):
        return self.__enemy_type
    def getEnemy_name(self):
        return self.__enemy_name
    def getEnemy_defence(self):
        return self.__enemy_defence
    def getEnemy_image(self):
        return self.__enemy_image
    def getEnemy_exp(self):
        return self.__enemy_exp


    # Mutators
    def setEnemy_hp(self, enemy_hp):
        self.__enemy_hp = enemy_hp
    def setEnemy_attack(self, enemy_attack):
        self.__enemy_attack = enemy_attack
    def setEnemy_speed(self, enemy_speed):
        self.__enemy_speed = enemy_speed
    def setEnemy_type(self, enemy_type):
        self.__enemy_type = enemy_type
    def setEnemy_name(self, enemy_name):
        self.__enemy_name = enemy_name
    def setEnemy_defence(self, enemy_defence):
        self.__enemy_defence = enemy_defence
    def setEnemy_image(self, enemy_image):
        self.__enemy_image = enemy_image
    def setEnemy_exp(self, enemy_exp):
        self.__enemy_exp = enemy_exp