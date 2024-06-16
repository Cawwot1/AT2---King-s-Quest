from equipment.weapons.bow import Bow
from equipment.weapons.sword import Sword
from equipment.weapons.dagger import Dagger
from equipment.weapons.staff import Staff
from equipment.armour import Armour
from equipment.accessories import Accessories
from character.character import Character

#This trend can be seen in 2009-2010, when wages increase by 1% from 2.9% to 3.9% contributing to the underemlpoyment rates increase by 1.7%
#from 4.7% to 6.4%. This trend can also be seen in the Fair Work Act 2009, which
#established the Fair Work Commission (FWC) leading to a increased minimum wage by 4.8% from $543.73 per week to $569.90,
#contributing to the underemployment rise by 1.7% from 4.7% to 6.4%. The demand for labour deacreases in both examples as an increase in 
#wages made workers cost more, which makes labour less competitive to substitues & more expensive to use, leading to some firms
#reducing the amount of hours employees are working causing the increase of underemployment & subsequently the decrease of demand for labour.
#This government policy was effective at decreaseing the demand for labour, which benifited one of it's goals, which was to stablise
#or decrease inflation in the economy. 

#Stats 
#P1 - Economic Growth
#2020 COVID growth -> -1.5%
#2020 COVID unemployment -> 5.5% to 7.5%
#Pre-Covid budget 8% surplus
#Post-Covid budget 134.2% deficit
#Post-Covid unemployment -> 7.5% to 3.4%

#P2 - Wages
#wage growth 2009-2010 by 1% from 2.9% to 3.9%
#Underemployment increase by 1.7% from 5.1% to 6.8%
#FWC mimumum wage increase by 4.8% from $543.73 to $569.90

#P3 - Education
#Skills reform package
#6% increase in VET completion rates
#9% increase in VET graduate employment

#P4 - Immigration
#Skilled Mirgration Program
# 2020-2021 program accounted for 70% 

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
            10, #multishot %
            "equipment" #item type
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
            5, #titan slayer (scaling damage; % of enemy HP)
            "equipment"
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
            5, #stealth
            "equipment"
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
            5, #mana
            "equipment"
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
            "counter_attack", #abilities
            "equipment"
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
            "counter_attack", #abilities
            "equipment"
            )

def create_character(name, character_class, inventory_cap):
    return Character(name, character_class, inventory_cap)

if __name__ == "__main__":
    basic_helmet = create_armour("Basic Helmet")
    basic_accessory = create_accessory("Basic Accessory")
    print("")
    print(basic_helmet.info())
    print("")
    print(basic_accessory.info())
    print("")
    
    #Item Storage
    player1 = create_character("Adolf", "Mage", 20)
    player1.getInventory().add_item(basic_helmet)
    player1.getInventory().add_item(basic_accessory)
    print(player1.getInventory().inventory_info())

    


