class Ability_list():
    
    #Atributes
    _ability_name = None
    
    def __init__(self, ability_name):
       self._ability_name = ability_name
    
    # Accessors for abilities

    def getAbilityName(self):
        return self._ability_name

    # Mutators for abilities

    def setAbilityName(self, new_name):
        self._ability_name = new_name

    # Behaviours

    def counter_attack(): #add more later
        return("counter attack")
