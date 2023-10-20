from abc import ABC, abstractmethod
import pygame
import os
from data.components.Inventario import Inventario


class Criatura(pygame.sprite.Sprite, ABC):
    def __init__(self, nome, posicao, grupos):
        # insanciacao do Sprite
        super().__init__(grupos)

        # atributos concretos
        self.__nome = nome
        self.__vida = 100
        self.__velocidade = 5
        self.__inventario = Inventario()
        self.__image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../resources/graphics/player/' + nome + '.png').convert_alpha()

        # atributos subjetivos
        self.__rect = self.image.get_rect(topleft=posicao)
        self.__direcao = pygame.math.Vector2()

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
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade
    
    @property
    def inventario(self):
        return self.__inventario

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def direcao(self):
        return self.__direcao

    # todo
    def atacar(self):
        self.__item_ofensivo.atacar()
    # todo?
    def defender(self):
        self.__item_defensivo.defender()
    
    def mover(self, velocidade):
        self.rect.center += self.direcao * velocidade

    @abstractmethod
    def update(self):
        pass
