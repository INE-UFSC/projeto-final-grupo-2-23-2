import pygame
from configuracoes import *

class Tile(pygame.sprite.Sprite):


    def __init__(self, pos, grupos,string):
        super().__init__(grupos)
        if string == 'a':
            self.image = pygame.image.load('prototipo/Graficos/_arvore.png')
        elif string == 'e':
            self.image = pygame.image.load('prototipo/Graficos/jogador.png')
        self.rect = self.image.get_rect(topleft = pos)
