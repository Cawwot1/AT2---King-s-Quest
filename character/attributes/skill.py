import pygame

class Skill():
    
    # Attributes
        #Skills stat
    __atri_attack = None
    __atri_defence = None
    __atri_speed = None
        
        #Skill Level
    __attack_lv = None
    __defence_lv = None
    
        #Plater
    __player = None
        
        #Skill Buttons
    __attack_image = None
    __attack_rect = None
    __defence_image = None
    __defence_rect = None
    __speed_image = None
    __speed_rect = None

    # Constructor    
    def __init__(self, player): # requests input (into constr.) for name & cha. class
        
        #Extra stats -> based on skill level)
        self.setAtri_atk(0)
        self.setAtri_def(0)
        self.setAtri_spd(0)
        self.setPlayer(player)

        #Skill Level
        self.setAttack_lv(0)
        self.setDefence_lv(0)

        #Skill Buttons & their rectangles (outline / hitbox) -> 100 x 100 pixels
        self.setAttack_image(pygame.image.load('assets/skills/attack.png').convert_alpha())
        self.setAttack_rect(self.__attack_image.get_rect(topleft=(50, 50)))
        self.setDefence_image(pygame.image.load('assets/skills/defence.png').convert_alpha())
        self.setDefence_rect(self.__defence_image.get_rect(topleft=(50, 150)))
        self.setSpeed_image(pygame.image.load('assets/skills/speed.png').convert_alpha())
        self.setSpeed_rect(self.__speed_image.get_rect(topleft=(50, 250)))
    
    #Getters
        #Skills
    def getAtri_atk(self): return self.__atri_attack
    def getAtri_def(self): return self.__atri_defence
    def getAtri_speed(self): return self.__atri_speed

        #Skill Level
    def getAttack_lv(self): return self.__attack_lv
    def getDefence_lv(self): return self.__defence_lv
    
        #Player
    def getPlayer(self):return self.__player

        #Skill Buttons
    def getAttack_image(self): return self.__attack_image
    def getAttack_rect(self): return self.__attack_rect
    def getDefence_image(self): return self.__defence_image
    def getDefence_rect(self): return self.__defence_rect
    def getSpeed_image(self): return self.__speed_image
    def getSpeed_rect(self): return self.__speed_rect

    #Setters
        #Skills
    def setAtri_atk(self, new_attack): self.__atri_attack = new_attack
    def setAtri_def(self, new_defence): self.__atri_defence = new_defence
    def setAtri_spd(self, new_speed): self.__atri_speed = new_speed

        #Skill Level
    def setAttack_lv(self, attack_lv): self.__attack_lv = attack_lv
    def setDefence_lv(self, defence_lv): self.__defence_lv = defence_lv

        #Player
    def setPlayer(self, player):self.__player = player

        #Skill Buttons
    def setAttack_image(self, attack_image): self.__attack_image = attack_image
    def setAttack_rect(self, attack_rect): self.__attack_rect = attack_rect
    def setDefence_image(self, defence_image): self.__defence_image = defence_image
    def setDefence_rect(self, defence_rect): self.__defence_rect = defence_rect
    def setSpeed_image(self, speed_image): self.__speed_image = speed_image
    def setSpeed_rect(self, speed_rect): self.__speed_rect = speed_rect

    #Behaviours

        #Boosts stats by a certain ammount (points * multiplier) based on skill level (calculated by boosted damage)
    def boost_attack(self, points):
        if self.__attack_lv > 30:
            self.setAtri_atk(self.__atri_attack + points * 10)
        elif self.__attack_lv > 10:
            self.setAtri_atk(self.__atri_attack + points * 5)
        else:
            self.setAtri_atk(self.__atri_attack + points * 3)
    
    def boost_defence(self, points):
        if self.__defence_lv > 30:
            self.setAtri_atk(self.__atri_defence + points * 8)
        elif self.__defence_lv > 10:
            self.setAtri_atk(self.__atri_defence + points * 4)
        else:
            self.setAtri_atk(self.__atri_defence + points * 2)

    def boost_speed(self, points): #Speed is incremented by 1 
        self.setAtri_spd(self.__atri_speed + points)
    
    # Skill Point Allocation Interface
    def show_skill_point_screen(self, screen, clock):
        running = True
        font = pygame.font.Font(None, 36)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Quit fuction
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: #Escape Key exits skill screen
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        if self.__attack_rect.collidepoint(mouse_pos): #If attack button is pressed
                            if self.__player.getAttribute_points() > 0: #There are atribute points
                                self.boost_attack(1) #Increase attack
                                self.setAttack_lv(self.__attack_lv + 1) #Increase attack level by 1
                                self.__player.setAttribute_points(self.__player.getAttribute_points() - 1) #Reduces atribute points by 1 (spent)
                        elif self.__defence_rect.collidepoint(mouse_pos): #Same as attack button
                            if self.__player.getAttribute_points() > 0:
                                self.boost_defence(1)
                                self.setDefence_lv(self.__defence_lv + 1)
                                self.__player.setAttribute_points(self.__player.getAttribute_points() - 1)
                        elif self.__speed_rect.collidepoint(mouse_pos): 
                            if self.__player.getAttribute_points() > 0:
                                self.boost_speed(1) #Increases speed by 1 (stat & level since they all increment by 1)
                                self.__player.setAttribute_points(self.__player.getAttribute_points() - 1)

            screen.fill((0, 0, 0))

            #Draw buttons
            screen.blit(self.__attack_image, self.__attack_rect.topleft)
            screen.blit(self.__defence_image, self.__defence_rect.topleft)
            screen.blit(self.__speed_image, self.__speed_rect.topleft)

            #Sets texts
            attack_text = font.render(f"Attack: {self.__attack_lv}", True, (255, 255, 255))
            defence_text = font.render(f"Defence: {self.__defence_lv}", True, (255, 255, 255))
            speed_text = font.render(f"Speed: {self.__atri_speed}", True, (255, 255, 255)) #speed atribute can be lv as well as it only increments by 1
            points_text = font.render(f"Skill Points: {self.__player.getAttribute_points()}", True, (255, 255, 255))
            
            #Renders Texts
            screen.blit(attack_text, (200, 50))
            screen.blit(defence_text, (200, 150))
            screen.blit(speed_text, (200, 250))
            screen.blit(points_text, (200, 350))

            #Instructions
            instructions_text = font.render("Click buttons to increase Attack, Defence, or Speed. ESC to exit.", True, (255, 255, 255))
            screen.blit(instructions_text, (200, 400))

            #Update Screen/Display
            pygame.display.flip()
            clock.tick(60) #Max frame rate
