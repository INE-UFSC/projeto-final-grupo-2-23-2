import pygame
import os

class Powerup(pygame.sprite.Sprite):
    def __init__(self, name, player, groups):
        super().__init__(groups)
        self.name = name
        self.icon = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__)) + '/../../resources/elements/powerups/icons/' + name + '.png').convert_alpha()
        self.player = player
        self.direction = player.direction