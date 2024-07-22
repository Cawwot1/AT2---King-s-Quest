import pygame
import random
import sys
import time
from game_run.settings import *
from equipment.weapons.bow import Bow
from equipment.weapons.sword import Sword
from equipment.weapons.dagger import Dagger
from equipment.weapons.staff import Staff
from equipment.armour import Armour
from equipment.accessories import Accessories
from equipment.create_equipment import Create_Equipment
from character.character import Character
from item_management.inventory import Inventory
from maps.woodlands import Map_Woodlands

#Player Actions
from character.actions.explore import Explore

class Game:
    # Attributes
    __screen = None
    __clock = None
    __running = None
    __all_sprites = None

    # Game Sections
    __main_menu = None
    __char_naming = None
    __class_selection = None
    __introduction = None
    __in_game = None

    #Instances (player actions)
    __explore_instance = None
    

    # Player
    __player_list = None
    __selected_player = None
    __class_select = None
    __char_name = None

    # Other
    __player_choice = None

    def __init__(self):
        # Pygame config
        pygame.init()
        self.setScreen(pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
        pygame.display.set_caption(TITLE)
        self.setClock(pygame.time.Clock())
        self.setRunning(True)
        self.setAll_sprites(pygame.sprite.Group())

        # Game Sections
        self.setMain_menu(True)
        self.setChar_naming(False)
        self.setClass_selection(False)
        self.setIntroduction(False)
        self.setIn_game(False)

        self.setExplore_instance(Explore(self.getScreen()))
        
        # Player
        self.setPlayer_list([])
        self.setSelected_player(None)
        self.setClass_select(None)
        self.setChar_name("")

        # Other
        self.setPlayer_choice(None)

    # Getters
    def getScreen(self):
        return self.__screen
    def getClock(self):
        return self.__clock
    def getRunning(self):
        return self.__running
    def getAll_sprites(self):
        return self.__all_sprites
    def getMain_menu(self):
        return self.__main_menu
    def getChar_naming(self):
        return self.__char_naming
    def getClass_selection(self):
        return self.__class_selection
    def getIntroduction(self):
        return self.__introduction
    def getIn_game(self):
        return self.__in_game
    def getPlayer_list(self):
        return self.__player_list
    def getSelected_player(self):
        return self.__selected_player
    def getClass_select(self):
        return self.__class_select
    def getChar_name(self):
        return self.__char_name
    def getPlayer_choice(self):
        return self.__player_choice
    def getExplore_instance(self):
        return self.__explore_instance
    
        
    # Setters
    def setScreen(self, screen):
        self.__screen = screen
    def setClock(self, clock):
        self.__clock = clock
    def setRunning(self, running):
        self.__running = running
    def setAll_sprites(self, all_sprites):
        self.__all_sprites = all_sprites
    def setMain_menu(self, main_menu):
        self.__main_menu = main_menu
    def setChar_naming(self, char_naming):
        self.__char_naming = char_naming
    def setClass_selection(self, class_selection):
        self.__class_selection = class_selection
    def setIntroduction(self, introduction):
        self.__introduction = introduction
    def setIn_game(self, in_game):
        self.__in_game = in_game
    def setPlayer_list(self, player_list):
        self.__player_list = player_list
    def setSelected_player(self, selected_player):
        self.__selected_player = selected_player
    def setClass_select(self, class_select):
        self.__class_select = class_select
    def setChar_name(self, char_name):
        self.__char_name = char_name
    def setPlayer_choice(self, player_choice):
        self.__player_choice = player_choice
    def setExplore_instance(self, explore_instance):
        self.__explore_instance = explore_instance

    # Behaviours
    def create_character(self, name, character_class, inventory_cap):
        return Character(name, character_class, inventory_cap)

    def loading_line(self, duration):
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

    def run(self):
        while self.__running:
            self.events()
            self.update()
            self.draw()
            self.__clock.tick(FPS)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.setRunning(False)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.setRunning(False)
                if self.__main_menu:
                    self.main_menu_events(event)
                elif self.__char_naming:
                    self.character_naming_events(event)
                elif self.__class_selection:
                    self.class_selection_events(event)
                elif self.__in_game:
                    self.in_game_events(event)

    def update(self):
        self.__all_sprites.update()

    def draw(self):
        self.__screen.fill(BG_COLOR)
        if self.__main_menu:
            self.draw_main_menu()
        elif self.__char_naming:
            self.draw_character_naming()
        elif self.__class_selection:
            self.draw_class_selection()
        elif self.__in_game:
            self.draw_in_game()
        pygame.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(pygame.font.match_font(FONT_NAME), size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.__screen.blit(text_surface, text_rect)

    def draw_main_menu(self):
        self.draw_text("Main Menu", 36, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Press Enter to Start", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30)
        self.draw_text("Press C for Credits", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("Press Q to Quit", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30)

    def main_menu_events(self, event):
        if event.key == pygame.K_RETURN:
            self.setMain_menu(False)
            self.setChar_naming(True)
        elif event.key == pygame.K_c:
            self.show_credits()
        elif event.key == pygame.K_q:
            self.setRunning(False)

    def character_naming_events(self, event):
        if event.key == pygame.K_BACKSPACE:
            self.setChar_name(self.__char_name[:-1])
        elif event.key == pygame.K_RETURN:
            self.setClass_selection(True)
            self.setChar_naming(False)
        elif event.key == pygame.K_TAB:
            self.setChar_name(self.__char_name + ' ')
        else:
            self.setChar_name(self.__char_name + event.unicode)

    def class_selection_events(self, event):
        if event.key == pygame.K_1:
            self.setClass_select("Mage")
            self.setClass_selection(False)
            self.setIn_game(True)
        elif event.key == pygame.K_2:
            self.setClass_select("Warrior")
            self.setClass_selection(False)
            self.setIn_game(True)
        elif event.key == pygame.K_3:
            self.setClass_select("Archer")
            self.setClass_selection(False)
            self.setIn_game(True)
        elif event.key == pygame.K_4:
            self.setClass_select("Rogue")
            self.setClass_selection(False)
            self.setIn_game(True)
        
        #Creates Character
        self.setSelected_player(self.create_character(self.__char_name, self.__class_select, 30))

    def in_game_events(self, event):
        if event.key == pygame.K_1:
            self.show_inventory()
        elif event.key == pygame.K_2:
            explore_result = self.__explore_instance.explore(self.__selected_player)
            self.draw_explore_result(explore_result)


    #Class Selection Text (Visuals)
    def draw_character_naming(self):
        self.draw_text("Enter Character Name:", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text(self.__char_name, 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    def draw_class_selection(self):
        self.draw_text("Select Your Class:", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("1. Mage", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30)
        self.draw_text("2. Warrior", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("3. Archer", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30)
        self.draw_text("4. Rogue", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60)

    #In-Game Menu (Visuals)
    def draw_in_game(self):
        self.draw_text("In-Game Menu", 36, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("1. Inventory", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30)
        self.draw_text("2. Explore", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("3. Equipment", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30)
        self.draw_text("4. Quit", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60)

    #Explore Text (Visuals)
    def draw_explore_result(self, result):
        if result == "Fight":
            self.draw_text("Entered Combat!", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        elif result == "Resources":
            self.draw_text("Gained Resources!", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        elif result == "Event":
            self.draw_text("Event Triggered!", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        else:
            self.draw_text("Unknown Result", 24, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    def show_credits(self):
        print("Credits")
        print("Game developed by Your Name")
        print("Thanks for playing!")
        pygame.time.wait(2000)

    def show_inventory(self):
        print("\nInventory")
        print("1. View Item")
        print("2. Remove Item")
        inventory_choice = input("Please input your choice: ")

        if inventory_choice.lower() in ["1", "view item"]:
            print(f"{self.__char_name}'s Inventory")
            print(f"\n{self.__selected_player.getInventory().inventory_info()}")
            view_choice = input("Please input what item you want to view: ")  # input item name CAPS SENSITIVE
            item = self.__selected_player.getInventory().find_item(view_choice)  # checks if item is in player inventory
            if item is False:
                print("Item not found in inventory\n")
            else:
                print(f"\nName: {item.getName()}\n")
                if item.getItemType() == "equipment":  # CHANGE LATER WHEN MORE INVENTORY CATEGORIES ARE ADDED
                    print(f"Description: {item.getDescription()}\n"
                          f"Quality: {item.getQuality()}\n"
                          f"Rarity: {item.getRarity()}\n"
                          f"Level Requirements: {item.getLevelReq()}\n"
                          f"Item Type: {item.getItemType()}\n")