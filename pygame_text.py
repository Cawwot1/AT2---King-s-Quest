from equipment.weapons.bow import Bow
from equipment.weapons.sword import Sword
from equipment.weapons.dagger import Dagger
from equipment.weapons.staff import Staff
from equipment.armour import Armour
from equipment.accessories import Accessories

def create_bow(selection):
    if selection == "Basic Bow":
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
            10 #multishot %
            )

def create_sword(selection):
    if selection == "Basic Sword":
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
            5 #titan slayer (scaling damage; % of enemy HP)
            )

def create_dagger(selection):
    if selection == "Basic Dagger":
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
            5 #stealth
            )

def create_staff(selection):
    if selection == "Basic Staff":
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
            5 #mana
            )

def create_armour(selection):
    if selection == "Basic Helmet":
            return Armour("Basic Helmet", #name
            "A very basic helmet", #description
            "Normal", #quality
            "Common", #rarity
            0, #level req.
            10, #defence
            5, #hardness % (negate piercing)
            "helmet", #armour piece
            0, #elemental defence
            "counter_attack" #abilities
            )

def create_accessory(selection):
    if selection == "Basic Accessory":
        return Accessories("Basic Accessory", #name
            "A very basic accessory", #description
            "Normal", #quality
            "Common", #rarity
            0, #level req.
            3, #defence
            3, #attack
            "ring", #accessory piece
            0, #elemental defence
            0, #elemental attack
            "counter_attack" #abilities
            )

if __name__ == "__main__":
    basic_helmet = create_armour("Basic Helmet")
    basic_accessory = create_accessory("Basic Accessory")
    print("")
    print(basic_helmet.info())
    print("")
    print(basic_accessory.info())
    


