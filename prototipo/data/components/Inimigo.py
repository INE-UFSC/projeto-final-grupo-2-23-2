from data.components.Criatura import Criatura
import pygame
import os

class Inimigo(Criatura):
    def __init__(self, nome, posicao, grupos, sprites_obstaculo):
        super().__init__(nome, posicao, grupos, sprites_obstaculo)

        self.__image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../resources/graphics/enemies/' + nome + '.png').convert_alpha()
        self.__rect = self.image.get_rect(topleft=posicao)
        self.__hitbox = self.__rect.inflate(0, -10)

    def mover(self, velocidade):
        pass
    
    def update(self):
        self.mover(self.velocidade)
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, image):
        self.__image = image
    
    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def hitbox(self):
        return self.__hitbox
    
    @rect.setter
    def hitbox(self, hitbox):
        self.__hitbox = hitbox