import pygame
from game_run.settings import *

class CharacterSelection:

    #Attributes
    __screen = None
    __clock = None
    __screen_width = None
    __screen_height = None
    __selected_class = None

    #Class Selection UI
    __character_buttons = None
    __character_positions = None
    __description_boxes = None
    __character_info = None

    def __init__(self, screen, clock):
        self.setScreen(screen)
        self.setClock(clock)
        self.setScreen_width(SCREEN_WIDTH)
        self.setScreen_height(SCREEN_HEIGHT)
        
        self.setSelected_class(None)

        #Class Selection UI
        self.setCharacter_buttons({ #Images of character classes (which will be turned into buttons)
            'Warrior': pygame.image.load('assets/classes/warrior.png').convert_alpha(),
            'Mage': pygame.image.load('assets/classes/mage.png').convert_alpha(),
            'Archer': pygame.image.load('assets/classes/archer.png').convert_alpha(),
            'Rogue': pygame.image.load('assets/classes/rogue.png').convert_alpha()})

        self.setCharacter_positions({ #Positions for the character buttons
            'Warrior': (self.__screen_width // 4 - 160, self.__screen_height // 3 - 120),
            'Mage': (self.__screen_width // 4 * 3 - 160, self.__screen_height // 3 - 120),
            'Archer': (self.__screen_width // 4 - 160, self.__screen_height // 3 * 2 - 120),
            'Rogue': (self.__screen_width // 4 * 3 - 160, self.__screen_height // 3 * 2 - 120)})

        self.setDescription_boxes({ #Positions for the description boxes
            'Warrior': (self.__screen_width // 4 - 160, self.__screen_height // 3 - 40),
            'Mage': (self.__screen_width // 4 * 3 - 160, self.__screen_height // 3 - 40),
            'Archer': (self.__screen_width // 4 - 160, self.__screen_height // 3 * 2 - 40),
            'Rogue': (self.__screen_width // 4 * 3 - 160, self.__screen_height // 3 * 2 - 40)})
        
        self.setCharacter_info({ #Descriptions and special abilities
            'Warrior': ("A brave warrior with high defense.", "Special Ability: Power Strike"),
            'Mage': ("A master of magic with powerful spells.", "Special Ability: Fireball"),
            'Archer': ("An agile archer with deadly accuracy.", "Special Ability: Critical Strikes"),
            'Rogue': ("A stealthy rogue with quick strikes.", "Special Ability: Backstab")})

    # Getters
    def getScreen(self): return self.__screen
    def getClock(self): return self.__clock
    def getScreen_width(self): return self.__screen_width
    def getScreen_height(self): return self.__screen_height
    def getSelected_class(self): return self.__selected_class
    def getCharacter_buttons(self): return self.__character_buttons
    def getCharacter_positions(self): return self.__character_positions
    def getDescription_boxes(self): return self.__description_boxes
    def getCharacter_info(self): return self.__character_info

    # Setters
    def setScreen(self, screen): self.__screen = screen
    def setClock(self, clock): self.__clock = clock
    def setScreen_width(self, screen_width): self.__screen_width = screen_width
    def setScreen_height(self, screen_height): self.__screen_height = screen_height
    def setSelected_class(self, selected_class): self.__selected_class = selected_class
    def setCharacter_buttons(self, character_buttons): self.__character_buttons = character_buttons
    def setCharacter_positions(self, character_positions): self.__character_positions = character_positions
    def setDescription_boxes(self, description_boxes): self.__description_boxes = description_boxes
    def setCharacter_info(self, character_info): self.__character_info = character_info

    # Behaviours
    def draw_selection_screen(self):
        self.__screen.fill((0, 0, 0))  # Fill screen with black

        for char, pos in self.__character_positions.items():
            self.__screen.blit(self.__character_buttons[char], pos)  # Draw character buttons

        for char, pos in self.__description_boxes.items():
            pygame.draw.rect(self.__screen, (50, 50, 50), pygame.Rect(pos, (330, 150)))  # Draw description box background
            self.draw_text(char, 24, (255, 255, 255), pos[0] + 10, pos[1] + 10)  # Draw character name
            description, ability = self.__character_info[char]
            self.draw_text(description, 18, (255, 255, 255), pos[0] + 10, pos[1] + 50)  # Draw character description
            self.draw_text(ability, 18, (255, 255, 255), pos[0] + 10, pos[1] + 80)  # Draw character special ability
        
        pygame.display.flip()  # Update the display

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(pygame.font.match_font('arial'), size)  # Create font object
        text_surface = font.render(text, True, color)  # Render the text
        text_rect = text_surface.get_rect()  # Get the text's rectangle
        text_rect.topleft = (x, y)  # Set the position
        self.__screen.blit(text_surface, text_rect)  # Draw the text on the screen

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Return None to signal the game should quit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # Get the mouse click position
                for char, pos in self.__character_positions.items():
                    rect = pygame.Rect(pos, (100, 100))  # Define button area (100x100 pixels)
                    if rect.collidepoint(x, y):  # Check if the click is within the button area
                        self.__selected_class = char  # Set selected character class
                        return char  # Return the selected character

        return None  # Return None if no character was selected

    def run(self):
        running = True
        while running:
            self.draw_selection_screen()  # Draw the character selection screen
            selected = self.handle_events()  # Handle user events

            if selected:
                return selected  # Return the selected character to be used in the game

