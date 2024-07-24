import pygame

class CharacterSelection:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.screen_width = 1200
        self.screen_height = 800

        # Character buttons
        self.character_buttons = {
            'Warrior': pygame.image.load('assets/classes/warrior.png').convert_alpha(),
            'Mage': pygame.image.load('assets/classes/mage.png').convert_alpha(),
            'Archer': pygame.image.load('assets/classes/archer.png').convert_alpha(),
            'Rogue': pygame.image.load('assets/classes/rogue.png').convert_alpha()
        }

        # Positions for the character buttons
        self.character_positions = {
            'Warrior': (self.screen_width // 4 - 50, self.screen_height // 3 - 50),
            'Mage': (self.screen_width // 4 * 3 - 50, self.screen_height // 3 - 50),
            'Archer': (self.screen_width // 4 - 50, self.screen_height // 3 * 2 - 50),
            'Rogue': (self.screen_width // 4 * 3 - 50, self.screen_height // 3 * 2 - 50)
        }

        # Positions for the description boxes
        self.description_boxes = {
            'Warrior': (self.screen_width // 4 - 50, self.screen_height // 3 + 50),
            'Mage': (self.screen_width // 4 * 3 - 50, self.screen_height // 3 + 50),
            'Archer': (self.screen_width // 4 - 50, self.screen_height // 3 * 2 + 50),
            'Rogue': (self.screen_width // 4 * 3 - 50, self.screen_height // 3 * 2 + 50)
        }

        # Descriptions and special abilities
        self.character_info = {
            'Warrior': ("A brave warrior with high defense.", "Special Ability: Power Strike"),
            'Mage': ("A master of magic with powerful spells.", "Special Ability: Fireball"),
            'Archer': ("An agile archer with deadly accuracy.", "Special Ability: Shoot a volley of arrows that hits multiple enemies."),
            'Rogue': ("A stealthy rogue with quick strikes.", "Special Ability: Backstab")
        }

        self.selected_character = None

    def draw_selection_screen(self):
        self.screen.fill((0, 0, 0))  # Fill screen with black

        for char, pos in self.character_positions.items():
            self.screen.blit(self.character_buttons[char], pos)

        for char, pos in self.description_boxes.items():
            pygame.draw.rect(self.screen, (50, 50, 50), pygame.Rect(pos, (200, 100)))  # Description box background
            self.draw_text(char, 24, (255, 255, 255), pos[0] + 10, pos[1] + 10)  # Character name
            description, ability = self.character_info[char]
            self.draw_text(description, 18, (255, 255, 255), pos[0] + 10, pos[1] + 30)  # Description
            self.draw_text(ability, 18, (255, 255, 255), pos[0] + 10, pos[1] + 60)  # Special Ability
        
        pygame.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(pygame.font.match_font('arial'), size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # To signal the game should quit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for char, pos in self.character_positions.items():
                    rect = pygame.Rect(pos, (100, 100))  # Assuming each button is 100x100 pixels
                    if rect.collidepoint(x, y):
                        self.selected_character = char
                        return char  # Return the selected character

        return None  # No character selected

    def run(self):
        running = True
        while running:
            self.draw_selection_screen()
            selected = self.handle_events()

            if selected:
                return selected  # Return the selected character to be used in the game
