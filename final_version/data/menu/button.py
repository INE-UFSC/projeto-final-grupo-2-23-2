from data.utils.settings import Settings
from data.utils.audio import Audio
import pygame
import os

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, action):
        self.font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + Settings().button_font, 32)
        self.content = content
        self.action = action

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

    def is_pressed(self, pos , pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                Audio().play_sound("menu")
                return True
            return False
        return False
    

