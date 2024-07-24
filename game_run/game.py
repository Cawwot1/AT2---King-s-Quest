import pygame
import random
import sys
import time
import math

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

#Maps
from maps.woodlands import Map_Woodlands
from maps.mudflats import Map_mudflats
from maps.dungeon import Map_dungeon

from character.actions.explore import Explore

#Combat
from enemy.create_enemy import Create_Enemy

#Skills
from character.attributes.skill import Skill

#Character Selection & Class
from character.classes.character_class import CharacterSelection

class Game:
    def __init__(self):
        self.__combat_finished = False

        # Pygame config
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800

        self.setScreen(pygame.display.set_mode((self.screen_width, self.screen_height)))
        pygame.display.set_caption(TITLE)
        self.setClock(pygame.time.Clock())
        self.setRunning(True)
        self.setAll_sprites(pygame.sprite.Group())

        self.setExplore_instance(Explore(self.getScreen()))

        #Player Initialised
        self.setPlayer_list([])
        spawn_position = (self.screen_width // 2, self.screen_height // 2)
        self.setSelected_player(self.create_character("Player", "Warrior", 30, spawn_position))

        self.map = Map_Woodlands()

        self.__all_sprites.add(self.__selected_player)

        self.last_explore_check = pygame.time.get_ticks()
        self.explore_interval = 1000  # Check for exploration every 1 second
        self.move_distance = 0

        # Initialize Character Selection
        self.character_selection = CharacterSelection(self.__screen, self.__clock)

        #Quit Button
        self.quit_button_image = pygame.image.load('assets/quit_button.png')
        self.quit_button_rect = self.quit_button_image.get_rect(topleft=(10, 10))

        #Skill Button
        self.skills_button_image = pygame.image.load('assets/skills_button.png')
        self.skills_button_rect = self.skills_button_image.get_rect(topleft=(10, 100)) #84 pixels height + 20 pixels spacing
        #Skill
        self.__skill_screen = Skill.show_skill_point_screen

        #Enemies
        self.enemy_group = pygame.sprite.Group()  # Create a group for enemies
        self.generate_enemies(5)  # Generate 5 enemies for example

        # Define viewport position
        self.viewport_x = 0
        self.viewport_y = 0

    # Getters
    def getScreen(self):
        return self.__screen

    def getClock(self):
        return self.__clock

    def getRunning(self):
        return self.__running

    def getAll_sprites(self):
        return self.__all_sprites

    def getExplore_instance(self):
        return self.__explore_instance

    def getPlayer_list(self):
        return self.__player_list

    def getSelected_player(self):
        return self.__selected_player

    # Setters
    def setScreen(self, screen):
        self.__screen = screen

    def setClock(self, clock):
        self.__clock = clock

    def setRunning(self, running):
        self.__running = running

    def setAll_sprites(self, all_sprites):
        self.__all_sprites = all_sprites

    def setExplore_instance(self, explore_instance):
        self.__explore_instance = explore_instance

    def setPlayer_list(self, player_list):
        self.__player_list = player_list

    def setSelected_player(self, selected_player):
        self.__selected_player = selected_player

    # Behaviours
    def create_character(self, name, character_class, inventory_cap, pos):
        if character_class == "Warrior":
            return Character(name, character_class, inventory_cap, pos, self.__all_sprites)
        elif character_class == "Mage":
            return Character(name, character_class, inventory_cap, pos, self.__all_sprites)
        elif character_class == "Archer":
            return Character(name, character_class, inventory_cap, pos, self.__all_sprites)
        elif character_class == "Rogue":
            return Character(name, character_class, inventory_cap, pos, self.__all_sprites)

    def run(self):
        selected_character = self.character_selection.run()
        self.__selected_player.setImage(pygame.image.load(f'assets/classes/{selected_character.lower()}.png').convert_alpha())
    
        if selected_character is None:
            self.__running = False  # Exit game if no character selected
        else:

            while self.__running:
                self.events()  # Handle events

                # Update player position
                self.__selected_player.update()
                self.check_combat()
                self.update_viewport()

                # Clear the screen
                self.__screen.fill((0, 0, 0))

                # Draw map and entities
                self.draw_map()
                self.__all_sprites.draw(self.__screen)
                self.enemy_group.draw(self.__screen)

                #Check if no more enemies are no (so boss can spawn)
        

                # Draw buttons
                self.draw_quit_button()
                self.draw_skills_button()

                # Refresh the screen
                pygame.display.flip()

                # Cap the frame rate
                self.__clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.setRunning(False)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.setRunning(False)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.quit_button_rect.collidepoint(mouse_pos):
                    self.setRunning(False)  # Quit the game
                elif self.skills_button_rect.collidepoint(mouse_pos):
                    self.__selected_player.skills(self.__screen, self.__clock)  # Open skill screen

        if self.move_distance >= 100:
            self.move_distance = 0
            if random.random() < 0.01:
                explore_result = self.__explore_instance.explore(self.__selected_player)
                self.draw_explore_result(explore_result)

    def update_viewport(self):
        player_rect = self.__selected_player.rect
        map_width, map_height = self.map.get_map_size()
        
        # Update viewport position based on player position
        self.viewport_x = max(0, min(player_rect.centerx - self.screen_width // 2, map_width - self.screen_width))
        self.viewport_y = max(0, min(player_rect.centery - self.screen_height // 2, map_height - self.screen_height))

        # Clamp player position to viewport boundaries
        self.__selected_player.rect.centerx = max(self.viewport_x + self.__selected_player.rect.width // 2, min(self.__selected_player.rect.centerx, self.viewport_x + self.screen_width - self.__selected_player.rect.width // 2))
        self.__selected_player.rect.centery = max(self.viewport_y + self.__selected_player.rect.height // 2, min(self.__selected_player.rect.centery, self.viewport_y + self.screen_height - self.__selected_player.rect.height // 2))

    """"
    Combat Functions
    """

    def generate_enemies(self, num_enemies):
        map_width, map_height = self.map.get_map_size()
        player_x, player_y = self.__selected_player.rect.center  # Get the player's position

        if self.map.getNum_of_enemies() <= 0:
                    self.spawn_boss()

        for _ in range(num_enemies):
            while True:
                x = random.randint(0, map_width - 50)
                y = random.randint(0, map_height - 50)
                
                # Calculate distance from player
                distance = math.sqrt((x - player_x) ** 2 + (y - player_y) ** 2)
                
                if distance >= 100:  # Check if the distance is greater than 100 pixels
                    break # -> So that enemies cannot spawn on top of player

            # Choose a random enemy type from the map's enemies
            enemy_data = random.choice(self.map.getEnemies())
            
            # Create a sprite for the enemy
            enemy_image = pygame.image.load(enemy_data.getEnemy_image()).convert_alpha()
            enemy_sprite = pygame.sprite.Sprite()
            enemy_sprite.image = enemy_image
            enemy_sprite.rect = enemy_image.get_rect(topleft=(x, y))
            
            # Set custom attributes on the sprite to store enemy data
            enemy_sprite.enemy_data = enemy_data  # Add this line to store the enemy data
            
            # Add the sprite to the group
            self.enemy_group.add(enemy_sprite)

    def spawn_boss(self):
        boss_data = self.map.getBosses()  # Ensure this is a list of boss objects
        if boss_data:
            boss = random.choice(boss_data)  # Choose a random boss from the list
            boss_image = pygame.image.load(boss.getEnemy_image()).convert_alpha()  # Adjust as needed
            boss_sprite = pygame.sprite.Sprite()
            boss_sprite.image = boss_image
            boss_sprite.rect = boss_image.get_rect(center=(self.screen_width // 2, self.screen_height // 2))  # Center the boss on screen
            
            # Set custom attributes on the sprite to store boss data
            boss_sprite.boss_data = boss
            
            # Add the sprite to the group
            self.enemy_group.add(boss_sprite)

    def check_combat(self):
        for enemy_sprite in self.enemy_group:
            if pygame.sprite.collide_rect(self.__selected_player, enemy_sprite) and not self.__combat_finished:
                # Access the enemy or boss data from the sprite
                if hasattr(enemy_sprite, 'enemy_data'):
                    combat_data = enemy_sprite.enemy_data
                elif hasattr(enemy_sprite, 'boss_data'):
                    combat_data = enemy_sprite.boss_data
                
                # Call the combat method with the enemy or boss data
                self.__combat_finished = self.__selected_player.combat(self.getScreen(), combat_data)

                if self.__combat_finished:
                    print("efewoifIFEOHWFHEWFHWOE")
                    if hasattr(enemy_sprite, 'boss_data'):
                        # Move to the next map after defeating the boss
                        self.transition_to_next_map()
                    else:
                        print("iefiefoowuhhou")
                        self.enemy_group.empty()  # Resets Enemies on Map
                        self.map.setNum_of_enemies(self.map.getNum_of_enemies() - 1)  # Reduces number of enemies by 1
                        self.generate_enemies(self.map.getNum_of_enemies())  # Regenerates the enemies
                    self.__combat_finished = False  # Reset combat state
                else:
                    if pygame.sprite.collide_rect(self.__selected_player, enemy_sprite) and self.__combat_finished == False:
                        #If player is defeated, they will be moved down 100 pixels to stop them going to combat again
                        self.__selected_player.rect.y += 100
                        self.enemy_group.empty()
                        self.generate_enemies(0)
                        


    def transition_to_next_map(self):
        print("next map")
        self.enemy_group.empty()

        if self.map.getArea_level() == 1:
            print("mudflats")
            self.map = Map_mudflats() # Switch to the Mudflats map
        elif self.map.getArea_level() == 2:
            self.map = Map_dungeon()  # Switch to the Dungeon map

        self.generate_enemies(self.map.getNum_of_enemies())  # Generate enemies for the new map
        self.__selected_player.rect.center = (self.screen_width // 2, self.screen_height // 2)  # Reset player position
        self.__combat_finished = False  # Reset combat state


    """
    Draw (Generate Text & Visuals e.g. Maps) Functions
    """

    def draw_map(self):
        map_sprite = self.map.getMap_sprite()
        map_width, map_height = self.map.get_map_size()

        # Draw only the visible part of the map
        map_rect = pygame.Rect(self.viewport_x, self.viewport_y, self.screen_width, self.screen_height)
        self.__screen.blit(map_sprite, (-self.viewport_x, -self.viewport_y), map_rect)

    def draw_quit_button(self):
        self.__screen.blit(self.quit_button_image, self.quit_button_rect)

    def draw_skills_button(self):
        self.__screen.blit(self.skills_button_image, self.skills_button_rect)

    def draw_explore_result(self, result):
        font = pygame.font.Font(None, 36)
        text = font.render(result, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.__screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Show the result for 2 seconds
