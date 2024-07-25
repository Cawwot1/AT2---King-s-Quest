import pygame
import random
from character.character import Character
from enemy.enemy import Enemy

class Combat(Character):
    
    # Attributes

        #Player & Enemy Sprites
    __player_sprite = None
    __enemy_sprite = None

        #Screen
    __screen = None

        #Player/Character
    __char_stats = None
    __char_health = None
    __stamina_points = None
    __base_damage = None
    __piercing = None
    __elemental_dmg = None
    __hardness = None
    __defence = None

        #Enemy
    __enemy = None
    __enemy_def = None
    __enemy_attack = None
    __enemy_speed = None
    __enemy_hp = None

        #Weapon
    __weapon_gimick = None
    __weapon_type = None

        #Turn-based Combat
    __acting = None
    __non_acting = None
    __turn_order = None

        #Images
    __victory_image = None
    __defeat_image = None

        #Button-Setup
    __buttons = None
    __button_colours = None
    __button_texts = None
    __confirm_buttons = None
    __confirm_button_colours = None
    __confirm_button_texts = None

        #Comabt Message-Box
    __message_box_position = None
    __message_box_size = None
    __message_box_border_colour = None
    __messages = None

    # Constructor (paramerters: screen/window, character/player, enemy)
    def __init__(self, screen, selected_character, enemy):
        
            # Store player and enemy sprites
        self.setPlayer_sprite(selected_character.getImage())
        self.setEnemy_sprite(pygame.image.load(enemy.getEnemy_image()).convert_alpha())

            # Screen
        self.setScreen(screen)
        
            #Player/Character
        self.setChar_stats(selected_character.combat_stats())
        self.setChar_health(selected_character.getHealth()) #Set the initial health of the character
        self.setStamina_points(5) #Set the initial stamina points
        #Set stats based from character_stats
        self.setBase_damage(self.getChar_stats()[2])
        self.setPiercing(self.getChar_stats()[7])
        self.setElemental_dmg(self.getChar_stats()[5])
        self.setHardness(self.getChar_stats()[0])
        self.setDefence(selected_character.getDefence())

            #Enemy
        self.setEnemy(enemy)
        # Set enemy's stats retrived from enemy
        self.setEnemy_def(enemy.getEnemy_defence())
        self.setEnemy_attack(enemy.getEnemy_attack())
        self.setEnemy_speed(enemy.getEnemy_speed())
        self.setEnemy_hp(enemy.getEnemy_hp())
        
            #Weapon - UNUSED
        self.setWeapon_gimick(None) #Weapon Special ability
        if hasattr(selected_character.getEquipped_weapon(), 'getWeaponType'): #Checks if a weapon is equipped
            self.setWeapon_type(selected_character.getEquipped_weapon().getWeaponType())
        else:
            self.setWeapon_type(None)

            #Turn-based Combat
        self.setActing(None) #Combatant turns
        self.setNon_acting(None)
        self.setTurn_order([]) #Combatant turn order (first act based on speed)
        self.setMessages([])

            #Images - Loads & sets images
        self.setVictory_image(pygame.image.load('assets/victory.png'))
        self.setDefeat_image(pygame.image.load('assets/defeat.png'))
        # Modify image size for high-quality images (1200x800)
        self.setVictory_image(pygame.transform.scale(self.__victory_image, (1200, 900)))
        self.setDefeat_image(pygame.transform.scale(self.__defeat_image, (1200, 900)))

            #Button-setup
        #Set up attack buttons with positions and sizes
        self.setButtons({
            'attack1': pygame.Rect(screen.get_width() // 2 - 75, screen.get_height() - 120, 150, 40),
            'attack2': pygame.Rect(screen.get_width() // 2 - 75, screen.get_height() - 70, 150, 40),
        })
        
        #Set colors for the attack buttons
        self.setButton_colours({
            'attack1': (0, 255, 0),  # Green for Attack Level 1
            'attack2': (0, 0, 255),  # Blue for Attack Level 2
        })
        #Set text labels for the attack buttons
        self.setButton_texts({
            'attack1': "Attack Level 1",
            'attack2': "Attack Level 2",
        })
        
        #Set up confirmation buttons with positions and sizes
        self.setConfirm_buttons({
            'continue': pygame.Rect(screen.get_width() // 2 - 80, screen.get_height() // 2, 150, 40),
            'exit': pygame.Rect(screen.get_width() // 2 - 80, screen.get_height() // 2 + 50, 150, 40),
        })
        
        #Set colors for the confirmation buttons
        self.setConfirm_button_colours({
            'continue': (0, 255, 0),  # Green for Continue
            'exit': (255, 0, 0),     # Red for Exit / Quit game
        })
        
        #Set text labels for the confirmation buttons
        self.setConfirm_button_texts({
            'continue': "Continue",
            'exit': "Exit",
        })

            #Combat Message box
        #Set the position and size of the message box
        self.setMessage_box_position((self.getScreen().get_width() - 310, self.getScreen().get_height() - 160))
        self.setMessage_box_size((300, 150))
        #Set the color and border color of the message box
        self.setMessage_box_colour((50, 50, 50))
        self.setMessage_box_border_colour((0, 0, 0))
        #Initialize message list
        self.setMessages([])


    # Getters

        #Player & Enemy Sprites
    def getPlayer_sprite(self): return self.__player_sprite
    def getEnemy_sprite(self): return self.__enemy_sprite

        #Screen
    def getScreen(self): return self.__screen

        #Player/Character
    def getChar_stats(self): return self.__char_stats
    def getChar_health(self): return self.__char_health
    def getStamina_points(self): return self.__stamina_points
    def getBase_damage(self): return self.__base_damage
    def getPiercing(self): return self.__piercing
    def getElemental_dmg(self): return self.__elemental_dmg
    def getHardness(self): return self.__hardness
    def getDefence(self): return self.__defence

        #Enemy
    def getEnemy(self): return self.__enemy
    def getEnemy_def(self): return self.__enemy_def
    def getEnemy_attack(self): return self.__enemy_attack
    def getEnemy_speed(self): return self.__enemy_speed
    def getEnemy_hp(self): return self.__enemy_hp
    
        #Weapon - UNUSED
    def getWeapon_gimick(self): return self.__weapon_gimick
    def getWeapon_type(self): return self.__weapon_type

        #Turn-based Combat

    def getTurn_order(self): return self.__turn_order
    def getActing(self): return self.__acting
    def getNon_acting(self): return self.__non_acting
    
        #Images
    def getVictory_image(self): return self.__victory_image
    def getDefeat_image(self): return self.__defeat_image

       #Button-Setup
    def getButtons(self): return self.__buttons
    def getButton_colours(self): return self.__button_colours
    def getButton_texts(self): return self.__button_texts
    def getConfirm_buttons(self): return self.__confirm_buttons
    def getConfirm_button_colours(self): return self.__confirm_button_colours
    def getConfirm_button_texts(self): return self.__confirm_button_texts

        #Combat Message-Box
    def getMessage_box_position(self): return self.__message_box_position
    def getMessage_box_size(self): return self.__message_box_size
    def getMessage_box_colour(self): return self.__message_box_colour
    def getMessage_box_border_colour(self): return self.__message_box_border_colour

    #Setters

        #Player & Enemy Sprites
    def setPlayer_sprite(self, player_sprite): self.__player_sprite = player_sprite
    def setEnemy_sprite(self, enemy_sprite): self.__enemy_sprite = enemy_sprite

        #Screen
    def setScreen(self, screen): self.__screen = screen

        #Player/Character
    def setChar_stats(self, char_stats): self.__char_stats = char_stats
    def setChar_health(self, char_health): self.__char_health = char_health
    def setStamina_points(self, point_num): self.__stamina_points = point_num
    def setBase_damage(self, base_damage): self.__base_damage = base_damage
    def setPiercing(self, piercing): self.__piercing = piercing
    def setElemental_dmg(self, elemental_dmg): self.__elemental_dmg = elemental_dmg
    def setHardness(self, hardness): self.__hardness = hardness
    def setDefence(self, defence): self.__defence = defence

        #Enemy
    def setEnemy_hp(self, hp): self.__enemy_hp = hp
    def setEnemy(self, enemy): self.__enemy = enemy
    def setEnemy_def(self, defence): self.__enemy_def = defence
    def setEnemy_attack(self, attack): self.__enemy_attack = attack
    def setEnemy_speed(self, speed): self.__enemy_speed = speed
    
        #Weapon
    def setWeapon_gimick(self, weapon_gimick): self.__weapon_gimick = weapon_gimick
    def setWeapon_type(self, weapon_type): self.__weapon_type = weapon_type

        #Turn-based Combat
    def setActing(self, acting): self.__acting = acting
    def setNon_acting(self, non_acting): self.__non_acting = non_acting
    def setTurn_order(self, turn_order): self.__turn_order = turn_order

        #Images
    def setVictory_image(self, victory_image): self.__victory_image = victory_image
    def setDefeat_image(self, defeat_image): self.__defeat_image = defeat_image

        #Combat Buttons
    def setButtons(self, buttons): self.__buttons = buttons
    def setButton_colours(self, button_colours): self.__button_colours = button_colours
    def setButton_texts(self, button_texts): self.__button_texts = button_texts
    def setConfirm_buttons(self, confirm_buttons): self.__confirm_buttons = confirm_buttons
    def setConfirm_button_colours(self, confirm_button_colours): self.__confirm_button_colours = confirm_button_colours
    def setConfirm_button_texts(self, confirm_button_texts): self.__confirm_button_texts = confirm_button_texts

        #Combat Messages
    def setMessage_box_position(self, message_box_position): self.__message_box_position = message_box_position
    def setMessage_box_size(self, message_box_size): self.__message_box_size = message_box_size
    def setMessage_box_colour(self, message_box_colour): self.__message_box_colour = message_box_colour
    def setMessage_box_border_colour(self, message_box_border_colour): self.__message_box_border_colour = message_box_border_colour
    def setMessages(self, messages): self.__messages = messages
    
    # Behaviours

    def display_text(self, text, position=(10, 10), font_size=24, colour=(255, 255, 255), alpha=255):
        font = pygame.font.SysFont(None, font_size)  # Create a font object with specified size
        text_surface = font.render(text, True, colour)  # Render the text into a surface
        text_surface.set_alpha(alpha)  # Set the transparency of the text
        self.__screen.blit(text_surface, position)  # Draw the text on the screen at the specified position

    def draw_buttons(self, buttons, button_colours, button_texts):
        for key, rect in buttons.items():
            pygame.draw.rect(self.__screen, button_colours[key], rect)  # Draw each button with its color
            font = pygame.font.SysFont(None, 24)  # Create a font object for button text
            text_surface = font.render(button_texts[key], True, (0, 0, 0))  # Render button text
            text_rect = text_surface.get_rect(center=rect.center)  # Center the text within the button
            self.__screen.blit(text_surface, text_rect)  # Draw the text on the button

    def check_button_click(self, mouse_pos, buttons):
        for key, rect in buttons.items():
            if rect.collidepoint(mouse_pos):  # Check if mouse position is over the button
                return key  # Return the key of the clicked button
        return None  # Return None if no button was clicked



    def add_message(self, text):
        if len(self.__messages) * 30 >= self.__message_box_size[1]:  # Check if the number of messages exceeds the box height
            self.__messages.pop(0)  # Remove the oldest message if overflow
        self.__messages.append((text, 255))  # Append the new message with full opacity

    def draw_message_box(self):
        pygame.draw.rect(self.__screen, self.__message_box_colour, (*self.__message_box_position, *self.__message_box_size))  # Draw the background of the message box
        pygame.draw.rect(self.__screen, self.__message_box_border_colour, (*self.__message_box_position, *self.__message_box_size), 2)  # Draw the border of the message box

    def draw_messages(self):
        y = self.__message_box_position[1] + self.__message_box_size[1] - 30  # Start drawing messages from the bottom of the box
        for message, alpha in reversed(self.__messages):
            if alpha > 0:  # Only draw messages with positive opacity
                self.display_text(message, (self.__message_box_position[0] + 10, y), alpha=alpha)  # Display the message
                y -= 30  # Move up for the next message

    def draw_health_bar(self, current_health, max_health, position, size, base_colour):
        health_ratio = current_health / max_health  # Calculate the proportion of current health to maximum health

        # Interpolate color from base_colour to white based on health ratio
        colour = tuple(int(base_colour[i] + (255 - base_colour[i]) * (1 - health_ratio)) for i in range(3))

        pygame.draw.rect(self.__screen, (0, 0, 0), (*position, *size))  # Draw the black background of the health bar
        pygame.draw.rect(self.__screen, (0, 0, 0), (*position, size[0], size[1]), 1)  # Draw the thin black outline
        pygame.draw.rect(self.__screen, (255, 255, 255), (*position, size[0], size[1]), 2)  # Draw the white border

        health_bar_width = int(size[0] * health_ratio)  # Calculate the width of the foreground health bar
        pygame.draw.rect(self.__screen, colour, (*position, health_bar_width, size[1]))  # Draw the health bar foreground with changing color

    def update_messages(self):
        for i, (text, alpha) in enumerate(self.__messages):
            if alpha > 0:  # Check if the message is still visible
                self.__messages[i] = (text, alpha - 5)  # Reduce alpha to make the message fade out
            else:
                self.__messages[i] = (text, 0)  # Ensure alpha does not go negative (fully transparent)

    def draw_enemy_name(self, name):
        font = pygame.font.SysFont(None, 30)  # Create a font object with size 30
        text_surface = font.render(name, True, (255, 255, 255))  # Render the enemy's name in white
        text_rect = text_surface.get_rect(center=(self.__screen.get_width() // 2, 30))  # Center the text at the top of the screen
        self.__screen.blit(text_surface, text_rect)  # Draw the text on the screen

    def combat(self, selected_character, enemy):
        if self.__enemy_speed >= 100:
            self.setTurn_order([enemy, selected_character])  # Enemy goes first if speed is high
        else:
            self.setTurn_order([selected_character, enemy])  # Player goes first otherwise

        running = True
        player_turn = True
        while running and self.__char_health > 0 and self.__enemy_hp > 0:
            self.setActing(self.__turn_order[0])  # Set the character currently acting
            self.setNon_acting(self.__turn_order[1])  # Set the character not acting
            damage = 0

            if player_turn:
                action = None
                while not action:
                    self.__screen.fill((31, 36, 33))  # Clear screen with background color
                    
                    # Draw player and enemy sprites
                    player_sprite_position = (self.__screen.get_width() // 4 - self.__player_sprite.get_width() // 2, 
                                            self.__screen.get_height() // 2 - self.__player_sprite.get_height() // 2)
                    enemy_sprite_position = (self.__screen.get_width() * 3 // 4 - self.__enemy_sprite.get_width() // 2, 
                                            self.__screen.get_height() // 2 - self.__enemy_sprite.get_height() // 2)
                    
                    self.__screen.blit(self.__player_sprite, player_sprite_position)  # Draw player sprite
                    self.__screen.blit(self.__enemy_sprite, enemy_sprite_position)  # Draw enemy sprite
                    
                    self.draw_enemy_name(self.__enemy.getEnemy_name())  # Draw enemy's name
                    self.draw_health_bar(self.__char_health, selected_character.getHealth(), (10, 10), (200, 20), (0, 255, 0))  # Draw player's health bar
                    self.draw_health_bar(self.__enemy_hp, enemy.getEnemy_hp(), (self.__screen.get_width() - 210, 10), (200, 20), (255, 0, 0))  # Draw enemy's health bar
                    self.draw_message_box()  # Draw message box
                    self.draw_messages()  # Draw messages
                    self.draw_buttons(self.__buttons, self.__button_colours, self.__button_texts)  # Draw action buttons
                    pygame.display.flip()  # Update the display

                    attack_cooldown = 1000  # 1 second cooldown between attacks
                    last_attack_time = 0  # Initialize the last attack time

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()  # Quit the game if window is closed
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            current_time = pygame.time.get_ticks()  # Get current time in milliseconds
                            mouse_pos = event.pos  # Get mouse position
                            action = self.check_button_click(mouse_pos, self.__buttons)  # Check which button was clicked
                            if action and current_time - last_attack_time >= attack_cooldown:
                                self.add_message(f"Player selected: {self.__button_texts[action]}")  # Add action message
                                if action == 'attack1':
                                    damage = random.randint(15, 20)  # Random damage for attack1
                                elif action == 'attack2':
                                    damage = random.randint(25, 30)  # Random damage for attack2
                                self.setEnemy_hp(max(0, self.__enemy_hp - damage))  # Apply damage to enemy
                                player_turn = False  # Switch to enemy's turn
                                last_attack_time = current_time  # Update last attack time
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            running = False  # Exit combat loop if ESC is pressed

            else:
                enemy_action = 'attack'  # Simplified enemy action
                if enemy_action == 'attack':
                    damage = random.randint(10, 20)  # Random damage for enemy attack
                    self.setChar_health(max(0, self.__char_health - damage))  # Apply damage to player
                    self.add_message(f"Enemy attacks for {damage} damage!")  # Add enemy attack message
                player_turn = True  # Switch to player's turn

            # Update messages and redraw the screen
            self.update_messages()
            self.__screen.fill((31, 36, 33))  # Clear screen for next frame

            # Redraw player and enemy sprites
            self.__screen.blit(self.__player_sprite, player_sprite_position)
            self.__screen.blit(self.__enemy_sprite, enemy_sprite_position)
            
            self.draw_enemy_name(self.__enemy.getEnemy_name())
            self.draw_health_bar(self.__char_health, selected_character.getHealth(), (10, 10), (200, 20), (0, 255, 0))
            self.draw_health_bar(self.__enemy_hp, enemy.getEnemy_hp(), (self.__screen.get_width() - 210, 10), (200, 20), (255, 0, 0))
            self.draw_message_box()
            self.draw_messages()
            self.draw_buttons(self.__buttons, self.__button_colours, self.__button_texts)
            pygame.display.flip()

            pygame.time.delay(1000)  # Pause to simulate turn-based actions
            
            self.setTurn_order(self.__turn_order[::-1])  # Reverse turn order

        # End of combat
        self.add_message("Combat Ended!")  # Add end of combat message
        selected_character.gain_experience(enemy.getEnemy_exp(), self.__screen)  # Award experience
        self.add_message(f"Experience Gained: {enemy.getEnemy_exp()}")  # Add experience gained message

        while True:
            self.__screen.fill((31, 36, 33))  # Clear screen with background color
            self.draw_enemy_name(self.__enemy.getEnemy_name())  # Redraw enemy's name

            # Determine which image to show based on the outcome
            if self.__char_health <= 0:
                result_image = self.__defeat_image  # Set defeat image
            else:
                result_image = self.__victory_image  # Set victory image

            # Calculate positions for image and buttons
            image_position = (self.__screen.get_width() // 2 - result_image.get_width() // 2, 
                            self.__screen.get_height() // 2 - result_image.get_height() // 2 - 50)
            continue_button_position = (self.__screen.get_width() // 2 - 80, 
                                        self.__screen.get_height() // 2 + 50)

            # Blit the result image
            self.__screen.blit(result_image, image_position)

            # Draw buttons and other elements
            self.draw_message_box()
            self.draw_messages()
            self.draw_buttons(self.__confirm_buttons, self.__confirm_button_colours, self.__confirm_button_texts)  # Draw confirmation buttons
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()  # Quit the game if window is closed
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # Get mouse position
                    action = self.check_button_click(mouse_pos, self.__confirm_buttons)  # Check which confirmation button was clicked
                    if action == 'continue':
                        if result_image == self.__victory_image:
                            return (True)  # Return True if victory
                        else:
                            return (False)  # Return False if defeat
                    elif action == 'exit':
                        pygame.quit()
                        quit()  # Quit the game if exit button is clicked
