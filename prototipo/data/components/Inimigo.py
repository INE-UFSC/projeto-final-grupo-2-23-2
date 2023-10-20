from data.components.Criatura import Criatura
import pygame
import os

class Inimigo(Criatura):
    def __init__(self, nome, posicao, grupos):
        super().__init__(nome, posicao, grupos)

    def mover(self, velocidade):
        pass
    
    def update(self):
        self.mover(self.velocidade)