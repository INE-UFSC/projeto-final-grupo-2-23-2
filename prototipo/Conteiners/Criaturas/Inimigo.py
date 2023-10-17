from Criatura import Criatura
import pygame
import math

# class Inimigo(Criatura):
#     def __init__(self, nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte, x, y):
#         super().__init__(nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte, x, y)
    
#     def perseguir():
#         pass

class Inimigo(pygame.sprite.Sprite):
    def __init__(self,pos, grupos):
        super().__init__(self, pos, grupos)
        self.image = pygame.image.load('prototipo/Graficos/jogador.png')
        self.rect = self.image.get_rect(topleft = pos)
        self.direcao = pygame.math.Vector2()
        self.velocidade = 5
        
    def mover(self,player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery

        # Calculate the angle to the player
        angle = math.atan2(dy, dx)

        # Calculate the enemy's movement based on the angle
        enemy_dx = self.direcao * math.cos(angle)
        enemy_dy = self.velocidade * math.sin(angle)

        # Update the enemy's position
        self.rect.x += enemy_dx
        self.rect.y += enemy_dy