from data.components.Criatura import Criatura
import pygame
import os

class Jogador(Criatura):
    def __init__(self, nome, posicao, groups, sprites_obstaculos,criar_ataque,destruir_ataque):
        super().__init__(nome, posicao, groups, sprites_obstaculos)
        
        # todo: analisar heranca inimigo jogador
        self.__image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../resources/graphics/player/' + nome + '.png').convert_alpha()
        self.__rect = self.image.get_rect(topleft=posicao)
        self.__hitbox = self.__rect.inflate(0, -26)

        #caracteristicas do player
        self.status = 'baixo'
        self.atacando = False
        self.tempo_ataque = None
        self.cooldown_ataque = 250
        
        #metodos vindos de fase
        self.criar_ataque = criar_ataque
        self.destruir_ataque = destruir_ataque
        
        
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.atacando == False:
            self.direcao.y = -1   
            self.status = 'cima'

        elif keys[pygame.K_DOWN] and self.atacando == False:
            self.direcao.y = 1  
            self.status = 'baixo'
        else:
            self.direcao.y = 0

        if keys[pygame.K_LEFT] and self.atacando == False:
            self.direcao.x = -1
            self.status = 'esquerda'

        elif keys[pygame.K_RIGHT] and self.atacando == False:
            self.direcao.x = 1
            self.status = 'direita'
        else:
            self.direcao.x = 0
            
        if keys[pygame.K_SPACE]:
            if not self.atacando:
                self.atacando = True
                self.tempo_ataque = pygame.time.get_ticks()
                self.criar_ataque()

    def update(self):
        self.input()
        self.mover(self.velocidade)
        self.cooldowns()
    
    def cooldowns(self):
        tempo_atual = pygame.time.get_ticks()
        
        if self.atacando:
            if tempo_atual - self.tempo_ataque >= self.cooldown_ataque:
                self.destruir_ataque()
                self.atacando = False
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
