from equipment.weapons.bow import Bow
from equipment.weapons.sword import Sword
from equipment.weapons.dagger import Dagger
from equipment.weapons.staff import Staff
from equipment.armour import Armour
from equipment.accessories import Accessories
from character.character import Character
from item_management.inventory import Inventory
from maps.woodlands import map_woodlands

import random
from random import randint
import math
import time
import sys

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

def loading_line(duration):

    """
    Loading Timer
    """

    length = 50  # Length of the loading line
    interval = duration / length  # Time interval for each step
    
    for i in range(length):
        # Print the loading line progress
        sys.stdout.write(f'\r[{"=" * i}{" " * (length - i)}] {int((i / length) * 100)}%')
        sys.stdout.flush()
        time.sleep(interval)
    
    # Complete the loading line
    sys.stdout.write(f'\r[{"=" * length}] 100%\n')
    sys.stdout.flush()

def searching_animation():
    start_time = time.time()
    duration = randint(5, 15)
    while (time.time() - start_time) <= duration:
        for char in ['.', '..', '...']:
            sys.stdout.write(f'\r{char}')
            sys.stdout.flush()
            time.sleep(0.5)  # Adjust the delay time as needed
    sys.stdout.write('\r...')  # Ensure to overwrite the last printed chars with final output
    sys.stdout.flush()

###FIX
def searching_animation():
    start_time = time.time()
    duration = randint(5, 15)
    while (time.time() - start_time) <= duration:
        for char in ['.', '..', '...']:
            sys.stdout.write('\r   ')  # Write blank spaces to clear previous output
            sys.stdout.flush()
            time.sleep(0.5)  # Delay before showing the next character
            sys.stdout.write(f'\r{char}')
            sys.stdout.flush()
            time.sleep(0.5)  # Adjust the delay time as needed
    sys.stdout.write('\r   ')  # Clear the last printed chars
    sys.stdout.flush()


def text_game():
    #THINGS TO DO
    #1. Fix my "OR" in my if Statements
    
    #Game Sections
    character_naming = True
    class_selection = True
    introduction = True
    game_running = True
    in_game = True

    #Other
    player_list = []
    selected_player = None

    print("\n\033[1mGame Started\033[0m\n")
    print("Loading Game Assets...")
    print(f"{loading_line(3)}\n")
    print("Loading Characters...")
    print(f"{loading_line(5)}\n") 
    print(f"Loading Equipment...")
    print(f"{loading_line(1)}")
    print("\nLoading Finished, Game Started\n")

    while game_running == True:
        
        #Character Naming
        while character_naming == True:
            character_name = input("Character Name: ")
            name_confirm = input(f"Your Name is {character_name}, Confirm? (y/n): ")
            if name_confirm.lower() == "y":
                print(f"Your Name is \033[1m{name_confirm}\033[0m\n")
                character_naming = False
            else:
                print(f"Name was not cofirmed\n")

        while class_selection == True: #Class Selection
            #ADD VALIDATION PROCESS
            print("Class Options")
            print("1. Mage")
            print("2. Warrior")
            print("3. Archer")
            print("4. Rogue\n")
            class_select = input("Please select your character Class: ")
            if class_select.lower() in ["1", "mage"]:
                class_select = "Mage"
                class_selection = False
            elif class_select.lower() in ["2", "warrior"]:
                class_select = "Warrior"
                class_selection = False
            elif class_select.lower() in ["3", "archer"]:
                class_select = "Archer"
                class_selection = False
            elif class_select.lower() in ["4", "rogue"]:
                class_select = "Rogue"
                class_selection = False
            else:
                print("Invalid Input")
            if class_selection == False:
                player_list.append(create_character(character_name, class_select, 20)) #name, class, inventory size
                print(f"\nPlayer Created\n"
                      f"Name: {character_name}\n"
                      f"Class: {class_select}\n")
                selected_player = player_list[-1]

        #Item Testing (Temporary)
        basic_helmet = create_armour("Basic Helmet")
        basic_staff = create_staff("Basic Staff")
        basic_accessory = create_accessory("Basic Accessory")
        selected_player.getInventory().add_item(basic_accessory)
        selected_player.getInventory().add_item(basic_staff)
        selected_player.getInventory().add_item(basic_helmet)
        
        while introduction == True:
            print("Welcome to the Game")
            print("This is the starting screen (added later in visuals)")
            do_tutorial = input("Would you like to do the tutorial? (y/n): ")
            if do_tutorial.lower() == "y":
                print("\nWelcome to the tutorial")
                print("This is the basic UI to control the game")
                print("----------------------------------------")
            else:
                introduction = False
        while in_game == True:
            print("\nPlayer Actions")
            print("1. Player Inventory")
            print("2. Player Explore")
            print("3. Player Equipment")   
            print("4. Quit\n")    
            player_choice = input("Please input your choice: ")
            if player_choice.lower() in ["1", "player inventory"]:
                print("\nInventory")
                print("1. View Item")
                print("2. Remove Item\n")
                inventory_choice = input("Please input your choice: ")
                if inventory_choice.lower() in ["1", "view item"]:
                    print(f"{character_name}'s Inventory")
                    print(f"\n{selected_player.getInventory().inventory_info()}")
                    view_choice = input("Please input what item you want to view: ") #input item name CAPS SENSITIVE
                    item = selected_player.getInventory().find_item(view_choice) #checks if item is in player inventory
                    if item == False:
                        print("Item not found in inventory\n")
                    else:
                        print(f"\nName: {item.getName()}\n")
                        if item.getItemType() == "equipment": #CHANGE LATER WHEN MORE INVENTORY CATEGORIES ARE ADDED
                            print(f"Description: {item.getDescription()}\n"
                                  f"Quality: {item.getQuality()}\n"
                                  f"Rarity: {item.getRarity()}\n"
                                  f"Level Requrements: {item.getLevelReq()}\n"
                                  f"Item Type: {item.getItemType()}\n")
            if player_choice.lower() in ["2", "player explore"]:
                print(f"Exploring {searching_animation()}")
                explore_choice = random.choice(["Fight", "Resources", "Event"])
                if explore_choice == "Fight":
                    print("Entered Combat")
                    player_area = selected_player.getMap()
                    enemy = random.choice(player_area.getEnemies()) #chooses a random object from list of enemies
                    print(f"You are fighting {enemy}")
                elif explore_choice == "Resources":
                    pass
                elif explore_choice == "Event":
                    pass
                else:
                    print("Invalid Input")
                

                        
#Model / Examples
    """
    #Item Creation
    basic_helmet = create_armour("Basic Helmet")
    basic_staff = create_staff("Basic Staff")
    basic_accessory = create_accessory("Basic Accessory")
    print(f"\n{basic_helmet.info()}")
    print(f"\n{basic_accessory.info()}")
    
    #Player Creation
    player1 = create_character("Adolf", "Mage", 20)
    
    #Inventory
    player1.getInventory().add_item(basic_accessory)
    player1.getInventory().add_item(basic_staff)
    print(f"\n{player1.getInventory().inventory_info()}")

    #Equip
    player1.equip_armour(basic_helmet)

    #Player Experience & Level Up
    player1.gain_experience(100)
    """


