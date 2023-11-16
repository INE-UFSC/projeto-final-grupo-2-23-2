import pygame

class Powerup(pygame.sprite.Sprite):
    def __init__(self, name, player, groups):
        super().__init__(groups)
        self.name = name
        self.player = player
        self.direction = player.direction