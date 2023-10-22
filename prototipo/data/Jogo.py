import pygame
import sys
from data.components.Criatura import Criatura
from data.components.Jogador import Jogador
from data.components.ContainerFases import ContainerFases
from data.components.Fase import Fase
# from data.components.ContainerTelas import ContainerTelas


class Jogo:
    def __init__(self):
        # inciando pygame
        pygame.init()
        self.__fps = 60

        # vai pra na tela depois
        self.__largura = 1280
        self.__altura = 768
        self.__clock = pygame.time.Clock()

        # atributos
        self.__jogador = None
        self.__dificuldade = None

        # self.__telas = ContainerTelas()
        # todo: nao vimos mvc
        # gera tela vazia com tamanho
        self.tela = pygame.display.set_mode((self.__largura, self.__altura))
        pygame.display.set_caption('PartsFinder')
        
        self.__fases = ContainerFases()
        self.__fase_atual = self.fases.obter_fase()



    # getters e setters
    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def fases(self):
        return self.__fases

    @property
    def fase_atual(self):
        return self.__fase_atual

    @property
    def telas(self):
        return self.__telas

    def iniciar(self):
        self.jogar()

    def jogar(self):
        # loop jogo
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if self.fase_atual.jogador.vida == 0:
                pygame.quit()
            
            # prenchendo display com preto, reseta a malha
            self.fase_atual.superficie.fill('darkgreen')

            #roda fase
            self.fase_atual.rodar()

            # atualiza display
            pygame.display.update()

            # define fps do jogo
            self.__clock.tick(self.__fps)
            
    def mudar_menu(self):
        pass

    def checar_vitoria(self):
        pass

    def checar_ataque(self):
        pass
