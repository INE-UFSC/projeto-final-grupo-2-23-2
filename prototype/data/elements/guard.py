from data.elements.powerup import Powerup
import pygame

import os

class Guard(Powerup):
    def __init__(self, name, player, groups):
        super().__init__(name, player, groups)
        direction = player.status
        self.speed = 2
        self.cooldown = 500
        self.time = None
        
        if "right" in direction:
            self.image = pygame.Surface((5,40))
            self.rect = self.image.get_rect(midleft = player.rect.midright)
            self.hitbox = self.rect.inflate(0, -26)
            
        elif 'left' in direction:
            self.image = pygame.Surface((5,40))
            self.rect = self.image.get_rect(midright = player.rect.midleft)
            self.hitbox = self.rect.inflate(0, -26)

        elif "down" in direction:
            self.image = pygame.Surface((40,5))
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)
            self.hitbox = self.rect.inflate(-26,0)
            
        elif "up" in direction:
            self.image = pygame.Surface((40,5))
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)
            self.hitbox = self.rect.inflate(-26, 0)
    