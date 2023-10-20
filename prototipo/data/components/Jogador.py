from data.components.Criatura import Criatura
import pygame
import os

class Jogador(Criatura):
    def __init__(self, nome, posicao, grupos):
        super().__init__(nome, posicao, grupos)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direcao.y = - 1
        elif keys[pygame.K_DOWN]:
            self.direcao.y = 1
        else:
            self.direcao.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.direcao.x = 1
        elif keys[pygame.K_LEFT]:
            self.direcao.x = -1
        else:
            self.direcao.x = 0


    def mover(self, velocidade):
        self.rect.center += self.direcao * velocidade
    
    def update(self):
        self.input()
        self.mover(self.velocidade)