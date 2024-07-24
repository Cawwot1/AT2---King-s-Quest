import pygame
import random
from character.character import Character
from enemy.enemy import Enemy

class Combat(Character):
    
    # Add Attributes
    __hardness = None
    __defence = None
    __messages = None

    #Image
    __victory_image = None
    __defeat_image = None
 
    # Constructor with screen parameter
    def __init__(self, screen, selected_character, enemy):
        
        # Store player and enemy sprites
        self.player_sprite = selected_character.getImage()
        self.enemy_sprite = pygame.image.load(enemy.getEnemy_image()).convert_alpha()

        self.setScreen(screen)
        
        self.setChar_stats(selected_character.combat_stats())
        self.setChar_health(selected_character.getHealth())
        self.setStamina_points(5)

        self.setEnemy(enemy)
        self.setEnemy_def(enemy.getEnemy_defence())
        self.setEnemy_attack(enemy.getEnemy_attack())
        self.setEnemy_speed(enemy.getEnemy_speed())
        self.setEnemy_hp(enemy.getEnemy_hp())
        
        self.setWeapon_gimick(None)
        
        if hasattr(selected_character.getEquipped_weapon(), 'getWeaponType'):
            self.setWeapon_type(selected_character.getEquipped_weapon().getWeaponType())
        else:
            self.setWeapon_type(None)
        
        self.setBase_damage(self.getChar_stats()[2])
        self.setPiercing(self.getChar_stats()[7])
        self.setElemental_dmg(self.getChar_stats()[5])
        self.setHardness(self.getChar_stats()[0])
        self.setDefence(selected_character.getDefence())

        self.setActing(None)
        self.setNon_acting(None)
        self.setTurn_order([])
        self.setMessages([])

        #Images
        self.setVictory_image(pygame.image.load('assets/victory.png'))
        self.setDefeat_image(pygame.image.load('assets/defeat.png'))

        #Modify their size ratio (if image is high quality ONLY)
        self.setVictory_image(pygame.transform.scale(self.__victory_image, (800, 700)))
        self.setDefeat_image(pygame.transform.scale(self.__defeat_image, (800, 700)))

        # Button setup
        self.buttons = {
            'attack1': pygame.Rect(screen.get_width() // 2 - 75, screen.get_height() - 120, 150, 40),
            'attack2': pygame.Rect(screen.get_width() // 2 - 75, screen.get_height() - 70, 150, 40),
        }

        self.button_colors = {
            'attack1': (0, 255, 0),
            'attack2': (0, 0, 255),
        }

        self.button_texts = {
            'attack1': "Attack Level 1",
            'attack2': "Attack Level 2",
        }

        self.confirm_buttons = {
            'continue': pygame.Rect(screen.get_width() // 2 - 80, screen.get_height() // 2, 150, 40),
            'exit': pygame.Rect(screen.get_width() // 2 - 80, screen.get_height() // 2 + 50, 150, 40)
        }

        self.confirm_button_colors = {
            'continue': (0, 255, 0),
            'exit': (255, 0, 0)
        }

        self.confirm_button_texts = {
            'continue': "Continue",
            'exit': "Exit"
        }

        # Message box setup
        self.message_box_position = (self.getScreen().get_width() - 310, self.getScreen().get_height() - 160)
        self.message_box_size = (300, 150)
        self.message_box_color = (50, 50, 50)
        self.message_box_border_color = (0, 0, 0)

        # Initialize messages as an empty list of tuples
        self.__messages = []

    # Getters
    def getChar_stats(self):
        return self.__char_stats

    def getChar_health(self):
        return self.__char_health

    def getStamina_points(self):
        return self.__stamina_points

    def getEnemy_def(self):
        return self.__enemy_def

    def getEnemy_attack(self):
        return self.__enemy_attack

    def getEnemy_speed(self):
        return self.__enemy_speed

    def getEnemy_hp(self):
        return self.__enemy_hp

    def getTurn_order(self):
        return self.__turn_order

    def getEnemy(self):
        return self.__enemy

    def getActing(self):
        return self.__acting

    def getNon_acting(self):
        return self.__non_acting

    def getWeapon_gimick(self):
        return self.__weapon_gimick

    def getWeapon_type(self):
        return self.__weapon_type

    def getBase_damage(self):
        return self.__base_damage

    def getPiercing(self):
        return self.__piercing

    def getElemental_dmg(self):
        return self.__elemental_dmg

    def getHardness(self):
        return self.__hardness
    
    def getDefence(self):
        return self.__defence
    
    def getScreen(self):
        return self.__screen
    
    def getMessages(self):
        return self.__messages

    def getVictory_image(self):
        return self.__victory_image
    def getDefeat_image(self):
        return self.__defeat_image


    #Setters

    def setChar_stats(self, char_stats):
        self.__char_stats = char_stats

    def setChar_health(self, char_health):
        self.__char_health = char_health

    def setStamina_points(self, point_num):
        self.__stamina_points = point_num
    
    def setEnemy_hp(self, hp):
        self.__enemy_hp = hp
    def setEnemy(self, enemy):
        self.__enemy = enemy
    def setEnemy_def(self, defence):
        self.__enemy_def = defence
    def setEnemy_attack(self, attack):
        self.__enemy_attack = attack
    def setEnemy_speed(self, speed):
        self.__enemy_speed = speed

    def setActing(self, acting):
        self.__acting = acting
    def setNon_acting(self, non_acting):
        self.__non_acting = non_acting
    def setTurn_order(self, turn_order):
        self.__turn_order = turn_order

    def setWeapon_gimick(self, weapon_gimick):
        self.__weapon_gimick = weapon_gimick

    def setWeapon_type(self, weapon_type):
        self.__weapon_type = weapon_type

    def setBase_damage(self, base_damage):
        self.__base_damage = base_damage

    def setPiercing(self, piercing):
        self.__piercing = piercing

    def setElemental_dmg(self, elemental_dmg):
        self.__elemental_dmg = elemental_dmg
    
    def setHardness(self, hardness):
        self.__hardness = hardness

    def setDefence(self, defence):
        self.__defence = defence

    def setScreen(self, screen):
        self.__screen = screen

    def setMessages(self, messages):
        self.__messages = messages

    def setVictory_image(self, victory_image):
        self.__victory_image = victory_image
    def setDefeat_image(self, defeat_image):
        self.__defeat_image = defeat_image

    # Behaviours
    def display_text(self, text, position=(10, 10), font_size=24, color=(255, 255, 255), alpha=255):
        font = pygame.font.SysFont(None, font_size)
        text_surface = font.render(text, True, color)
        text_surface.set_alpha(alpha)
        self.getScreen().blit(text_surface, position)

    def draw_buttons(self, buttons, button_colors, button_texts):
        for key, rect in buttons.items():
            pygame.draw.rect(self.getScreen(), button_colors[key], rect)
            font = pygame.font.SysFont(None, 24)
            text_surface = font.render(button_texts[key], True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=rect.center)
            self.getScreen().blit(text_surface, text_rect)
    
    def check_button_click(self, mouse_pos, buttons):
        for key, rect in buttons.items():
            if rect.collidepoint(mouse_pos):
                return key
        return None

    def add_message(self, text):
        if len(self.__messages) * 30 >= self.message_box_size[1]:  # Check if overflow
            self.__messages.pop(0)
        self.__messages.append((text, 255))  # Initialize alpha to 255
    
    def draw_message_box(self):
        pygame.draw.rect(self.getScreen(), self.message_box_color, (*self.message_box_position, *self.message_box_size))
        pygame.draw.rect(self.getScreen(), self.message_box_border_color, (*self.message_box_position, *self.message_box_size), 2)  # Border

    def draw_messages(self):
        y = self.message_box_position[1] + self.message_box_size[1] - 30  # Start at bottom of box
        for message, alpha in reversed(self.__messages):
            if alpha > 0:
                self.display_text(message, (self.message_box_position[0] + 10, y), alpha=alpha)
                y -= 30  # Move up for next message

    def draw_health_bar(self, current_health, max_health, position, size, base_color):
        # Calculate health ratio
        health_ratio = current_health / max_health

        # Change color from base color to white based on health ratio
        # Start with base_color (red or green) and gradually change to white
        color = tuple(int(base_color[i] + (255 - base_color[i]) * (1 - health_ratio)) for i in range(3))

        # Draw the background of the health bar
        pygame.draw.rect(self.getScreen(), (0, 0, 0), (*position, *size))  # Black outline
        pygame.draw.rect(self.getScreen(), (0, 0, 0), (*position, size[0], size[1]), 1)  # Thin black outline
        pygame.draw.rect(self.getScreen(), (255, 255, 255), (*position, size[0], size[1]), 2)  # Thin black border

        # Draw the health bar foreground with changing color
        health_bar_width = int(size[0] * health_ratio)
        pygame.draw.rect(self.getScreen(), color, (*position, health_bar_width, size[1]))  # Foreground

    def update_messages(self):
        for i, (text, alpha) in enumerate(self.__messages):
            if alpha > 0:
                self.__messages[i] = (text, alpha - 5)
            else:
                self.__messages[i] = (text, 0)  # Ensure alpha does not go negative

    def draw_enemy_name(self, name):
        font = pygame.font.SysFont(None, 30)
        text_surface = font.render(name, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.getScreen().get_width() // 2, 30))
        self.getScreen().blit(text_surface, text_rect)


    def combat(self, selected_character, enemy):
        if self.getEnemy_speed() >= 100:
            self.setTurn_order([enemy, selected_character])
        else:
            self.setTurn_order([selected_character, enemy])

        running = True
        player_turn = True
        while running and self.getChar_health() > 0 and self.getEnemy_hp() > 0:
            self.setActing(self.getTurn_order()[0])
            self.setNon_acting(self.getTurn_order()[1])
            damage = 0

            if player_turn:
                action = None
                while not action:
                    self.getScreen().fill((31, 36, 33))  # Background color
                    
                    # Draw player and enemy sprites
                    player_sprite_position = (self.getScreen().get_width() // 4 - self.player_sprite.get_width() // 2, 
                                            self.getScreen().get_height() // 2 - self.player_sprite.get_height() // 2)
                    enemy_sprite_position = (self.getScreen().get_width() * 3 // 4 - self.enemy_sprite.get_width() // 2, 
                                            self.getScreen().get_height() // 2 - self.enemy_sprite.get_height() // 2)
                    
                    self.getScreen().blit(self.player_sprite, player_sprite_position)
                    self.getScreen().blit(self.enemy_sprite, enemy_sprite_position)
                    
                    self.draw_enemy_name(self.getEnemy().getEnemy_name())  # Draw enemy name
                    self.draw_health_bar(self.getChar_health(), selected_character.getHealth(), (10, 10), (200, 20), (0, 255, 0))  # Player health bar
                    self.draw_health_bar(self.getEnemy_hp(), enemy.getEnemy_hp(), (self.getScreen().get_width() - 210, 10), (200, 20), (255, 0, 0))  # Enemy health bar
                    self.draw_message_box()
                    self.draw_messages()
                    self.draw_buttons(self.buttons, self.button_colors, self.button_texts)
                    pygame.display.flip()

                    attack_cooldown = 1000  # 1 second cooldown

                    # Track the time of the last attack
                    last_attack_time = 0

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            current_time = pygame.time.get_ticks()
                            mouse_pos = event.pos
                            action = self.check_button_click(mouse_pos, self.buttons)
                            if action and current_time - last_attack_time >= attack_cooldown:
                                self.add_message(f"Player selected: {self.button_texts[action]}")
                                if action == 'attack1':
                                    damage = random.randint(15, 20)
                                elif action == 'attack2':
                                    damage = random.randint(25, 30)
                                self.setEnemy_hp(max(0, self.getEnemy_hp() - damage))
                                player_turn = False  # Switch to enemy's turn
                                last_attack_time = current_time  # Update the last attack time
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            running = False  # Exit combat loop

            else:
                enemy_action = 'attack'
                if enemy_action == 'attack':
                    damage = random.randint(10, 20)
                    self.setChar_health(max(0, self.getChar_health() - damage))
                    self.add_message(f"Enemy attacks for {damage} damage!")
                player_turn = True  # Switch to player's turn

            # Update messages
            self.update_messages()
            self.getScreen().fill((31, 36, 33))  # Clear screen for the next frame

            # Draw player and enemy sprites again
            self.getScreen().blit(self.player_sprite, player_sprite_position)
            self.getScreen().blit(self.enemy_sprite, enemy_sprite_position)
            
            self.draw_enemy_name(self.getEnemy().getEnemy_name())
            self.draw_health_bar(self.getChar_health(), selected_character.getHealth(), (10, 10), (200, 20), (0, 255, 0))
            self.draw_health_bar(self.getEnemy_hp(), enemy.getEnemy_hp(), (self.getScreen().get_width() - 210, 10), (200, 20), (255, 0, 0))
            self.draw_message_box()
            self.draw_messages()
            self.draw_buttons(self.buttons, self.button_colors, self.button_texts)
            pygame.display.flip()

            pygame.time.delay(1000)  # Pause to simulate turn-based actions
            
            # Rotate turn order
            self.setTurn_order(self.getTurn_order()[::-1])

        # End of combat
        self.add_message("Combat Ended!")
        selected_character.gain_experience(enemy.getEnemy_exp(), self.__screen)
        self.add_message(f"Experience Gained: {enemy.getEnemy_exp()}")

        while True:
            self.getScreen().fill((31, 36, 33))  # Background color
            self.draw_enemy_name(self.getEnemy().getEnemy_name())  # Redraw enemy name

            # Determine which image to show based on the outcome
            if self.getChar_health() <= 0:
                result_image = self.__defeat_image
            else:
                result_image = self.__victory_image

            # Calculate positions for image and buttons
            image_position = (self.getScreen().get_width() // 2 - result_image.get_width() // 2, 
                            self.getScreen().get_height() // 2 - result_image.get_height() // 2 - 50)
            continue_button_position = (self.getScreen().get_width() // 2 - 80, 
                                        self.getScreen().get_height() // 2 + 50)

            # Blit the result image
            self.getScreen().blit(result_image, image_position)

            # Draw buttons and other elements
            self.draw_message_box()
            self.draw_messages()
            self.draw_buttons(self.confirm_buttons, self.confirm_button_colors, self.confirm_button_texts)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    action = self.check_button_click(mouse_pos, self.confirm_buttons)
                    if action == 'continue':
                        # Clear or hide combat sprites before exiting
                        if result_image == self.__victory_image:
                            return (True)
                        else:
                            return (False) # Exit combat and return to the previous state (e.g., the map)
                    elif action == 'exit':
                        pygame.quit()
                        quit()
