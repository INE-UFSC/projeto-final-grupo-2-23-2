from data.components.Criatura import Criatura
import pygame
import os

class Inimigo(Criatura):
    def __init__(self, nome, vida, posicao, groups, sprites_visiveis, sprites_obstaculos):
        super().__init__(nome, vida, posicao, groups, sprites_visiveis, sprites_obstaculos)

        self.__image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../resources/graphics/enemies/' + nome + '.png').convert_alpha()
        self.__rect = self.image.get_rect(topleft=posicao)
        self.__hitbox = self.__rect.inflate(0, -10)

        #barra de vida
        self.tamanho_barra_vida = self.__rect.width*1.5
        self.razao_barra_vida = vida / self.tamanho_barra_vida # tamanho da barra

    
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
    
    # todo: gambiarra
    def barra_vida(self):
        sv = self.sprites_visiveis
        a0 = -sv.desvio.x + self.posicao[0]
        a1 = -sv.desvio.y + self.posicao[1] - 25
        desconto = (self.tamanho_barra_vida - self.__rect.width)/2
        pygame.draw.rect(sv.superficie, (255, 0, 0), (a0-desconto, a1, self.vida/self.razao_barra_vida, 10))
        pygame.draw.rect(sv.superficie, (255, 255, 255), (a0-desconto, a1, self.tamanho_barra_vida, 10),2)

    def update(self):
        self.barra_vida()
        self.mover()