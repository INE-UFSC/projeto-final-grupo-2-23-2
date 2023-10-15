import pygame
from configuracoes import *

class Tile(pygame.sprite.Sprite):


    def __init__(self, pos, grupos):
        super().__init__(grupos)
        self.image = pygame.image.load('prototipo\Graficos\_arvore.png')
        self.rect = self.image.get_rect(topleft = pos)
