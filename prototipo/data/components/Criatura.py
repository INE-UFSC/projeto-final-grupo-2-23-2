from abc import ABC, abstractmethod
import pygame
import os
from data.components.Inventario import Inventario


class Criatura(pygame.sprite.Sprite, ABC):
    def __init__(self, nome, vida, posicao, groups, sprites_visiveis, sprites_obstaculos):
        # insanciacao do Sprite
        super().__init__(groups)

        # atributos concretos
        self.__nome = nome
        self.__vida_maxima = 100
        self.__vida = 100
        self.__velocidade = 5
        self.__inventario = Inventario()

        # atributos mais subjetivos
        self.__posicao = posicao
        # vetor direcao
        self.__direcao = pygame.math.Vector2()
        self.__sprites_visiveis = sprites_visiveis
        self.__sprites_obstaculos = sprites_obstaculos

    # getters e setters
    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida
    
    @property
    def vida_maxima(self):
        return self.__vida_maxima
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade
    
    @property
    def inventario(self):
        return self.__inventario
    
    @property
    def direcao(self):
        return self.__direcao

    @property
    def posicao(self):
        return self.__posicao

    @direcao.setter
    def direcao(self, direcao):
        self.__direcao = direcao
    
    @property
    def sprites_obstaculos(self):
        return self.__sprites_obstaculos
    
    @property
    def sprites_visiveis(self):
        return self.__sprites_visiveis
    
    def mover(self):
        # normalizando a velocidade na diagonal
        if self.direcao.magnitude() != 0:
            self.direcao = self.direcao.normalize()
        
        # horizontal
        self.hitbox.x += self.direcao.x * self.velocidade
        self.colisao('horizontal')
        # vertical
        self.hitbox.y += self.direcao.y * self.velocidade
        self.colisao('vertical')
        self.rect.center = self.hitbox.center

    def colisao(self, direcao):
        # colisao horizontal
        if direcao == 'horizontal':
            for sprite in self.sprites_obstaculos:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direcao.x > 0 :
                        self.hitbox.right = sprite.hitbox.left
                    if self.direcao.x < 0 :
                        self.hitbox.left = sprite.hitbox.right
        # colisao vertical
        if direcao == 'vertical':
            for sprite in self.sprites_obstaculos:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direcao.y > 0 :
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direcao.y < 0 :
                        self.hitbox.top = sprite.hitbox.bottom

    def tomar_dano(self, quantia):   
        if self.vida > 0:
            self.vida -= quantia
        if self.vida < 0:
            self.vida = 0
    
    def tomar_cura(self, quantia):
        if self.vida < self.vida_maxima:
            self.vida += quantia
        if self.vida > self.vida_maxima:
            self.vida = vida_maxima 

    # todo
    def atacar(self):
        self.__item_ofensivo.atacar()
    # todo?
    def defender(self):
        self.__item_defensivo.defender()
    
    @abstractmethod
    def update(self):
        pass
