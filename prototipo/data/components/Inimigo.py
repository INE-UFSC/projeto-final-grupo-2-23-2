from data.components.Criatura import Criatura
from .Jogador import Jogador
import pygame
import os

class Inimigo(Criatura):
    def __init__(self, nome, vida, posicao, groups, sprites_visiveis, sprites_obstaculos):
        super().__init__(nome, vida, posicao, groups, sprites_visiveis, sprites_obstaculos)

        self.__image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../resources/graphics/enemies/' + nome + '.png').convert_alpha()
        self.__rect = self.image.get_rect(topleft=posicao)
        self.__hitbox = self.__rect.inflate(0, -10)
        self.__status = 'idle'
        self.__visao = 200
        self.__sprite_tipo = 'inimigo'
        self.__velocidade = 2
        self.__ataqueAlcance = 50
        self.__dano = 10

        self.atacando = False
        self.tempo_ataque = None
        self.cooldown_ataque = 300


        
        #barra de vida
        self.tamanho_barra_vida = self.__rect.width*1.5
        self.razao_barra_vida = vida / self.tamanho_barra_vida # tamanho da barra

    @property
    def sprite_tipo(self):
        return self.__sprite_tipo
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def ataqueAlcance(self):
        return self.__ataqueAlcance
    
    @property
    def dano(self):
        return self.__dano
        
    

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

        if distancia <= self.ataqueAlcance:
            self.status = 'atacar'

        elif distancia <= self.visao:
            self.status = 'move'
        else:
            self.status = 'idle'

    def acao(self,jogador):
        if self.status == 'atacar' and self.cooldowns():
            self.atacar(jogador)
        
        if self.status == 'move':
            self.direcao = self.get_jogador_distancia_direcao(jogador)[1]
        else:
            self.direcao = pygame.math.Vector2()

    def atacar(self, jogador: Jogador):
        jogador.vida -= self.dano
        self.atacando = True
        self.tempo_ataque = pygame.time.get_ticks()

    def inimigo_update(self,jogador):
        self.get_status(jogador)
        self.acao(jogador)

    def cooldowns(self):
        tempo_atual = pygame.time.get_ticks()
        if self.atacando:
            if tempo_atual - self.tempo_ataque >= self.cooldown_ataque:
                self.atacando = False
                return True
            else:
                return False
        else:
            return True    
    
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
        self.cooldowns()

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