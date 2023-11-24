from data.components.settings import Settings
import pygame
import os

class Powerup(pygame.sprite.Sprite):
    def __init__(self, name, player, groups):
        super().__init__(groups)
        self.name = name
        self.icon = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__)) + '/../../resources/elements/powerups/icons/' + self.name + '.png').convert_alpha()
        self.player = player
        self.direction = self.player.status
        self.time = 0
        self.info = getattr(Settings(), self.name)