import pygame
import random
import sys
import time
import math

from game_run.settings import *
from character.character import Character

#Maps
from maps.woodlands import Map_Woodlands
from maps.mudflats import Map_mudflats
from maps.dungeon import Map_dungeon

#Character Selection & Class
from character.classes.character_class import CharacterSelection

class Game:
   
    #Attributes
        #Map & UI
    __screen_width = None
    __screen_height = None
    __map = None
    __viewport_x = None
    __viewport_y = None

        #Class Selection
    __character_selection = None

        #Quit Button
    __quit_button_image = None
    __quit_button_rect = None

        #Skill Button
    __skills_button_image = None
    __skills_button_rect = None

        #Enemies on map
    __enemy_group = None

        #Other
    __combat_finished = None
    
    def __init__(self):
        # Pygame config
        pygame.init()

            #UI & Display
        self.setScreen_width(SCREEN_WIDTH)
        self.setScreen_height(SCREEN_HEIGHT)
        self.setScreen(pygame.display.set_mode((self.__screen_width, self.__screen_height)))
        pygame.display.set_caption(TITLE)
        self.setClock(pygame.time.Clock())
        self.setRunning(True)
        self.setAll_sprites(pygame.sprite.Group())
        #Viewport Position
        self.setViewport_x(0)
        self.setViewport_y(0)

            #Map
        self.setMap(Map_Woodlands())

            #Player Initialised
        self.setPlayer_list([])
        spawn_position = (self.__screen_width // 2, self.__screen_height // 2)
        self.setSelected_player(self.create_character("Player", "Warrior", 30, spawn_position))
        self.__all_sprites.add(self.__selected_player)
            
            #Initialize Character Selection
        self.setCharacter_selection(CharacterSelection(self.__screen, self.__clock))
        
            #Quit Button
        self.setQuit_button_image(pygame.image.load('assets/quit_button.png'))
        self.setQuit_button_rect(self.__quit_button_image.get_rect(topleft=(10, 10)))

            #Skill Button
        self.setSkills_button_image(pygame.image.load('assets/skills_button.png'))
        self.setSkills_button_rect(self.__skills_button_image.get_rect(topleft=(10, 100)))
        
            #Enemies & Combat
        self.setEnemy_group(pygame.sprite.Group())  #Create a group for enemies
        self.setCombat_finished(False)
        self.generate_enemies(5)  # Generate 5 enemies for example

    #Getters

        #UI & Display
    def getScreen_width(self): return self.__screen_width
    def getScreen_height(self): return self.__screen_height
    def getScreen(self): return self.__screen
    def getClock(self): return self.__clock
    def getRunning(self): return self.__running
    def getAll_sprites(self): return self.__all_sprites
    #Viewport Position
    def getViewport_x(self): return self.__viewport_x
    def getViewport_y(self): return self.__viewport_y

        #Map
    def getMap(self): return self.__map

        #Player
    def getPlayer_list(self): return self.__player_list
    def getSelected_player(self): return self.__selected_player

        #Initialize Character Selection
    def getCharacter_selection(self): return self.__character_selection
    
        #Quit Button
    def getQuit_button_image(self): return self.__quit_button_image
    def getQuit_button_rect(self): return self.__quit_button_rect
    
        #Skill Button
    def getSkills_button_image(self): return self.__skills_button_image
    def getSkills_button_rect(self): return self.__skills_button_rect
        
        #Enemies & Combat
    def getEnemy_group(self): return self.__enemy_group
    def getCombat_finished(self): return self.__combat_finished

    # Setters

        #UI & Display
    def setScreen_width(self, screen_width): self.__screen_width = screen_width
    def setScreen_height(self, screen_height): self.__screen_height = screen_height
    def setScreen(self, screen): self.__screen = screen
    def setClock(self, clock): self.__clock = clock
    def setRunning(self, running): self.__running = running
    def setAll_sprites(self, all_sprites): self.__all_sprites = all_sprites
    #Viewport Position
    def setViewport_x(self, viewport_x): self.__viewport_x = viewport_x
    def setViewport_y(self, viewport_y): self.__viewport_y = viewport_y

        #Player
    def setPlayer_list(self, player_list): self.__player_list = player_list
    def setSelected_player(self, selected_player): self.__selected_player = selected_player

        #Map
    def setMap(self, map): self.__map = map
    
        #Character Selection
    def setCharacter_selection(self, character_selection): self.__character_selection = character_selection
    
        #Quit Button
    def setQuit_button_image(self, quit_button_image): self.__quit_button_image = quit_button_image
    def setQuit_button_rect(self, quit_button_rect): self.__quit_button_rect = quit_button_rect

        #Skill Button
    def setSkills_button_image(self, skills_button_image): self.__skills_button_image = skills_button_image
    def setSkills_button_rect(self, skills_button_rect): self.__skills_button_rect = skills_button_rect

        #Enemies & Combat
    def setEnemy_group(self, enemy_group): self.__enemy_group = enemy_group
    def setCombat_finished(self, combat_finished): self.__combat_finished = combat_finished

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
        selected_character = self.__character_selection.run()
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
                self.__enemy_group.draw(self.__screen)

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
                if self.__quit_button_rect.collidepoint(mouse_pos):
                    self.setRunning(False)  # Quit the game
                elif self.__skills_button_rect.collidepoint(mouse_pos):
                    self.__selected_player.skills(self.__screen, self.__clock)  # Open skill screen

    def update_viewport(self):
        player_rect = self.__selected_player.rect
        map_width, map_height = self.__map.get_map_size()
        
        # Update viewport position based on player position
        self.setViewport_x(max(0, min(player_rect.centerx - self.__screen_width // 2, map_width - self.__screen_width)))
        self.setViewport_y(max(0, min(player_rect.centery - self.__screen_height // 2, map_height - self.__screen_height)))

        # Clamp player position to viewport boundaries
        self.__selected_player.rect.centerx = max(self.__viewport_x + self.__selected_player.rect.width // 2, min(self.__selected_player.rect.centerx, self.__viewport_x + self.__screen_width - self.__selected_player.rect.width // 2))
        self.__selected_player.rect.centery = max(self.__viewport_y + self.__selected_player.rect.height // 2, min(self.__selected_player.rect.centery, self.__viewport_y + self.__screen_height - self.__selected_player.rect.height // 2))

    """"
    Combat Functions
    """

    def generate_enemies(self, num_enemies):
        map_width, map_height = self.__map.get_map_size()
        player_x, player_y = self.__selected_player.rect.center  # Get the player's position

        if self.__map.getNum_of_enemies() <= 0:
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
            enemy_data = random.choice(self.__map.getEnemies())
            
            # Create a sprite for the enemy
            enemy_image = pygame.image.load(enemy_data.getEnemy_image()).convert_alpha()
            enemy_sprite = pygame.sprite.Sprite()
            enemy_sprite.image = enemy_image
            enemy_sprite.rect = enemy_image.get_rect(topleft=(x, y))
            
            # Set custom attributes on the sprite to store enemy data
            enemy_sprite.enemy_data = enemy_data  # Add this line to store the enemy data
            
            # Add the sprite to the group
            self.__enemy_group.add(enemy_sprite)

    def spawn_boss(self):
        boss_data = self.__map.getBosses()  # Ensure this is a list of boss objects
        if boss_data:
            boss = random.choice(boss_data)  # Choose a random boss from the list
            boss_image = pygame.image.load(boss.getEnemy_image()).convert_alpha()  # Adjust as needed
            boss_sprite = pygame.sprite.Sprite()
            boss_sprite.image = boss_image
            boss_sprite.rect = boss_image.get_rect(center=(self.__screen_width // 2, self.__screen_height // 2))  # Center the boss on screen
            
            # Set custom attributes on the sprite to store boss data
            boss_sprite.boss_data = boss
            
            # Add the sprite to the group
            self.__enemy_group.add(boss_sprite)

    def check_combat(self):
        for enemy_sprite in self.__enemy_group:
            if pygame.sprite.collide_rect(self.__selected_player, enemy_sprite) and not self.__combat_finished:
                # Access the enemy or boss data from the sprite
                if hasattr(enemy_sprite, 'enemy_data'):
                    combat_data = enemy_sprite.enemy_data
                elif hasattr(enemy_sprite, 'boss_data'):
                    combat_data = enemy_sprite.boss_data
                
                # Call the combat method with the enemy or boss data
                self.__combat_finished = self.__selected_player.combat(self.getScreen(), combat_data)

                if self.__combat_finished:
                    if hasattr(enemy_sprite, 'boss_data'):
                        # Move to the next map after defeating the boss
                        self.transition_to_next_map()
                    else:
                        self.__enemy_group.empty()  # Resets Enemies on Map
                        self.__map.setNum_of_enemies(self.__map.getNum_of_enemies() - 1)  # Reduces number of enemies by 1
                        self.generate_enemies(self.__map.getNum_of_enemies())  # Regenerates the enemies
                    self.__combat_finished = False  # Reset combat state
                else:
                    if pygame.sprite.collide_rect(self.__selected_player, enemy_sprite) and self.__combat_finished == False:
                        #If player is defeated, they will be moved down 100 pixels to stop them going to combat again
                        self.__selected_player.rect.y += 100
                        self.__enemy_group.empty()
                        self.generate_enemies(0)
                        
    def transition_to_next_map(self):
        self.__enemy_group.empty()

        if self.__map.getArea_level() == 1:
            self.__map = Map_mudflats() # Switch to the Mudflats map
        elif self.__map.getArea_level() == 2:
            self.__map = Map_dungeon()  # Switch to the Dungeon map

        self.generate_enemies(self.__map.getNum_of_enemies())  # Generate enemies for the new map
        self.__selected_player.rect.center = (self.__screen_width // 2, self.__screen_height // 2)  # Reset player position
        self.setCombat_finished(False)  # Reset combat state

    """
    Draw (Generate Text & Visuals e.g. Maps) Functions
    """

    def draw_map(self):
        map_sprite = self.__map.getMap_sprite()
        map_width, map_height = self.__map.get_map_size()

        # Draw only the visible part of the map
        map_rect = pygame.Rect(self.__viewport_x, self.__viewport_y, self.__screen_width, self.__screen_height)
        self.__screen.blit(map_sprite, (-self.__viewport_x, -self.__viewport_y), map_rect)

    def draw_quit_button(self):
        self.__screen.blit(self.__quit_button_image, self.__quit_button_rect)

    def draw_skills_button(self):
        self.__screen.blit(self.__skills_button_image, self.__skills_button_rect)
