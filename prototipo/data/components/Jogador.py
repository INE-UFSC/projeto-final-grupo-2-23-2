from data.components.Criatura import Criatura
from ..config import *
import pygame
import os

class Jogador(Criatura):
    def __init__(self, nome, pos, groups, sprites_obstaculos):
        super().__init__(nome, pos, groups, sprites_obstaculos)

        self.__velocidade = 5 #Pode ser alterada quando o jogador pegar um power up (ainda nao ta implementado)
        self.__direcao = pygame.math.Vector2()

    @property 
    def velocidade(self):
        return self.__velocidade
    
    @property
    def direcao(self):
        return self.__direcao
    
    @direcao.setter
    def direcao(self, direcao):
        self.__direcao = direcao

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
                


    def mover(self, velocidade):
        if self.direcao.magnitude() != 0:
            self.direcao = self.direcao.normalize()
        self.rect.x += self.direcao.x * velocidade
        self.colisao('horizontal')
        self.rect.y += self.direcao.y * velocidade
        self.colisao('vertical')

    def update(self):
        self.input()
        self.mover(self.velocidade)