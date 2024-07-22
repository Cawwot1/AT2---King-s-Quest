import random
import time
import pygame
from enemy.create_enemy import Create_Enemy

class Explore:
    # Attributes
    __enemy_rateup = None
    __effect_duration = None
    __screen = None  # Pygame screen object

    # Constructor
    def __init__(self, screen):
        self.setEnemy_rateup(False)
        self.setEffect_duration(1)
        self.setScreen(screen)

    # Getters
    def getEnemy_rateup(self):
        return self.__enemy_rateup

    def getEffect_duration(self):
        return self.__effect_duration
    
    def getScreen(self):
        return self.__screen

    # Setters
    def setEnemy_rateup(self, enemy_rateup):
        self.__enemy_rateup = enemy_rateup

    def setEffect_duration(self, effect_duration):
        self.__effect_duration = effect_duration

    def setScreen(self, screen):
        self.__screen = screen

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.__screen.blit(text_surface, text_rect)

    def explore(self, selected_character):
        """
        Handles the exploration logic, including time delay and random event generation.
        """
    def explore(self, selected_character):
        random_delay = random.randint(5, 10)
        time.sleep(random_delay)
        self.draw_text(f"Explored for {random_delay} seconds", 24, (255, 255, 255), 400, 300)
        pygame.display.flip()
        
        explore_weights = [60, 35, 5]
        if self.__enemy_rateup:
            explore_weights = [80, 15, 5]
        
        explore_choice = random.choices(["Fight", "Resources", "Event"], weights=explore_weights)[0]
        
        if self.__effect_duration > 0 and explore_choice == "Event":
            explore_choice = random.choices(["Fight", "Resources"], weights=[50, 50])[0]

        if explore_choice == "Fight":
            self.draw_text("Entered Combat", 24, (255, 0, 0), 400, 330)
            enemy = random.choice(selected_character.getMap().getEnemies())
            self.draw_text(f"You are fighting {enemy.getEnemy_name()}", 24, (255, 0, 0), 400, 360)
            pygame.display.flip()
            selected_character.combat(self.getScreen(), enemy)
        elif explore_choice == "Resources":
            random_resource = random.choices(["Wood", "Stone", "Iron"], weights=[50, 45, 5])[0]
            if random_resource == "Wood":
                num_wood = random.randint(6, 10)
                selected_character.setWood(selected_character.getWood() + num_wood)
                self.draw_text(f"You have gained {num_wood} wood", 24, (0, 255, 0), 400, 330)
            elif random_resource == "Stone":
                num_stone = random.randint(4, 8)
                selected_character.setStone(selected_character.getStone() + num_stone)
                self.draw_text(f"You have gained {num_stone} stone", 24, (0, 255, 0), 400, 330)
            else:
                num_iron = random.randint(1, 3)
                selected_character.setIron(selected_character.getIron() + num_iron)
                self.draw_text(f"You have gained {num_iron} iron", 24, (0, 255, 0), 400, 330)
            pygame.display.flip()
        else:  # Event
            random_event = random.choice(["Bandit Ambush", "Abandoned Camp", "Wandering Merchant", "Darkening Skies"])
            if random_event == "Bandit Ambush":
                self.draw_text("You have been ambushed by bandits", 24, (255, 0, 0), 400, 330)
                self.draw_text("Entered Combat", 24, (255, 0, 0), 400, 360)
                enemy = Create_Enemy.Bandit()
                self.draw_text(f"You are fighting {enemy.getEnemy_name()}", 24, (255, 0, 0), 400, 390)
                pygame.display.flip()
            elif random_event == "Abandoned Camp":
                self.draw_text("You have wandered into an Abandoned Camp", 24, (255, 255, 0), 400, 330)
                pygame.display.flip()
            elif random_event == "Wandering Merchant":
                self.draw_text("You encounter a Wandering Merchant", 24, (255, 255, 0), 400, 330)
                # Add shop feature
                pygame.display.flip()
            elif random_event == "Darkening Skies":
                self.draw_text("A torrential downpour begins ... Enemy Appearance Rates have increased (2 turns)", 24, (255, 0, 0), 400, 330)
                self.setEnemy_rateup(True)
                self.setEffect_duration(2)
                pygame.display.flip()

        return explore_choice  # Return the result to be used for visual display
