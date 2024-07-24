import random
import time
import pygame
from enemy.create_enemy import Create_Enemy

class Explore:
    # Attributes
    __enemy_rateup = None
    __effect_duration = None
    __screen = None  # Pygame screen object

    # Explore (timing method)
    __explore_start_time = None
    __explore_duration = None
    __exploring = None
    __explore_choice = None

    # Constructor
    def __init__(self, screen):
        self.setEnemy_rateup(False)
        self.setEffect_duration(1)
        self.setScreen(screen)
        self.setExplore_start_time(None)
        self.setExplore_duration(0)
        self.setExploring(False)
        self.__explore_choice = None

    # Getters
    def getEnemy_rateup(self):
        return self.__enemy_rateup
    def getEffect_duration(self):
        return self.__effect_duration
    def getScreen(self):
        return self.__screen
    def getExplore_start_time(self):
        return self.__explore_start_time
    def getExplore_duration(self):
        return self.__explore_duration
    def getExploring(self):
        return self.__exploring

    # Setters
    def setEnemy_rateup(self, enemy_rateup):
        self.__enemy_rateup = enemy_rateup
    def setEffect_duration(self, effect_duration):
        self.__effect_duration = effect_duration
    def setScreen(self, screen):
        self.__screen = screen
    def setExplore_start_time(self, explore_start_time):
        self.__explore_start_time = explore_start_time
    def setExplore_duration(self, explore_duration):
        self.__explore_duration = explore_duration
    def setExploring(self, exploring):
        self.__exploring = exploring

    # Behaviours

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.__screen.blit(text_surface, text_rect)

    def draw_explore_animation(self):
        elapsed_time = time.time() - self.__explore_start_time
        circle_x = 200 + int((elapsed_time % 1) * 400)
        circle_y = 300
        circle_color = (255, 255, 0)
        circle_radius = 30
        self.__screen.fill((0, 0, 0))  # Clear screen with black
        pygame.draw.circle(self.__screen, circle_color, (circle_x, circle_y), circle_radius)

    def update_explore(self, selected_character):
        if self.__exploring:
            elapsed_time = time.time() - self.__explore_start_time
            if elapsed_time >= self.__explore_duration:
                self.__exploring = False
                self.__screen.fill((0, 0, 0))  # Clear screen with black
                self.draw_text(f"Explored for {self.__explore_duration} seconds", 24, (255, 255, 255), 400, 300)
                pygame.display.flip()
                self.handle_explore_outcome(selected_character)
            else:
                self.__screen.fill((0, 0, 0))  # Clear screen with black
                self.draw_explore_animation()
                self.draw_text(f"Exploring... {int(elapsed_time)}s", 24, (255, 255, 255), 400, 300)
                pygame.display.flip()

    def handle_explore_outcome(self, selected_character):
        explore_choice = self.__explore_choice
        self.__screen.fill((0, 0, 0))  # Clear screen with black
        if explore_choice == "Fight":
            self.draw_text("Entered Combat", 24, (255, 0, 0), 400, 330)
            enemy = random.choice(selected_character.getMap().getEnemies())
            self.draw_text(f"You are fighting {enemy.getEnemy_name()}", 24, (255, 0, 0), 400, 360)
            pygame.display.flip()
            selected_character.combat(self.__screen, enemy)
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
                pygame.display.flip()
            elif random_event == "Darkening Skies":
                self.draw_text("A torrential downpour begins ... Enemy Appearance Rates have increased (2 turns)", 24, (255, 0, 0), 400, 330)
                self.setEnemy_rateup(True)
                self.setEffect_duration(2)
                pygame.display.flip()

    def explore(self, selected_character):
        self.__explore_duration = random.randint(5, 10)
        self.__explore_start_time = time.time()
        self.__exploring = True

        explore_weights = [60, 35, 5]
        if self.__enemy_rateup:
            explore_weights = [80, 15, 5]

        self.__explore_choice = random.choices(["Fight", "Resources", "Event"], weights=explore_weights)[0]

        if self.__effect_duration > 0 and self.__explore_choice == "Event":
            self.__explore_choice = random.choices(["Fight", "Resources"], weights=[50, 50])[0]

        return self.__explore_choice