from data.elements.powerup import Powerup
import pygame

import os

class Guard(Powerup):
    def __init__(self, name, player, groups):
        super().__init__(name, player, groups)
        self.duration = 500
        self.cooldown = 600
        
        if "right" in self.direction:
            self.image = pygame.Surface((5,40))
            self.rect = self.image.get_rect(midleft = player.rect.midright)
            
        elif 'left' in self.direction:
            self.image = pygame.Surface((5,40))
            self.rect = self.image.get_rect(midright = player.rect.midleft)

        elif "down" in self.direction:
            self.image = pygame.Surface((40,5))
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)
            
        elif "up" in self.direction:
            self.image = pygame.Surface((40,5))
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)

        self.hitbox = self.rect