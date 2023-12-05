from data.utils.settings import Settings
from data.game.powerup import Powerup
import pygame


class Guard(Powerup):
    def __init__(self, name, player, groups):
        super().__init__(name, player, groups)
        self.speed = 2
#         self.duration = 500
        self.stamina_cost = 70
#         self.cooldown = 600
        self.duration = self.info.get('duration')
        self.cooldown = self.info.get('cooldown')
        
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