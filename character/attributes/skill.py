#BASIC ATRIBUTES -> UPDRADE WITH MORE EPIC NAMES

class Skill():
    
    #Atributes
    _atri_attack = None
    _atri_defence = None
    _atri_speed = None

    #Constructor    
    def __init__(self, attack, defence, speed): #requests input (into constr.) for name & cha. class
        super().__init__(attack, defence, speed)
        self._atri_attack = 2
        self._atri_defence = 2
        self._atri_speed = 2

    # Accessors
    def getAtri_atk(self):
        return self._atri_attack

    def getAtri_def(self):
        return self._atri_defence

    def getAtri_speed(self):
        return self._atri_speed

    # Mutators

    def setArti_atk(self, new_attack):
        self._atri_attack = new_attack

    def setAtri_def(self, new_defence):
        self._atri_defence = new_defence
    
    def setArti_spd(self, new_speed):
        self._atri_speed = new_speed
    
    #Behaviours -> To Be Improved

    def boost_attack(self, points):
        return self._atri_attack * points
    
    
    def boost_defence(self, points):
        return self._atri_attack * points

    def boost_speed(self, points):
        return self._atri_attack * points