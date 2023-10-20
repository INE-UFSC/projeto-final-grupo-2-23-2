import pygame
from map_data.mvp_map import *

class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, grupos):
        super().__init__(grupos)
        self.image = pygame.image.load('graphics/objects/tree.png')
        self.rect = self.image.get_rect(topleft = pos)
