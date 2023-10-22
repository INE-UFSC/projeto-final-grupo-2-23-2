from data.components.Criatura import Criatura
import pygame
import os

class Jogador(Criatura):
    def __init__(self, nome, posicao, groups, sprites_obstaculos):
        super().__init__(nome, posicao, groups, sprites_obstaculos)
        
        # todo: analisar heranca inimigo jogador
        self.__image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../resources/graphics/player/' + nome + '.png').convert_alpha()
        self.__rect = self.image.get_rect(topleft=posicao)
        self.__hitbox = self.__rect.inflate(0, -26)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direcao.y = -1   

        elif keys[pygame.K_DOWN]:
            self.direcao.y = 1  
        else:
            self.direcao.y = 0

        if keys[pygame.K_LEFT]:
            self.direcao.x = -1

        elif keys[pygame.K_RIGHT]:
            self.direcao.x = 1
        else:
            self.direcao.x = 0

    def update(self):
        self.input()
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
