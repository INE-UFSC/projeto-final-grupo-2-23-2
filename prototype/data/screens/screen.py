import pygame
import os

class Screen:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.height = self.game.height
        self.width = self.game.width

        self.background = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + "/../../resources/screens/intro2.png")
        self.background_rect = self.background.get_rect()
        
        self.background_x = (self.width - self.background_rect.width) // 2
        self.background_y = (self.height - self.background_rect.height) // 2
        
        self.font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + "/../../resources/fonts/stocky.ttf", 32)
        self.title = self.font.render('Parts Finder', True, (255, 255,255))
        self.title_rect = self.title.get_rect(x = self.game.width/2 - 130, y = 10)
        
        self.buttons = []
        self.wait_time = 300
        self.primary = True


    def get_button_clicks(self, mouse_pos, mouse_pressed):
        for button in self.buttons:
            if button.is_pressed(mouse_pos, mouse_pressed):
                return button    
        return None

    def blit(self):
        self.game.view.blit(self.background, (self.background_x,self.background_y))
        self.game.view.blit(self.title, self.title_rect)

        for button in self.buttons:
            self.game.view.blit(button.image, button.rect)

        pygame.display.flip()
        self.game.clock.tick(self.game.fps)

