from data.utils.settings import Settings
import pygame
import os

class Powerup(pygame.sprite.Sprite):
    def __init__(self, name, player, groups):
        super().__init__(groups)
        self.time = 0
        self.name = name
        self.icon = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + Settings().icons_folder + self.name + '.png').convert_alpha()
        self.player = player
        self.direction = self.player.status
        self.info = getattr(Settings(), self.name)

    def get_save_data(self):
        save_data = {
            'type': 'powerup',  
            'name': self.name,
            'time': self.time,
        }
        return save_data
    
    