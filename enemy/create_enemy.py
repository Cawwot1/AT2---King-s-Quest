from enemy.enemy import Enemy

#Factory Class
class Create_Enemy():
    #Behaviors -> Preset Enemy Stats
    def Bandit():
        return Enemy(
            20, #Health
            5, #Attack
            30, #Defence (negatges __ % dmg)
            10, #Speed
            "level1", #Type
            "Bandit", #Name
            "assets/enemies/bandit.png", #enemy sprite
            20 #exp given when defeated
        )
    
    def Goblin():
        return Enemy(
            10, #Health
            2, #Attack
            15, #Defence
            5, #Speed
            "level1", #Type
            "Goblin", #Name
            "assets/enemies/goblin.png",
            10
        )

    def Zombie():
        return Enemy(
            30, #Health
            3, #Attack
            0, #Defence
            1, #Speed
            "level1", #Type
            "Zombie", #Name
            "assets/enemies/zombie.png",
            20
        )
    
    def Boss_boar():
        return Enemy(
            200, #Health
            5, #Attack
            10, #Defence
            10, #Speed
            "Boss", #Type
            "Boss Boar", #Name
            "assets/enemies/boss_boar.png",
            150
        )
    
    def MMmole():
        return Enemy(
            400, #Health
            10, #Attack
            10, #Defence
            5, #Speed
            "Boss", #Type
            "MMmole", #Name
            "assets/enemies/MMmole.png",
            450
        )
