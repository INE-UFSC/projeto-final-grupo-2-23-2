from data.components.Criatura import Criatura
import pygame
import os

class Inimigo(Criatura):
    def __init__(self, nome, posicao, grupos, sprites_obstaculo):
        super().__init__(nome, posicao, grupos, sprites_obstaculo)

    def mover(self, velocidade):
        pass
    
    def update(self):
        self.mover(self.velocidade)