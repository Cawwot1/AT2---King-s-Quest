import pygame

class Skill():
    
    # Attributes
    _atri_attack = None
    _atri_defence = None
    _atri_speed = None

    # Constructor    
    def __init__(self, player): # requests input (into constr.) for name & cha. class
        self._atri_attack = 2
        self._atri_defence = 2
        self._atri_speed = 2
        
        self.__player = player

        #Buttons & their rectangles (outline / hitbox) -> 100 x 100 pixels
        self.attack_image = pygame.image.load('assets/skills/attack.png').convert_alpha()
        self.attack_rect = self.attack_image.get_rect(topleft=(50, 50))

        self.defence_image = pygame.image.load('assets/skills/defence.png').convert_alpha()
        self.defence_rect = self.defence_image.get_rect(topleft=(50, 150))

        self.speed_image = pygame.image.load('assets/skills/speed.png').convert_alpha()
        self.speed_rect = self.speed_image.get_rect(topleft=(50, 250))
    
    # Accessors
    def getAtri_atk(self):
        return self._atri_attack

    def getAtri_def(self):
        return self._atri_defence

    def getAtri_speed(self):
        return self._atri_speed

    # Mutators
    def setAtri_atk(self, new_attack):
        self._atri_attack = new_attack

    def setAtri_def(self, new_defence):
        self._atri_defence = new_defence
    
    def setAtri_spd(self, new_speed):
        self._atri_speed = new_speed

    # Behaviours -> To Be Improved
    def boost_attack(self, points):
        self.setAtri_atk(self._atri_attack + points)
    
    def boost_defence(self, points):
        self.setAtri_def(self._atri_defence + points)

    def boost_speed(self, points):
        self.setAtri_spd(self._atri_speed + points)
    
    # Skill Point Allocation Interface
    def show_skill_point_screen(self, screen, clock):
        running = True
        font = pygame.font.Font(None, 36)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        if self.attack_rect.collidepoint(mouse_pos):
                            if self.__player.getAttribute_points() > 0:
                                self.boost_attack(1)
                                self.__player.setAttribute_points(self.__player.getAttribute_points() - 1)
                        elif self.defence_rect.collidepoint(mouse_pos):
                            if self.__player.getAttribute_points() > 0:
                                self.boost_defence(1)
                                self.__player.setAttribute_points(self.__player.getAttribute_points() - 1)
                        elif self.speed_rect.collidepoint(mouse_pos):
                            if self.__player.getAttribute_points() > 0:
                                self.boost_speed(1)
                                self.__player.setAttribute_points(self.__player.getAttribute_points() - 1)

            screen.fill((0, 0, 0))

            # Draw buttons
            screen.blit(self.attack_image, self.attack_rect.topleft)
            screen.blit(self.defence_image, self.defence_rect.topleft)
            screen.blit(self.speed_image, self.speed_rect.topleft)

            # Render text
            attack_text = font.render(f"Attack: {self.getAtri_atk()}", True, (255, 255, 255))
            defence_text = font.render(f"Defence: {self.getAtri_def()}", True, (255, 255, 255))
            speed_text = font.render(f"Speed: {self.getAtri_speed()}", True, (255, 255, 255))
            points_text = font.render(f"Skill Points: {self.__player.getAttribute_points()}", True, (255, 255, 255))

            screen.blit(attack_text, (200, 50))
            screen.blit(defence_text, (200, 150))
            screen.blit(speed_text, (200, 250))
            screen.blit(points_text, (200, 350))

            # Instructions
            instructions_text = font.render("Click buttons to increase Attack, Defence, or Speed. ESC to exit.", True, (255, 255, 255))
            screen.blit(instructions_text, (200, 400))

            pygame.display.flip()
            clock.tick(60)
