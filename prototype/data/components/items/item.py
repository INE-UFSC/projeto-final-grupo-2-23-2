import pygame
import os

class Item(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status.split(' ')[0]
        self.image = pygame.Surface((40,40))
        self.rect = self.image.get_rect(center = player.rect.center)
        
        if direction == 'rigth':
            self.rect = self.image.get_rect(midleft = player.rect.midright)
            
        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft)

        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)
            
        else:
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)