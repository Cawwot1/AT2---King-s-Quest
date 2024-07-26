from equipment.weapons.bow import Bow
from equipment.weapons.dagger import Dagger
from equipment.weapons.staff import Staff
from equipment.weapons.sword import Sword
from equipment.accessories import Accessories
from equipment.armour import Armour

#Factory Class
class Create_Equipment:
    
    #Weapons
    def Basic_Bow():
        return Bow("Basic Bow", #name
            "A very basic bow", #description
            "Normal", #quality
            "Common", #rarity
            0, #level req.
            10, #damage
            5, #piercing % (hardness pen)
            "bow", #weapon type
            False, #elemental weap.?
            0, #elemental damage
            "none", #element
            10, #multishot %
            "equipment" #item type
            )
    
    def Basic_Sword():
        return Sword("Basic Sword", #name
            "A very basic sword", #description
            "Normal", #quality
            "Common", #rarity
            0, #level req.
            15, #damage
            10, #piercing % (hardness pen)
            "sword", #weapon type
            False, #elemental weap.?
            0, #elemental damage
            "none", #element
            5, #titan slayer (scaling damage; % of enemy HP)
            "equipment"
            )
    
    def Basic_Dagger():
        return Dagger("Basic Dagger", #name
            "A very basic dagger", #description
            "Normal", #quality
            "Common", #rarity
            0, #level req.
            15, #damage
            10, #piercing % (hardness pen)
            "sword", #weapon type
            False, #elemental weap.?
            0, #elemental damage
            "none", #element
            5, #stealth
            "equipment"
            )

    def Basic_Staff():
        return Staff("Basic Staff", #name
            "A very basic staff", #description
            "Normal", #quality
            "Common", #rarity
            0, #level req.
            15, #damage
            10, #piercing % (hardness pen)
            "sword", #weapon type
            False, #elemental weap.?
            0, #elemental damage
            "none", #element
            5, #mana
            "equipment"
            )
    
    #Armour

    def Basic_Helment():
        return Armour("Basic Helmet", #name
            "A very basic helmet", #description
            "Normal", #quality
            "Common", #rarity
            0, #level req.
            10, #defence
            5, #hardness % (negate piercing)
            "helmet", #armour piece
            0, #elemental defence
            "counter_attack", #abilities
            "equipment"
            )
    
    #Accessories

    def Basic_Accessory():
        return Accessories("Basic Accessory", #name
            "A very basic accessory", #description
            "Normal", #quality
            "Common", #rarity
            0, #level req.
            3, #defence
            3, #attack
            "ring", #accessory piece
            "counter_attack", #abilities
            "equipment"
            )
