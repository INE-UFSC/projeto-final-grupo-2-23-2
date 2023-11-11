import pygame
import os


# todo : tratamento

class Tile(pygame.sprite.Sprite):
    def __init__(self, name, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__)) + '/../../../../resources/graphics/objects/' + name + '.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -20)