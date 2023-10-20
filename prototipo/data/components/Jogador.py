from data.components.Criatura import Criatura
import pygame
import os

# class Jogador(Criatura):
#     def __init__(self, nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte, x, y):
#         super().__init__(nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte, x, y)
        
#     def pegar_item(self,item):
#         self.__inventario.adicionar_item(item)

class Jogador(pygame.sprite.Sprite):

    def __init__(self, pos, grupos):
        super().__init__(grupos)
        self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/../../resources/graphics/player/player.png')
        self.rect = self.image.get_rect(topleft = pos)
        self.direcao = pygame.math.Vector2()
        self.velocidade = 5

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