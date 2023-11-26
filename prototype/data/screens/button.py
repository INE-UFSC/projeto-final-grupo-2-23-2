from data.components.settings import Settings
import pygame
import os
import sys

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + Settings().button_font, fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center = (self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

        #self.menu_sound = pygame.mixer.Sound(-C:\Users\USUARIO\Documents\GitHub\projeto-final-grupo-2-23-2\prototype\resources\sounds\Acceptsucesso.wav)
        self.menu_sound = pygame.mixer.Sound('C:/Users/USUARIO/Documents/GitHub/projeto-final-grupo-2-23-2/prototype/data/screens/../../resources/sounds/Acceptsucesso.wav' )
        #self.menu_sound = pygame.mixer.Sound('c:/Users/USUARIO/Documents/GitHub/projeto-final-grupo-2-23-2/prototype/../../resources/sounds/Acceptsucesso.wav' )
        


    def is_pressed(self, pos , pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                pygame.mixer.Sound.play(self.menu_sound)
                return True
            return False
        return False
    

