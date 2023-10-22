from data.components.Criatura import Criatura
import pygame
import os

class Inimigo(Criatura):
    def __init__(self, nome, posicao, grupos, sprites_obstaculo):
        super().__init__(nome, posicao, grupos, sprites_obstaculo)

        self.__image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../resources/graphics/enemies/' + nome + '.png').convert_alpha()
        self.__rect = self.image.get_rect(topleft=posicao)
        self.__hitbox = self.__rect.inflate(0, -10)
        self.__status = 'idle'
        self.__visao = 200
        
    

    def get_jogador_distancia_direcao(self,jogador):
        inimigo_vec = pygame.math.Vector2(self.rect.center)
        jogador_vec = pygame.math.Vector2(jogador.rect.center)
        distancia = (jogador_vec - inimigo_vec).magnitude()

        if distancia > 0:
            direcao = (jogador_vec - inimigo_vec).normalize()
        else:
            direcao = pygame.math.Vector2()

        return (distancia,direcao)
        

    def get_status(self, jogador):
        distancia = self.get_jogador_distancia_direcao(jogador)[0]

        if distancia <= self.visao:
            self.status = 'move'
        else:
            self.status = 'idle'

    def acao(self,jogador):
        if self.status == 'move':
            self.direcao = self.get_jogador_distancia_direcao(jogador)[1]
            
        else:
            self.direcao = pygame.math.Vector2()

    def inimigo_update(self,jogador):
        self.get_status(jogador)
        self.acao(jogador)

  
    def update(self):
        self.mover(self.velocidade)

#---------------------
# -Getters e Setters-
#---------------------

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, image):
        self.__image = image
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def visao(self):
        return self.__visao
    
    @visao.setter
    def visao(self, visao):
        self.__visao = visao
        
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