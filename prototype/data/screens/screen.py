import pygame
import os
from data.components.settings import Settings

class Screen:
    def __init__(self, game):
        self.game = game
        pygame.init()

        self.width, self.height = pygame.display.Info().current_w, pygame.display.Info().current_h

        self.background = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + "/../../resources/screens/intro2.png")
        self.background_rect = self.background.get_rect()
        
        self.background_x = (self.width - self.background_rect.width) // 2
        self.background_y = (self.height - self.background_rect.height) // 2
        
        self.font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/../../resources/fonts/stocky.ttf", 32)
        self.title = self.font.render('Parts Finder', True, (255, 255,255))
        self.title_rect = self.title.get_rect(x = self.width/2 - 130, y = 10)
        
        self.buttons = []
        self.wait_time = 300
        self.primary = True


    def get_button_clicks(self, mouse_pos, mouse_pressed):
        for button in self.buttons:
            if button.is_pressed(mouse_pos, mouse_pressed):
                return button    
        return None

    def blit(self):
        pygame.display.get_surface().blit(self.background, (self.background_x,self.background_y))
        pygame.display.get_surface().blit(self.title, self.title_rect)

        for button in self.buttons:
            pygame.display.get_surface().blit(button.image, button.rect)

        pygame.display.flip()
        Settings().clock.tick(Settings().fps)

